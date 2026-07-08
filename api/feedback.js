import { put } from '@vercel/blob';

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'method not allowed' });
  }
  const { text, lang, website } = req.body || {};
  if (website) {
    return res.status(200).json({ ok: true });
  }
  if (!text || typeof text !== 'string' || !text.trim() || text.length > 3000) {
    return res.status(400).json({ error: 'invalid' });
  }
  const id = `${Date.now()}-${Math.random().toString(36).slice(2, 8)}`;
  await put(
    `feedback/${id}.json`,
    JSON.stringify({ text: text.trim(), lang: lang || null, at: new Date().toISOString() }),
    { access: 'private', contentType: 'application/json' }
  );
  return res.status(200).json({ ok: true });
}

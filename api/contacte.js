// Formulari de contacte d'escoladansa.com → tina.colome@gmail.com, de moment (+ còpia oculta).
// Substitueix contacte.php de Webempresa: vercel.json reescriu /contacte.php cap aquí,
// així la home no canvia. El correu surt pel servidor SMTP de la bústia de l'escola.
// Variables a Vercel (Settings → Environment Variables): SMTP_HOST, SMTP_PORT,
// SMTP_USER, SMTP_PASS. Les posa el Xavi; no van mai al repo.
import nodemailer from 'nodemailer'

const DESTI = 'tina.colome@gmail.com' // de moment (10-nov-2026), per decisió del Xavi
const COPIA = 'xcolome@hotmail.com'

const neteja = (v) => String(v ?? '').replace(/[\r\n]+/g, ' ').trim()
const json = (dades, status = 200) =>
  new Response(JSON.stringify(dades), {
    status,
    headers: { 'Content-Type': 'application/json; charset=utf-8' },
  })

export async function POST(request) {
  let form
  try {
    form = await request.formData()
  } catch {
    return json({ ok: false }, 400)
  }

  const nom = neteja(form.get('nom')).slice(0, 120)
  const contacte = neteja(form.get('contacte')).slice(0, 160)
  const missatge = String(form.get('missatge') ?? '').trim().slice(0, 4000)
  const honeypot = String(form.get('web') ?? '')
  const torn = Number(form.get('torn') ?? 0)

  // anti-spam: honeypot ple o formulari enviat en menys de 3 segons = bot
  if (honeypot !== '' || !(torn >= 3) || !nom || !contacte || !missatge) {
    return json({ ok: false })
  }

  const esEmail = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(contacte)
  const transport = nodemailer.createTransport({
    host: process.env.SMTP_HOST,
    port: Number(process.env.SMTP_PORT || 465),
    secure: Number(process.env.SMTP_PORT || 465) === 465,
    auth: { user: process.env.SMTP_USER, pass: process.env.SMTP_PASS },
  })

  try {
    await transport.sendMail({
      from: `"Web escoladansa.com" <${process.env.SMTP_USER || DESTI}>`,
      to: DESTI,
      bcc: COPIA,
      replyTo: esEmail ? { name: nom, address: contacte } : undefined,
      subject: `Consulta web: ${nom}`,
      text:
        "Nou missatge del formulari de contacte d'escoladansa.com\n\n" +
        `Nom: ${nom}\nContacte: ${contacte}\n\nMissatge:\n${missatge}\n`,
    })
    return json({ ok: true })
  } catch (e) {
    console.error('contacte: no s’ha pogut enviar', e?.message)
    return json({ ok: false }, 502)
  }
}

export function GET() {
  return json({ ok: false }, 405)
}

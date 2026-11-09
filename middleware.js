// Markdown per a agents d'IA: si la petició demana `Accept: text/markdown`, es
// respon amb l'index.md de la pàgina en lloc de l'index.html (negociació de contingut,
// el que feia el .htaccess a Webempresa). Si la pàgina no té index.md, es deixa passar l'HTML.
// A vercel.json no es pot fer: allà les regles s'apliquen després de servir el fitxer.
export const config = {
  matcher: ['/((?!assets/|api/|.*\\.(?:jpg|jpeg|png|webp|svg|ico|mp4|webm|xml|txt|pdf|json|js|css|md)$).*)'],
}

export default async function middleware(request) {
  const accept = request.headers.get('accept') || ''
  if (!/text\/markdown/i.test(accept)) return

  const url = new URL(request.url)
  let cami = url.pathname
  if (cami.endsWith('/index.html')) cami = cami.slice(0, -'index.html'.length)
  if (!cami.endsWith('/')) return

  const md = await fetch(new URL(`${cami}index.md`, url.origin), { headers: { accept: 'text/plain' } })
  if (!md.ok) return

  return new Response(md.body, {
    status: 200,
    headers: {
      'Content-Type': 'text/markdown; charset=utf-8',
      Vary: 'Accept',
      Link: '<https://escoladansa.com/llms.txt>; rel="describedby llms-txt", <https://escoladansa.com/sitemap.xml>; rel="sitemap"',
    },
  })
}

"""Construcció a Vercel: comprova els enllaços i copia la web pública a _web/.

Només es publica el que hi ha a _web/ (outputDirectory de vercel.json): el generador,
els fluxos de GitHub, la funció de contacte i els fitxers de configuració queden fora.
Si hi ha algun enllaç intern trencat, la construcció falla i no es publica res
(el mateix que feia el desplegament per FTPS).
"""
import os
import shutil
import subprocess
import sys

ARREL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SORTIDA = os.path.join(ARREL, "_web")

# el mateix que excloïa el desplegament a Webempresa, més el que és propi de Vercel
FORA = {
    ".git", ".github", ".gitignore", ".vercel", ".vercelignore", "generador", "api",
    "node_modules", "_web", "info", ".env", ".env.local", "CLAUDE.md", "README.md", ".htaccess", "contacte.php",
    "package.json", "package-lock.json", "vercel.json", "middleware.js", "Thumbs.db", "desktop.ini",
}

env = dict(os.environ, PYTHONIOENCODING="utf-8")
r = subprocess.run([sys.executable, os.path.join(ARREL, "generador", "comprova_enllacos.py")], cwd=ARREL, env=env)
if r.returncode != 0:
    sys.exit("enllaços trencats: no es publica")

shutil.rmtree(SORTIDA, ignore_errors=True)
os.makedirs(SORTIDA)
n = 0
for nom in os.listdir(ARREL):
    if nom in FORA:
        continue
    origen = os.path.join(ARREL, nom)
    if os.path.isdir(origen):
        shutil.copytree(origen, os.path.join(SORTIDA, nom),
                        ignore=shutil.ignore_patterns("Thumbs.db", "desktop.ini", "__pycache__"))
    else:
        shutil.copy2(origen, os.path.join(SORTIDA, nom))
    n += 1
print(f"_web: {n} elements copiats")

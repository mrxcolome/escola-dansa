<?php
// Formulari de contacte d'escoladansa.com → info@escoladansa.com (+ còpia oculta)
header('Content-Type: application/json; charset=utf-8');
if ($_SERVER['REQUEST_METHOD'] !== 'POST') { http_response_code(405); echo '{"ok":false}'; exit; }

// neteja per a valors que van a capçaleres (anti header-injection)
function neteja($v) { return trim(str_replace(["\r", "\n"], ' ', $v ?? '')); }

$nom      = mb_substr(neteja($_POST['nom'] ?? ''), 0, 120);
$contacte = mb_substr(neteja($_POST['contacte'] ?? ''), 0, 160);
$missatge = mb_substr(trim($_POST['missatge'] ?? ''), 0, 4000);
$honeypot = $_POST['web'] ?? '';
$torn     = (int) ($_POST['torn'] ?? 0);

// anti-spam: honeypot ple o formulari enviat en menys de 3 segons = bot
if ($honeypot !== '' || $torn < 3 || $nom === '' || $contacte === '' || $missatge === '') {
    echo '{"ok":false}';
    exit;
}

$cos = "Nou missatge del formulari de contacte d'escoladansa.com\n\n"
     . "Nom: $nom\n"
     . "Contacte: $contacte\n\n"
     . "Missatge:\n$missatge\n";

$capceleres = "From: Web escoladansa.com <info@escoladansa.com>\r\n"
            . "Bcc: xcolome@hotmail.com\r\n"
            . "Content-Type: text/plain; charset=utf-8\r\n"
            . "Content-Transfer-Encoding: 8bit\r\n";
if (filter_var($contacte, FILTER_VALIDATE_EMAIL)) {
    $capceleres .= 'Reply-To: ' . mb_encode_mimeheader($nom, 'UTF-8') . " <$contacte>\r\n";
}

$assumpte = mb_encode_mimeheader("Consulta web: $nom", 'UTF-8');
$ok = mail('info@escoladansa.com', $assumpte, $cos, $capceleres);
echo json_encode(['ok' => (bool) $ok]);

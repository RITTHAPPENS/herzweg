# Design: Herzweg24

Visuelle Welt "Der rote Faden": Leinen als Grund, eine rote Garnlinie in der Strichsprache des Logos, Vorstich-Nähte als Trenner. Warm, persönlich, regional, ohne Pflegeheim- oder Klinikoptik.

## Farben

| Token | Wert | Einsatz |
|---|---|---|
| `--linen` | #f2e8dc | Seitengrund (Hausfarbe Creme) |
| `--linen-deep` | #e9dccb | Abwechselnde Sektionen |
| `--linen-light` | #f8f1e8 | Karten, Flächen auf Leinen |
| `--thread` | #ac5454 | Hausfarbe Rot: Akzente, Faden, Farbflächen (Kurzzeitbetreuung, Abschluss) |
| `--thread-dark` | #8e3f40 | Primär-Buttons (weißer Text, AA) |
| `--thread-ink` | #7a3536 | Links und roter Text auf Leinen (AA) |
| `--ink` | #2e2424 | Text |
| `--ink-soft` | #5a4a47 | Sekundärtext |
| `--stitch` | #ac5454 / 55 % | Gestrichelte Nähte |

Nur ein Akzent (Rot). Farbflächen in Rot sind bewusste Sektionen, kein Themenwechsel. Nur helles Schema: Hausfarben sind vorgegeben, Zielgruppe teils älter.

## Typografie

- Überschriften: Bricolage Grotesque 700/800, selbst gehostet, `letter-spacing: -.02em`.
- Text: Atkinson Hyperlegible Next 400/700 (gut lesbar für ältere Menschen), Grundgröße 19px.
- Ziffern im Text kommen aus Bricolage (Font "Digits" per `unicode-range`), weil Atkinson eine durchgestrichene Null hat.
- "24-Stunden-Pflege" in Überschriften nie am Bindestrich umbrechen (`.nowrap`).

## Formen und Material

- Radien: Karten 18px, kleine Flächen 10px, Buttons und Pills voll rund.
- Nähte: `2px dashed` in `--stitch` statt durchgezogener Linien.
- Primär-Button mit innerer Ziernaht (gestrichelte Outline).
- Stickrahmen: ovaler Holzrahmen um das Hero-Foto, später Teamfoto.
- Schatten rötlich getönt, weich, mit Versatz.
- Icons: Phosphor Regular, lokal (`assets/icons`).

## Signatur

Der rote Faden (SVG, `pathLength="1"`) zeichnet sich beim Erscheinen: aus dem Stickrahmen im Hero und als Verbindung der drei Ablaufschritte (horizontal am Desktop, vertikal mobil). Bei reduzierter Bewegung sofort sichtbar.

## Conversion

Drei Wege, überall gleich benannt: "Jetzt anrufen" (tel), "Per WhatsApp schreiben", "Rückruf anfordern" (Microsoft Forms, neuer Tab). Alle Links tragen `data-conversion="anruf|whatsapp|formular"` für das Google-Ads-Tracking. Mobil feste Kontaktleiste unten.

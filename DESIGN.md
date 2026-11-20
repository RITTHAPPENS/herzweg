# Design: Herzweg24

Ruhig und seriös: helle Basis, große echte Fotos, klare Typografie. Das Hausrot steht nur für Buttons, Akzente und die Nummern im Ablauf. Keine Dekoelemente, keine Verläufe, keine Effekte.

## Farben

| Token | Wert | Einsatz |
|---|---|---|
| `--bg` | #fcfaf7 | Seitengrund |
| `--cream-soft` | #f7f1ea | Abwechselnde Sektionen |
| `--cream` | #f2e8dc | Hausfarbe Creme: Kontaktbox, Foto-Platzhalter |
| `--line` | #e7ddd1 | 1px-Linien und Rahmen |
| `--red` | #ac5454 | Hausfarbe Rot: Akzente, Haken, Nummern, Linien über den Fakten |
| `--red-dark` | #8e3f40 | Primär-Button (weißer Text, AA) |
| `--ink` | #23201f | Text |
| `--ink-soft` | #5b5552 | Sekundärtext |

## Typografie

Figtree (400, 500, 600, 700), selbst gehostet. Überschriften 700, Zwischenüberschriften 600, Text 19px mit Zeilenhöhe 1.65. "24-Stunden-Pflege" in Überschriften nicht am Bindestrich umbrechen (`.nowrap`).

## Formen

Einheitlicher Radius 8px für Buttons, Bilder, Boxen. Linien 1px. Keine Schatten.

## Aufbau

Hero zentriert mit großem rundem Logo, H1, Unterzeile, zwei Buttons, darunter breites Foto. Danach wechseln helle und cremefarbene Sektionen.

## Conversion

Drei Wege, überall gleich benannt: "Jetzt anrufen", "Per WhatsApp schreiben", "Rückruf anfordern" (Microsoft Forms, neuer Tab). Links tragen `data-conversion="anruf|whatsapp|formular"`. Mobil feste Kontaktleiste unten.

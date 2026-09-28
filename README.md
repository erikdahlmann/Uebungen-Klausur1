# Übungen zur 1. Klausur — Mathematik LK Q2.1

28 Übungsaufgaben mit ausklappbaren Musterlösungen für den Mathematik-Leistungskurs
Q2.1 (Abitur 2027), Paul-Klee-Gymnasium Overath.

**Live:** https://erikdahlmann.github.io/Uebungen-Klausur1/

## Inhalt

### Teil A — hilfsmittelfrei, 24 Aufgaben, 137 BE

| Block | Thema | Aufgaben |
|---|---|---|
| A1 | Abstand Punkt–Ebene | 2 |
| A2 | Abstand Punkt–Gerade | 3 |
| A3 | Lage und Abstand zweier Geraden | 3 |
| A4 | Lot und Spiegelung | 3 |
| A5 | Vierfeldertafel und Unabhängigkeit | 3 |
| A6 | Empirische Kenngrößen | 3 |
| A7 | Simulationen beschreiben | 4 |
| A8 | Ereignisse als Mengen | 3 |

### Teil B — mit WTR und Formelsammlung, 4 Aufgaben, 130 BE

| Block | Aufgabe | BE |
|---|---|---|
| B1 | Festzelt | 32 |
| B1 | Drohne und Solarfläche | 34 |
| B2 | Fahrradverleih | 32 |
| B2 | Qualitätskontrolle und Messdaten | 32 |

Teil A ist ohne Hilfsmittel lösbar; die Ergebnisse sind exakte Brüche oder Wurzeln.
Für die empirische Varianz gilt durchgehend der Divisor `n`.

Jede Musterlösung besteht aus drei Teilen: *Der Weg* (welches Verfahren und warum),
die Rechnung Schritt für Schritt und ein Hinweis auf den häufigsten Fehler.

## Technik

Eine einzelne `index.html` ohne Framework. KaTeX liegt unter `vendor/` lokal bei,
damit die Seite ohne Netzzugriff auf fremde Server funktioniert.

Neu bauen:

```bash
python3 build_site.py
```

Aufgaben und Lösungen stehen als Datenstruktur oben in `build_site.py`;
`aufgaben.json` ist der maschinenlesbare Auszug daraus.

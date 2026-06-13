# Übersicht Tag 38 – Stop Losses: Platzierung und Logik

**Erstelldatum:** 2026-06-13
**Quelldatei:** Tag38-Stop Losses
**Typ:** Technik-Tag

---

## Überblick

Tag 38 erklärt die systematische Stop-Loss-Platzierung. Stops werden immer außerhalb des Liquiditätssweeps gesetzt – weil der Kurs dieses Level bereits getestet hat und eine Rückkehr dorthin das Setup invalidiert. Der Spread-Buffer ist Pflicht. Ausnahmen für das R:R werden erklärt.

---

## Teilgebiete

### Grundprinzip: Stop über/unter dem Sweep

- Bullisches Setup: Stop unter dem Liquiditätssweep-Tief
- Bärisches Setup: Stop über dem Liquiditätssweep-Hoch
- Logik: Wenn Kurs nochmals unter das Sweep-Tief fällt, war das Sweep kein echter Auslöser → Setup invalidiert

### Spread-Buffer ist Pflicht

- Nie Stop exakt auf das Sweep-Level setzen
- Immer 5–10 Pips Puffer addieren (je nach Instrument)
- Warum: Broker-Spread + normale Preisschwankungen könnten Stop unnötig auslösen
- Ohne Buffer: "Stop-Hunting" durch eigenen Broker möglich

### Ausnahmen: R:R-Optimierung

- Wenn Stop über Sweep zu groß ist für das gewünschte R:R...
- Kann Stop näher am Entry gesetzt werden (z.B. unter OB statt unter Sweep)
- Risiko: Wird häufiger ausgestoppt
- Empfehlung für Anfänger: Immer Stop unter Sweep – nie unter OB

### Stop-Größe und Entry-Typ

| Entry | Stop-Platzierung | Stop-Größe |
|-------|-----------------|-----------|
| Entry 1 (nach BoS) | Unter Sweep | Größer |
| Entry 2 (nach OB) | Unter OB oder Sweep | Mittel |
| Entry 3 (nach FVG) | Unter FVG oder Sweep | Mittel |
| Entry 4 (bei EQ) | Unter EQ oder Sweep | Kleiner |

### Trade Recap des Tages

- Konkretes Beispiel eines Trades mit Stop-Platzierung
- Stop unter dem Sweep, nicht unter dem Entry-Level
- Ergebnis: Trade lief, Stop nicht getriggert

---

## Zusammenhang

Stop Loss und Take Profit (Tag 37) sind die zwei Hälften des Trade-Managements. Zusammen mit Lot-Size (Tag 39) ergibt sich das vollständige Risikomanagement. Wer alle drei kennt, kann R:R, Kapitalrisiko und Position-Management präzise berechnen.

---

## Goldene Regeln

- Stop immer außerhalb des Sweep-Levels
- Immer Spread-Buffer addieren
- Stop nie manuell verschlechtert (weiter weg vom Entry) nach Einstieg

---

## Aufgaben

### Aus dem Video
- Für aktuelles Setup: Stop unter Sweep mit Buffer berechnen

### Von Claude erstellt
1. Berechne für 3 verschiedene Setups (S&P, Gold, GBP/USD): Stop-Level unter dem Sweep + 7 Pips Buffer. Wie viele Pips ist der Stop jeweils?
2. Vergleiche: Stop unter Sweep vs. Stop unter OB – was ist der Unterschied in Pips? Was ändert das für das R:R?
3. Backteste: Wenn du in den letzten 10 Setups immer Stop unter Sweep gesetzt hättest – wie oft wäre der Stop ausgelöst worden? Vergleiche mit Stop unter OB.

---

## Was könnte noch fehlen

- Dynamic Stop: Stop verschieben wenn Kurs läuft (Trailing)
- Stop auf Break-Even (bereits in Tag 37 erklärt)

---

## Fazit

- **Wichtigste Erkenntnis:** Stop außerhalb des Sweeps mit Buffer = logische Invalidierungszone, keine willkürliche Zahl
- **Risikobewertung:** Stop zu eng = wird durch normales Rauschen ausgelöst; Stop zu weit = schlechtes R:R
- **Empfehlung:** Stop immer unter Sweep mit Buffer, nie näher – auch wenn R:R dann nicht traumhaft ist

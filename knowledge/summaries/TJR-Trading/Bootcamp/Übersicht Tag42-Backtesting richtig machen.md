# Übersicht Tag 42 – Backtesting richtig machen

**Erstelldatum:** 2026-06-13
**Quelldatei:** Tag42-Wie man richtig Backtest macht
**Typ:** Technik-Tag

---

## Überblick

Tag 42 beantwortet die häufige Frage nach Backtesting. Bar Replay wird als suboptimal eingestuft und eine bessere Alternative vorgeschlagen: Chart manuell zurückscrollen und Top-Down analysieren. Die beste Methode bleibt Demo-Trading wegen der echten Emotionen.

---

## Teilgebiete

### Bar Replay: Warum nicht ideal

- Auf 15m Chart + Wechsel zu Daily → zeigt vollständige Tageskerze statt aktuellen Stand
- Zeitkontext geht verloren → Daily Bias kann nicht korrekt aufgebaut werden
- Ohne korrekten Daily Bias fehlt der wichtigste Filter der Strategie

### Bessere Alternative: Chart zurückscrollen

1. Chart auf einem zufälligen historischen Datum öffnen
2. Von diesem Punkt aus Top-Down-Analyse wie im echten Trading
3. Alle Zeitrahmen sind korrekt vorhanden
4. Setup identifizieren, Entry / Stop / TP markieren
5. Dann weiter scrollen und prüfen ob Setup aufgegangen wäre

**Vorteile:**
- Alle Zeitrahmen korrekt
- Daily Bias kann normal aufgebaut werden
- Mehrere TF gleichzeitig nutzbar

### Beste Methode: Demo-Trading

- Echte Emotionen entstehen auch auf Demo (Kerzen die sich bewegen, Unsicherheit)
- In Bar Replay gibt es keine Emotionen – zu vorhersehbar
- Emotionsmanagement ist ein riesiger Teil des Tradings → Demo ist echter als Replay

### Praktische Hausaufgabe

- Vergangene Woche auf dem Chart: 1–2 Setups pro Tag identifizieren
- Alle Bausteine markieren: Sweep, BoS, Entry-Zone, Stop, TP
- Trainiert das Auge bis Muster-Erkennung automatisch läuft

### Der einzige verbleibende Engpass

- Wenn Bausteine erkannt werden können: Einzige Restaufgabe ist das richtige Mindset
- Psychologie, Disziplin, Emotionskontrolle
- Genau das wurden in den Psychologie-Videos (Tag 3, 5, 15, 17, etc.) behandelt

---

## Zusammenhang

Backtesting ergänzt das Live-Demo-Trading. Beides zusammen beschleunigt das Lernen. Wer täglich 1h zurückscrollt und 1h auf Demo tradet, macht in 3 Monaten den Fortschritt von 12 Monaten.

---

## Goldene Regeln

- Bar Replay ist akzeptabel aber nicht optimal für diese Strategie
- Chart zurückscrollen + Top-Down = besseres Backtesting
- Demo-Trading bleibt die beste Trainingsform

---

## Aufgaben

### Aus dem Video
- Vergangene Woche auf Chart analysieren: 1-2 Setups pro Tag mit allen Bausteinen markieren

### Von Claude erstellt
1. Backteste 3 Wochen zurück auf GBP/USD 1H. Identifiziere für jeden Handelstag das beste Setup (wenn vorhanden). Wie viele Setups pro Woche gab es?
2. Für die 10 besten Setups: Notiere Entry, Stop, TP1. Hat der Kurs TP1 immer erreicht? Was war die durchschnittliche R:R?
3. Finde 3 Setups wo ein Backtesting-Fehler möglich wäre (Hindsight Bias): Man sieht "offensichtlich" den Hochpunkt, aber in Echtzeit wäre der Entry unklar gewesen. Was macht den Unterschied?

---

## Was könnte noch fehlen

- Systematisches Backtesting-Journal (wie viele Setups, Trefferquote, R:R)
- Wie viele historische Setups braucht man für statistisch signifikante Ergebnisse?

---

## Fazit

- **Wichtigste Erkenntnis:** Chart zurückscrollen + Top-Down ist die effektivste Backtesting-Methode für diese Strategie
- **Risikobewertung:** Wer nur Bar Replay nutzt, hat einen verzerrten Daily Bias → unzuverlässige Backtesting-Ergebnisse
- **Empfehlung:** Jeden Abend 20-30 Minuten Chart der vergangenen Woche analysieren und Setups markieren

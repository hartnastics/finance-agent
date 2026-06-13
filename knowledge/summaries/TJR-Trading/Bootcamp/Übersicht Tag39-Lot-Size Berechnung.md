# Übersicht Tag 39 – Lot-Size Berechnung

**Erstelldatum:** 2026-06-13
**Quelldatei:** Tag39-Lot-Size
**Typ:** Technik-Tag

---

## Überblick

Tag 39 erklärt die drei Methoden zur Lot-Size-Berechnung und empfiehlt die kalkulierte Methode mit dem Stinu-App-Tool. Drei Konfidenz-Level (D-Risk, Normal, Confident) definieren wie viel man bei verschiedenen Setup-Qualitäten riskiert. Die Full-Portfolio-Methode wird explizit verboten.

---

## Teilgebiete

### Die 3 Lot-Size-Methoden

| Methode | Beschreibung | Empfehlung |
|---------|-------------|-----------|
| Fixe Lot-Size | Immer gleiche Lot-Size | Für Demo-Anfänger ok |
| Kalkulierte Lot-Size | Berechnet nach % Risiko und Stop-Größe | Empfohlen für Live |
| Full-Portfolio | Alles rein | Niemals |

### Die kalkulierte Methode: So funktioniert es

1. Kontostand eingeben (z.B. $10.000)
2. Risiko in % wählen (z.B. 1% = $100 maximal verlieren)
3. Stop-Loss in Pips eingeben (aus Trade-Analyse)
4. Tool berechnet: Wie viele Lots für genau $100 Risiko bei diesem Stop?
5. Diese Lot-Size wird verwendet → exaktes Risiko-Management

### Tool: Stinu App (oder myfxbook Position Size Calculator)

- Stinu: Kostenlose App für Lot-Size-Berechnung
- Eingaben: Kontostand, Risikoanteil %, Stop-Pips, Broker-Kontrakt-Größe
- Ausgabe: Exakte Lot-Size
- Broker-Kontrakt-Größe beachten (je nach Instrument unterschiedlich!)

### Die 3 Konfidenz-Level

| Level | Risiko | Wann |
|-------|--------|------|
| D-Risk | 50% des Tagesrisikos | Unsicheres Setup, gegen Trend |
| Normal | 100% des Tagesrisikos | Standard-Setup, alle Confluences |
| Confident | 200% des Tagesrisikos | Perfektes Setup, maximale Confluence |

**Beispiel:** Tagesrisiko 1% bei $10.000 = $100
- D-Risk: $50 riskieren
- Normal: $100 riskieren
- Confident: $200 riskieren (max 2% Ausnahme)

### Broker-Kontrakt-Größe beachten

- Standard-Lot bei Forex: 100.000 Einheiten
- Gold, S&P: andere Kontrakt-Größen
- Stinu berechnet automatisch wenn Kontrakt-Größe eingegeben wird

---

## Zusammenhang

Lot-Size ist die letzte Variable des Risikomanagement-Dreiecks (Stop Loss → Take Profit → Lot-Size). Mit diesen drei Komponenten kann man exakt berechnen: Was verliere ich maximal? Was gewinne ich? Wie viel Einheiten kaufe ich?

---

## Goldene Regeln

- Niemals Full-Portfolio
- Kalkulierte Methode immer (nie schätzen)
- Confident-Level nur bei wirklich perfekten Setups mit maximaler Confluence

---

## Aufgaben

### Aus dem Video
- Stinu App installieren und für ein Demo-Setup die Lot-Size berechnen

### Von Claude erstellt
1. Berechne für 3 verschiedene Setups die Lot-Size: $10.000 Konto, 1% Risiko, Stop-Größen 20 Pips / 40 Pips / 80 Pips. Wie verändert sich die Lot-Size?
2. Simuliere alle 3 Konfidenz-Level für ein Setup: D-Risk, Normal, Confident. Berechne jeweils den maximalen Verlust in $ und %.
3. Identifiziere dein letztes Trade-Setup. War es D-Risk, Normal oder Confident? Hättest du das auch so eingestuft? Was waren die Kriterien?

---

## Was könnte noch fehlen

- Lot-Size-Anpassung bei Teilschließungen (nach TP1)
- Compound-Effekt: Lot-Size mit wachsendem Konto automatisch anpassen

---

## Fazit

- **Wichtigste Erkenntnis:** Kalkulierte Lot-Size + 3 Konfidenz-Level = exaktes, flexibles Risikomanagement ohne Überriskieren
- **Risikobewertung:** Wer Lot-Size schätzt, riskiert entweder zu viel (D-Risk-Setups mit Confident-Level) oder zu wenig (beste Setups unterriskiert)
- **Empfehlung:** Stinu App sofort installieren und vor jedem Trade die Lot-Size berechnen – nie schätzen

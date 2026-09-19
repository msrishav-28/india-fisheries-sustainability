# Methodology

Adapted from the analytical framing used by Zamborain-Mason and colleagues for multispecies coral-reef fisheries, translated to India's coastal continental-shelf and small-pelagic systems. We mirror KAUST's data-science-for-Red-Sea-fisheries workflow: **compile → harmonize → baseline analysis → sustainability indicators → communicate**.

## 1. Data model (target tidy schema)

| field | type | example |
|---|---|---|
| `year` / `month` | int | 2024, 11 |
| `state` / `coast` | str | Kerala / west |
| `species_group` | str | oil sardine, mackerel, elasmobranchs |
| `gear` | str | trawl, purse seine, gillnet |
| `landings_t` | float | 45230.5 |
| `effort_boat_hours` | float | optional; CMFRI effort data where available |
| `source` | str | cmfri_landings_2024 |
| `provenance` | str | URL + table ref + retrieval date |

Key harmonization decisions: standardize species-group names against CMFRI groupings; collapse UTs (Puducherry→Tamil Nadu coast where CMFRI does); track gear-class synonyms; record unit conversions explicitly.

## 2. Baseline analyses

1. National & statewise landings trends (2015–2024 series from annual reports; 2000–2010 data.gov.in series for longer context).
2. Seasonality from monthly PFZ/landings overlays.
3. Composition shifts: pelagic/demersal/elasmobranch ratios by year.
4. Mechanization intensity: mechanized vs motorized vs non-motorized share (data.gov.in fleet tables).
5. Simple fisheries-econ context from CMFRI valuation figures (first-sale value trends).

## 3. Sustainability indicators

1. **Stock-status synthesis** — digitize CMFRI 2022 assessment (135 stocks / 70 species). Produce country-level stats: % stocks sustainable vs overfished by coast; publish as a figure + CSV.
2. **Effort-adjustment** — where effort data exists, compute CPUE proxies (tonnes per standardized fishing day); trend consistent with/clashing with landings trends is itself a finding.
3. **GFW effort-vs-landings mismatch** — total AIS apparent fishing hours/year in Indian EEZ (4Wings API, summed over EEZ) regressed against CMFRI annual landings: identifies under-monitored pressure years.
4. **Dark-vessel risk proxy** — GFW SAR vessel-presence vs AIS-tracked density per grid cell; rank coastal zones by mismatch; validate qualitatively against darkships.in outputs.
5. **Environmental covariates** — INCOIS PFZ intensity (count of PFZ advisories per sub-zone per month) as a proxy for fishable-days, to contextualize effort.

## 4. Communication

- Streamlit dashboard: national overview tab, state deep-dive tab, stock-status tab, GFW map tab.
- Figure pipeline: matplotlib/seaborn, geopandas for coastal maps; export 300-dpi PNG + interactive Plotly.
- Write-up: 4–6 page technical report (Markdown → PDF) framing findings vs KAUST Red Sea baseline; aim for a preprint (e.g., SSRN or arXiv q-bio/stat.AP cross-list) once Phase 4 lands.

## 5. Ethics & limitations

- CMFRI data is research-grade but sample-based; document confidence caveats in every figure footnote.
- AIS effort under-detects India's huge non-motorized/artisanal fleet — explicitly frame GFW layers as *indicative of industrial/mechanized pressure*, not total effort.
- No personal fisher data; aggregate only.
- Cite every external dataset + tool (FAIR principles) in `DATA_INVENTORY.md`.

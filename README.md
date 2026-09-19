# India Marine Fisheries Sustainability Data Platform

**Data science for sustainable Indian marine fisheries and aquatic food systems.**
An open, reproducible effort to compile, harmonize, analyze, and visualize India's marine fisheries data — built to mirror the methodology of KAUST's Red Sea fisheries data-science project and contribute a baseline sustainability assessment for India's marine capture sector.

---

## Why this project

- India is the **3rd largest fish-producing nation**; marine capture landings were an estimated **3.45 million tonnes in 2024** (down ~2% from 3.53 Mt in 2023), yet public, harmonized, analysis-ready datasets are fragmented across PDFs and portals (ICAR-CMFRI, *Marine Fish Landings in India — 2024*).
- ICAR-CMFRI's **Stock Status Assessment 2022** evaluated **135 stocks across 70 species** — an under-digitized goldmine for sustainability indicator work (*Indian Journal of Fisheries*, ICAR-CMFRI eprints 18242).
- Satellite-derived vessel analytics (Global Fishing Watch APIs, added SAR dark-vessel layers) have **not been systematically fused with Indian landings data in open code** — that fusion is the novel contribution here.
- INCOIS already operationalizes daily **Potential Fishing Zone (PFZ)** advisories from SST/chlorophyll remote sensing — providing environmental covariates for effort and yield modeling.

## Objectives

1. **Compile** marine fish landings, effort, gear, and stock-status data across ICAR-CMFRI publications, data.gov.in, FAOSTAT/FishStat, and INCOIS.
2. **Harmonize** everything into tidy, analysis-ready tables (parquet/CSV) with consistent units, names, spatial keys, and timestamps.
3. **Analyze** trends and compute sustainability indicators: landings trends by state/species group, catch-per-unit-effort proxies, effort-vs-landings mismatch (GFW), and published stock-status synthesis.
4. **Communicate** results via an interactive dashboard and visualizations — including a GFW-based fishing-effort map and dark-vessel risk layer for India's EEZ.
5. **Package** the work as reproducible notebooks + a short technical write-up suitable for research-internship applications.

## Data sources

Full catalog in [`DATA_INVENTORY.md`](./DATA_INVENTORY.md). Highlights:

| Source | What it gives us |
|---|---|
| ICAR-CMFRI eprints (@eprints.cmfri.org.in) | Annual landings (PDF), Stock Assessment 2022, 70+ years of catch-effort survey data |
| data.gov.in | Fish catch & landings by species group (2000–2010 and beyond), mechanized/motorized craft fleet stats |
| FAOSTAT / FishStat | Global capture production (1950–present) for India benchmarking |
| Global Fishing Watch APIs | AIS fishing effort (2012–present), vessel identity, SAR dark-vessel detections — official Python SDK |
| INCOIS | PFZ advisories, ocean-state forecasts, historical SST/chl-a products |

## Roadmap

- **Phase 0 — Scaffold (this commit).** Repo structure, dataset inventory, methodology, starter code.
- **Phase 1 — Compilation.** Download & parse CMFRI annual landings PDFs (2015–2024), data.gov.in CSVs, FAOSTAT series. Hand-digitize where needed; log provenance.
- **Phase 2 — Harmonization.** Tidy schema: `year, month?, state, coast, species_group, gear, landings_t, effort_boat_hours?, source, provenance`.
- **Phase 3 — Baseline EDA.** National and statewise trends, seasonality, species-group composition shifts, mechanization intensity.
- **Phase 4 — Sustainability layer.** Cross-reference CMFRI Stock Status 2022 categories; join GFW EEZ effort via 4Wings API; draft dark-vessel risk proxy from GFW SAR products vs. darkships.in precedent.
- **Phase 5 — Communication.** Streamlit dashboard, key-figures notebook, README graphics archive, short write-up.

## Repository structure

```
├── README.md
├── DATA_INVENTORY.md      # every source, with URLs and access notes
├── METHODOLOGY.md         # analytical framework, adapted from Zamborain-Mason et al.
├── src/
│   ├── harvest_sources.py # downloaders + provenance log
│   └── eda_landings.py    # bootstrap EDA on landings totals
├── notebooks/             # analysis notebooks (Phase 1+)
├── data/                  # raw/processed data (gitignored)
├── figures/               # publication-quality figures
├── requirements.txt
└── .gitignore
```

## Reproducing

```bash
pip install -r requirements.txt
cp .env.example .env   # optional: add GFW_API_TOKEN for Global Fishing Watch
python src/harvest_sources.py
python src/eda_landings.py
```

## Acknowledgements & inspirations

- Jessica Zamborain-Mason & collaborators — sustainability frameworks for multispecies reef fisheries; KAUST VSRP project listing *“Harnessing data-science to enhance the sustainability of Red Sea fisheries”* as the methodological template.
- ICAR-CMFRI, INCOIS, FAO, and Global Fishing Watch for open data.

License: MIT.

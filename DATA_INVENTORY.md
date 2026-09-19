# Data Inventory — India Marine Fisheries Sustainability Data Platform

Legend: ✅ open download · 🔑 API token (free) · 📄 PDF (needs parsing) · 💰 restricted/paid

## Primary fisheries statistics

| # | Source | Dataset | Coverage | Format / access | Notes |
|---|---|---|---|---|---|
| 1 | ICAR-CMFRI Digital Repository | **Marine Fish Landings in India — 2024** (eprints.cmfri.org.in/19094) | 2024 national & statewise landings, spp groups | 📄 PDF | Mainland 3.45 Mt; A&N 16,674 t. Anchor dataset. |
| 2 | ICAR-CMFRI | **Marine Fish Landings annual reports, 2015–2023** | Yearly | 📄 PDF | Same series, prior years — enables 10-yr trend |
| 3 | ICAR-CMFRI | **Stock Status Assessment of Indian Marine Fisheries 2022** (eprints/18242) | 135 stocks / 70 species | 📄 PDF / journal | Categories: sustainable / overfished / recovering etc. Digitize the summary table. |
| 4 | CMFRI FRAD / NMLRDC | National Marine Living Resources Data Centre | 1950–present catch-effort surveys | 💰/on-request | Stratified multistage sampling, ~1,200 landing centres. Request or use published aggregates. |
| 5 | data.gov.in | **Fish Catch and Landings By Group of Species** | 2000–2010 | ✅ CSV | Species-group long series: sardines, anchovies, tunas, elasmobranchs, etc. |
| 6 | data.gov.in | Fisheries sub-catalog (various) | Various | ✅ CSV | Fleet, landing centres, worker stats — check catalog periodically. |
| 7 | FAO – FAOSTAT / FishStat | **Global Capture Production** | 1950–present, species × area | ✅ API/CSV | India vs world benchmarking; FAO Data Explorer has friendly UI; `fishstat` R pkg mirrors it. |

## Satellite / effort / enforcement

| # | Source | Dataset | Coverage | Format / access | Notes |
|---|---|---|---|---|---|
| 8 | Global Fishing Watch | **4Wings API — `public-global-fishing-effort`** | Indian EEZ, 2012–present (96-h lag) | 🔑 REST + official Python SDK | Gridded apparent AIS fishing effort |
| 9 | Global Fishing Watch | **Vessel Events / Identity / Encounters APIs** | 2012–present | 🔑 REST | Port visits, encounters, identity cross-checks |
| 10 | Global Fishing Watch | **SAR dark-vessel / vessel-presence layers** | Indian EEZ | 🔑 4Wings datasets | Proxy for IUU risk; cf. darkships.in (India-first SAR dark-ship monitoring) |
| 11 | INCOIS | **PFZ advisories + Ocean State Forecast archive** | Daily, Indian EEZ sub-zones | ✅ web + text data endpoints | SST & chl-a covariates for effort/biology models |
| 12 | xView3 / DIUx (SAR maritime CV benchmark) | xView3-SAR dataset | Global AOIs including Indian Ocean | ✅ with registration | Optional CV side-quest: dark-vessel detection model benchmarking |

## Priority order

**Phase 1 anchors:** #1, #5 → **Phase 1.5:** #2, #7 → **Phase 4:** #3, #8 → **Phase 4.5:** #10, #11.

## Provenance policy

- Every row in `data/processed/` carries `source` and `provenance` fields (URL + retrieval date + page/table ref for PDFs).
- Raw files stay in `data/raw/` (gitignored); parsers live in `src/`; never edit raw files.
- For hand-digitized tables, create `data/digitized/<source>_<table>.csv` with `digitized_by`, `digitized_date`, `verification_notes` columns.

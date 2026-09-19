# Phase 1 Work Board — Data Compilation

Owner: @msrishav-28 (field ops + local runs) · Co-researcher: @perplexity (architecture, code, review)

## Tasks

### T1 — Download & inspect CMFRI anchor PDFs
- **Do:** Run `python src/harvest_sources.py`. Confirm both PDFs land in `data/raw/` and provenance rows are logged in `data/raw/_provenance.csv`.
- **Acceptance:** Both PDFs open, page count noted; `_provenance.csv` has 2 rows with status `downloaded`.
- **Deliverable:** `data/raw/` contents + screenshot/log in first EDA notebook.

### T2 — Parse CMFRI Landings 2024 tables
- **Do:** Build `src/parse_cmfri_2024.py` using `tabula-py` or `camelot` (add deps to requirements). Extract: (a) national totals, (b) statewise landings table, (c) species-group table, (d) month-of-landing if present.
- **Acceptance:** `data/processed/cmfri_2024_statewise.csv` and `data/processed/cmfri_2024_species_group.csv` match PDF numbers within rounding error; each row has `source` + `provenance` fields.
- **Deliverable:** Parser + CSVs + a `notebooks/01_landings_2024_eda.ipynb` rendering first charts.

### T3 — Digitize CMFRI Stock Status 2022 summary table
- **Do:** Hand-transcribe the status counts (sustainable / overfished / recovering / etc., by coast if given) from eprints/18242 into `data/digitized/cmfri_stockstatus_2022_summary.csv` with `digitized_by`, `digitized_date`, `verification_notes`.
- **Acceptance:** Row count sums to 135; second-pass spot check of ≥10% of rows against the PDF.
- **Deliverable:** CSV + `figures/stock_status_2022_overview.png` (stacked bar by coast).

### T4 — Pull FAOSTAT India capture-production series
- **Do:** Run `python src/harvest_sources.py --faostat`. Write `src/parse_faostat.py` to extract India marine capture tonnes by species group, 1950–present.
- **Acceptance:** `data/processed/faostat_india_capture_long.csv` parsed; spot-check 2024 vs CMFRI (explain definitional differences in a note cell).
- **Deliverable:** CSV + long-run trend figure `figures/india_capture_1950_2024.png`.

### T5 — Register Global Fishing Watch API access
- **Do:** Create a free GFW account, generate an API token, set `GFW_API_TOKEN` in `.env`. Look up the India EEZ region ID from the regions endpoint and update the stub in `harvest_sources.py`.
- **Acceptance:** A successful 4Wings ping for one month (e.g., Jan 2023) of fishing-effort in the Indian EEZ saved to `data/raw/gfw_4wings/effort_2023-01_india_eez.json`.
- **Deliverable:** Token confirmed working + region ID recorded in `DATA_INVENTORY.md`.

### T6 — Extract data.gov.in historical series
- **Do:** Download the Fish Catch & Landings by Group of Species CSVs (2000–2010). Normalize to the tidy schema.
- **Acceptance:** `data/processed/datagov_catch_by_group_2000_2010.csv` passes a duplicate/NA audit.
- **Deliverable:** CSV + decade-trend chart.

## Rules of engagement
- One task = one branch (`task/T1-harvest` …) when we move to real code; docs edits may go straight to `main`.
- Commit habits: `data:` for datasets, `feat:` parsers, `docs:` write-ups, `fig:` figure refreshes.
- Every number in a notebook must trace to a CSV with `provenance`.
- Open questions go into a `DISCUSSIONS.md` thread rather than chat — keeps the repo self-documenting.

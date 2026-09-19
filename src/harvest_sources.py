"""harvest_sources.py — download & register raw datasets for the project.

Creates ./data/raw/<source>/ and appends to ./data/raw/_provenance.csv
so every downstream row is traceable to a URL + retrieval date + table ref.

Usage
-----
    python src/harvest_sources.py [--sources cmfri,data_gov,faostat] [--all]
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import os
import pathlib

import requests

ROOT = pathlib.Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
PROV = RAW / "_provenance.csv"

# ---------------------------------------------------------------------------
# Source registry — extend as we discover assets.
# Every entry: (source_key, filename, url, notes)
# ---------------------------------------------------------------------------
SOURCES = {
    "cmfri_landings_2024": {
        "files": [
            ("Marine_Fish_Landings_India_2024.pdf",
             "https://eprints.cmfri.org.in/19094/1/Marine%20Fish%20Landings%20in%20India%20-%202024.pdf",
             "Anchor dataset: 2024 national 3.45 Mt; A&N 16,674 t"),
        ],
        "why": "CMFRI annual landings report — primary"
    },
    "cmfri_stockstatus_2022": {
        "files": [
            ("CMFRI_StockStatus_2022_IJF.pdf",
             "http://eprints.cmfri.org.in/18242/1/Indian%20Journal%20of%20Fisheries_2024_A%20Gopalakrishnan.pdf",
             "135 stocks / 70 species; digitize status table"),
        ],
        "why": "CMFRI Stock Status Assessment 2022"
    },
}

# FAOSTAT bulk-ish endpoint for capture production (public)
FAOSTAT_CAPTURE_URL = (
    "https://fenixservices.fao.org/faostat/api/v1/"
    "CL_FI_CAPTURE_SOURCES/QCL"
)


def _prov_write(source: str, url: str, dest: pathlib.Path, status: str) -> None:
    RAW.mkdir(exist_ok=True, parents=True)
    write_header = not PROV.exists()
    with PROV.open("a", newline="") as f:
        w = csv.writer(f)
        if write_header:
            w.writerow(["source", "url", "local_path", "retrieved_utc", "status"])
        w.writerow([source, url, dest.relative_to(ROOT).as_posix(),
                    dt.datetime.utcnow().isoformat(timespec="seconds"), status])


def download_file(url: str, dest: pathlib.Path) -> str:
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists() and dest.stat().st_size > 0:
        return "cached"
    try:
        r = requests.get(url, timeout=60)
        r.raise_for_status()
        dest.write_bytes(r.content)
        return f"downloaded ({dest.stat().st_size/1e6:.1f} MB)"
    except Exception as e:  # noqa: BLE001
        return f"FAILED: {e}"


def harvest(source_keys: list[str]) -> None:
    for key in source_keys:
        meta = SOURCES[key]
        outdir = RAW / key
        print(f"\n=== {key} — {meta['why']} ===")
        for fname, url, notes in meta["files"]:
            dest = outdir / fname
            status = download_file(url, dest)
            print(f"  {fname}: {status}  [{notes}]")
            _prov_write(key, url, dest, status)


def fetch_faostat_india_capture() -> None:
    """Pull India capture-production rows from FAOSTAT API (demo pull)."""
    outdir = RAW / "faostat_capture"
    outdir.mkdir(parents=True, exist_ok=True)
    dest = outdir / "india_capture_production.json"
    params = {"area": "356"}  # FAOSTAT area code for India
    try:
        r = requests.get(FAOSTAT_CAPTURE_URL, params=params, timeout=90)
        r.raise_for_status()
        dest.write_text(r.text)
        status = f"downloaded ({dest.stat().st_size/1e6:.1f} MB)"
    except Exception as e:  # noqa: BLE001
        status = f"FAILED: {e}"
    print(f"faostat_capture -> {status}")
    _prov_write("faostat_capture", FAOSTAT_CAPTURE_URL, dest, status)


GFW_STUB = '''
# ---- Global Fishing Watch 4Wings API (free key; register at GFW portal) ----
# import os, requests
# GFW = "https://gateway.api.globalfishingwatch.org/v3/4wings/report"
# headers = {"Authorization": f"Bearer {os.environ['GFW_API_TOKEN']}"}
# payload = {
#   "spatial-aggregation": True,
#   "datasets": ["public-global-fishing-effort:latest"],
#   "date-range": "2023-01-01,2023-12-31",
#   "region": {"dataset": "public-eez-areas", "id": "8469"},  # India EEZ id — confirm from regions endpoint
# }
# r = requests.post(GFW, json=payload, headers=headers, timeout=120)
'''


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--sources", default=",".join(SOURCES),
                    help="comma-separated source keys")
    ap.add_argument("--faostat", action="store_true",
                    help="also pull FAOSTAT India capture data")
    args = ap.parse_args()
    harvest([s.strip() for s in args.sources.split(",") if s.strip()])
    if args.faostat:
        fetch_faostat_india_capture()
    print("\nGFW 4Wings stub:", GFW_STUB)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Run the data cleaning pipeline.
Usage:
    python scripts/data_processing.py
"""
from pathlib import Path
import pandas as pd

RAW = Path('data/raw'); PRO = Path('data/processed'); PRO.mkdir(parents=True, exist_ok=True)

def to_snake(s): return s.strip().lower().replace(' ','_').replace('-','_')

def clean_csv(src_name:str, out_name:str):
    fp = RAW/src_name
    if not fp.exists():
        print(f'[WARN] Missing {fp}'); return
    df = pd.read_csv(fp)
    df.columns = [to_snake(c) for c in df.columns]
    if 'bbl' in df.columns: df['bbl'] = df['bbl'].astype(str)
    out = PRO/out_name
    df.to_csv(out, index=False)
    print('Wrote', out)

if __name__ == '__main__':
    clean_csv('pluto_2024.csv', 'pluto_clean.csv')
    clean_csv('vacant_storefronts.csv', 'vacant_clean.csv')
    clean_csv('business_registry.csv', 'business_clean.csv')
    clean_csv('mta_ridership.csv', 'mta_clean.csv')

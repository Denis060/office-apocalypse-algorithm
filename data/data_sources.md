# Data Sources & Lineage

Record every dataset used in this project. Keep raw files in `data/raw/` and write cleaned outputs to `data/processed/`.

| Dataset Name | File(s) in `data/raw/` | Source / URL | Date Downloaded | License/Terms | Description | Join Keys / Notes |
|---|---|---|---|---|---|---|
| PLUTO / MapPLUTO | `pluto_2024.csv` | NYC DCP | YYYY-MM-DD | Open (NYC) | Parcel/building attributes (BBL, landuse, sqft, year built) | Join on **BBL**. CRS EPSG:2263/4326. |
| Vacant Storefronts | `vacant_storefronts.csv` | NYC Open Data | YYYY-MM-DD | Open (NYC) | Ground-floor vacancies by location/type | Spatial join to parcels/tracts. |
| Business Registry | `business_registry.csv` | NYC Open Data | YYYY-MM-DD | Open (NYC) | Licensed businesses (type, status) | Buffer counts around office parcels. |
| MTA Ridership | `mta_ridership.csv` | MTA | YYYY-MM-DD | Open (MTA) | Station entries/exits; deltas vs 2019 | Map to nearest stations, rolling windows. |
| Comptroller Profiles | `neighborhood_profiles.csv` | NYC Comptroller | YYYY-MM-DD | Open (NYC) | Neighborhood economic indicators | Aggregate to tract/CD. |
| (Optional) WiredNYC | `wirednyc.csv` | WiredScore | YYYY-MM-DD | Restricted | Building infra/connectivity scores | Fuzzy join via address/BBL. |
| (Optional) Market Reports | `submarket_vacancy.xlsx` | Moody's/Cushman/M&M | YYYY-MM-DD | Restricted | Submarket vacancy trends | Validation context only. |

**Rules**
- Do **not** commit `data/raw/` and `data/processed/` (see `.gitignore`).
- Log all transformations in notebooks/scripts and note them here.

# BlackoutWatch

Predicting power outages in Texas before they happen using ML.

## Setup

```bash
pip install -r requirements.txt
```

## Pipeline

Run scripts in order:

```bash
python scripts/01_download_data.py      # Download EAGLE-I from Figshare
python scripts/02_preprocess.py         # Filter Texas, merge with weather, build features
python scripts/03_feature_engineering.py # Create ML-ready feature matrix
python scripts/04_classification.py     # Outage yes/no prediction
python scripts/05_regression.py         # Severity & duration prediction
python scripts/06_clustering.py         # County risk profiles
python scripts/07_bootstrap_comparison.py # CIs and model comparison
streamlit run dashboard/app.py          # Launch live dashboard
```

## Data Sources

- **EAGLE-I** (ORNL/DOE): County-level outage data, 15-min intervals, 2014-2022
- **GHCN-Daily** (NOAA): Historical daily weather observations for Texas stations
- **Storm Events** (NOAA): Severe weather events by county

## Project Structure

```
blackoutwatch/
├── data/
│   ├── raw/              # Original downloaded files
│   ├── processed/        # Cleaned, merged datasets
│   └── models/           # Saved trained models
├── scripts/              # Pipeline scripts (run in order)
├── dashboard/            # Streamlit app
├── notebooks/            # Final results presentation
└── reports/figures/      # Exported plots
```

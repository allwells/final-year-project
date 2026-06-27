# Server

Flask backend for the Respiratory Disease Prediction System.

## Prerequisites

- Python 3.8+
- pip

## Setup

**1. Create and activate a virtual environment**

```bash
python -m venv env
source env/bin/activate
```

**2. Install dependencies**

```bash
pip install -r requirements.txt
```

**3. Make the run script executable** (first time only)

```bash
chmod +x run.sh
```

## Running the Development Server

```bash
./run.sh
```

This starts the Flask development server. The app will be available at `http://127.0.0.1:5000`.

The environment is configured via `.flaskenv`:
- `FLASK_APP=app`
- `FLASK_ENV=development`

## Rebuilding ML Models

Pre-trained models are already serialized in `app/utils/models/`. If you need to retrain them (e.g., after updating a dataset), run the builder scripts from inside the `app/utils/builders/` directory:

```bash
cd app/utils/builders
python lung_cancer_model_builder.py
python covid19_model_builder.py
```

This reads the CSVs from `app/utils/data/`, trains all four classifiers, and writes new `.pkl` files to `app/utils/models/`.

## Production Deployment

The app is Heroku-compatible. A `Procfile` is included that runs the app with Gunicorn:

```
web: gunicorn run:app
```

Use `deploy.sh` or push to a Heroku-connected remote to deploy.

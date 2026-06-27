# Respiratory Disease Prediction System

A web application that predicts risk for respiratory diseases using multiple machine learning classifiers. Users submit symptom and demographic data through a form, and the system runs the input through four trained ML models simultaneously, presenting each model's verdict in a side-by-side comparison table.

## Supported Predictions

- **COVID-19** — based on 20 symptom and exposure indicators (fever, dry cough, travel history, contact with infected individuals, mask-wearing habits, etc.)
- **Lung Cancer** — based on 15 inputs (age, gender, smoking, chest pain, alcohol consumption, anxiety, etc.)

## How It Works

For each disease, four classifiers are trained on labelled CSV datasets and serialized to `.pkl` files. At prediction time, the Flask server loads the pre-trained models, normalizes the input using a pre-fitted MinMaxScaler, and returns each model's binary verdict ("At risk" / "Not at risk").

**Classifiers used:**
- Logistic Regression
- Naive Bayes (Gaussian)
- K-Nearest Neighbors
- Decision Tree

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Flask 2.1, Gunicorn |
| ML | scikit-learn, NumPy, Pandas |
| Model persistence | joblib |
| Templating | Jinja2 |
| Styling | Tailwind CSS |
| Deployment | Procfile (Heroku-compatible) |

## Project Structure

```
.
├── notebooks/               # Jupyter notebooks for EDA and model training
│   ├── covid_19.ipynb
│   ├── lung_cancer.ipynb
│   └── heart_disease.ipynb
└── server/                  # Flask application
    ├── app/
    │   ├── lib/             # Prediction logic (runs all 4 classifiers)
    │   ├── templates/       # Jinja2 HTML templates
    │   ├── static/          # CSS, fonts, images
    │   └── utils/
    │       ├── builders/    # Scripts to train and serialize models
    │       ├── data/        # Training datasets (CSV)
    │       ├── models/      # Serialized .pkl model files
    │       └── providers/   # Model loading helpers
    └── requirements.txt
```

## Getting Started

See [server/README.md](./server/README.md) for setup and development instructions.

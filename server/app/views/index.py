from flask import Blueprint, render_template, request
from app.lib.covid19_prediction import covid19_process
from app.lib.lung_cancer_prediction import lung_cancer_process

index = Blueprint("index", __name__, url_prefix="/")


@index.route("/")
@index.route("/index")
def home():
    return render_template("index.html")


@index.route("/covid-19-prediction")
def covid_19():
    return render_template("covid-19.html")


@index.route("/lung-cancer-prediction")
def lung_cancer():
    return render_template("lung-cancer.html")


# Define the prediction route for covid-19
@index.route("/predict-covid-19", methods=["POST"])
def predict_covid_19():
    if request.method == "POST":
        breathing_problem = request.form["BreathingProblem"]
        fever = request.form["Fever"]
        dry_cough = request.form["DryCough"]
        sore_throat = request.form["SoreThroat"]
        running_nose = request.form["RunningNose"]
        asthma = request.form["Asthma"]
        chronic_lung_disease = request.form["ChronicLungDisease"]
        headache = request.form["Headache"]
        heart_disease = request.form["HeartDisease"]
        diabetes = request.form["Diabetes"]
        hyper_tension = request.form["HyperTension"]
        fatigue = request.form["Fatigue"]
        gastrointestinal = request.form["Gastrointestinal"]
        travel_abroad = request.form["TravelAbroad"]
        contact_with_covid_patient = request.form["ContactWithCOVIDPatient"]
        attended_large_gatherings = request.form["AttendedLargeGatherings"]
        visited_exposed_public_places = request.form["VisitedExposedPublicPlaces"]
        family_working_in_exposed_public_places = request.form[
            "FamilyWorkingInExposedPublicPlaces"
        ]
        wearing_masks = request.form["WearingMasks"]
        sanitization_from_market = request.form["SanitizationFromMarket"]

        user_input = [
            int(breathing_problem),
            int(fever),
            int(dry_cough),
            int(sore_throat),
            int(running_nose),
            int(asthma),
            int(chronic_lung_disease),
            int(headache),
            int(heart_disease),
            int(diabetes),
            int(hyper_tension),
            int(fatigue),
            int(gastrointestinal),
            int(travel_abroad),
            int(contact_with_covid_patient),
            int(attended_large_gatherings),
            int(visited_exposed_public_places),
            int(family_working_in_exposed_public_places),
            int(wearing_masks),
            int(sanitization_from_market),
        ]

        results = covid19_process(user_input)

        return render_template("result.html", results=results)
    else:
        return render_template("index.html")


# Define the prediction route for lung cancer
@index.route("/predict-lung-cancer", methods=["POST"])
def predict_lung_cancer():
    if request.method == "POST":
        gender = request.form["Gender"]
        age = request.form["Age"]
        smoking = request.form["Smoking"]
        yellow_fingers = request.form["YellowFingers"]
        anxiety = request.form["Anxiety"]
        peer_pressure = request.form["PeerPressure"]
        chronic_disease = request.form["ChronicDisease"]
        fatigue = request.form["Fatigue"]
        allergy = request.form["Allergy"]
        wheezing = request.form["Wheezing"]
        alcohol_consuming = request.form["AlcoholConsuming"]
        coughing = request.form["Coughing"]
        breath_shortage = request.form["BreathShortage"]
        swallowing_difficulty = request.form["SwallowingDifficulty"]
        chest_pain = request.form["ChestPain"]

        user_input = [
            int(gender),
            int(age),
            int(smoking),
            int(yellow_fingers),
            int(anxiety),
            int(peer_pressure),
            int(chronic_disease),
            int(fatigue),
            int(allergy),
            int(wheezing),
            int(alcohol_consuming),
            int(coughing),
            int(breath_shortage),
            int(swallowing_difficulty),
            int(chest_pain),
        ]

        results = lung_cancer_process(user_input)

        return render_template("result.html", results=results)
    else:
        return render_template("index.html")


@index.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

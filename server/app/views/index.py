from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///dev.db"
db = SQLAlchemy(app)


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/covid-19-prediction")
def covid_19():
    return render_template("covid-19.html")


@app.route("/copd-prediction")
def copd():
    return render_template("copd.html")


@app.route("/pneumonia-prediction")
def pneumonia():
    return render_template("pneumonia.html")


@app.route("/tuberculosis-prediction")
def tuberculosis():
    return render_template("tuberculosis.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)


# from flask import Blueprint, render_template, request, session, flash, redirect, url_for
# from app.lib.prediction import process
# from app.expertsystem import get_inference

# index = Blueprint("index", __name__, url_prefix="/")

# @index.route("/")
# def home():
#     return render_template('index.html')


# @index.route("/notebook")
# def notebook():
#     return render_template('heart_disease.html')


# @index.route("/predict", methods=['POST'])
# def predict():
#     if request.method == 'POST':
#         age = request.form['Age']
#         sex = request.form['Sex']
#         chestpaintype = request.form['ChestPainType']
#         restingbp = request.form['RestingBP']
#         cholesterol = request.form['Cholesterol']
#         fastingbs = request.form['FastingBS']
#         restecg = request.form['RestingECG']
#         maxhr = request.form['MaxHR']
#         exerciseangina = request.form['ExerciseAngina']
#         oldpeak = request.form['Oldpeak']
#         st_slope = request.form['ST_Slope']

#         session["user"] = request.form["name"]

#         if age == "" or restingbp == "" or cholesterol == "" or maxhr == "" or oldpeak == "":
#             flash(
#                 "Age, Trestbps, Chol, Thalach, Oldpeak, and CA are required", category="error")
#             return redirect(url_for('home'))

#         user_input =[int(age), sex, chestpaintype, int(restingbp), int(cholesterol), int(fastingbs), restecg, int(maxhr), exerciseangina, float(oldpeak), st_slope]

#         results = process(user_input)
#         inference = get_inference(restingbp=int(restingbp), fbs=bool(int(fastingbs)), cholesterol=int(cholesterol))
#         return render_template('result.html', results=results, inference=inference)
#     else:
#         return render_template('index.html')

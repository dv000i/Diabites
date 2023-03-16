from flask import Flask, request
import pickle
import flasgger
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

with open("diabites.pickle", 'rb') as f:
    classifier = pickle.load(f)


@app.route('/Predict', methods=["GET"])
def Predict():
    """ Check Present of diabities
        This is using docstrings for specifications.
        ---
        parameters:
          - name: Pregnancies
            in: query
            type: number
            required: true
          - name: Glucose
            in: query
            type: number
            required: true
          - name: BloodPressure
            in: query
            type: number
            required: true
          - name: Age
            in: query
            type: number
            required: true

        responses:
            200:
                description: the output type is

        """

    pre = request.args.get('Pregnancies')
    glu = request.args.get('Glucose')
    bp = request.args.get('BloodPressure')
    age = request.args.get('Age')

    prediction = classifier.predict([[pre, glu, bp, age]])

    if prediction == 1:
        return "You have Diabities"
    else:
        return "You don't have Diabities but take precautions"


@app.route("/")
def welcomwe():
    return "welcome"


if __name__ == '__main__':
    app.run()

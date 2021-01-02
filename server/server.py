from flask import Flask, request, jsonify, render_template
# import util  #this for local
import server.util as util #this for deployment

# app = Flask(__name__) #local
app = Flask(__name__, static_url_path="/client", static_folder='../client', template_folder="../client")


@app.route('/', methods=['GET'])
def index():
    if request.method == "GET":
        return render_template("app.html")


@app.route('/get_property_name', methods=['GET'])
def get_property_name():
    response = jsonify({
        'property_type': util.get_property_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/predict_loan', methods=['POST'])
def predict_loan():
    gender = int(request.form['gender'])
    married = int(request.form['married'])
    dependents = request.form['dependents']
    education = int(request.form['education'])
    self_employed = int(request.form['self_employed'])
    applicant_income = int(request.form['applicant_income'])
    coapplicant_income = int(request.form['coapplicant_income'])
    loan_amount = int(request.form['loan_amount'])
    loan_amount_term = int(request.form['loan_amount_term'])
    credit_history = int(request.form['credit_history'])
    property_area = request.form['property_area']

    response = jsonify({
        'classified_result': util.predict_loan(gender, married, dependents, education, self_employed, applicant_income,
                                               coapplicant_income, loan_amount, loan_amount_term, credit_history,
                                               property_area)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == "__main__":
    print("Starting Python Flask Server for Home Price Prediction")
    # print(util.get_property_names())
    # print(util.predict_loan(0, 0, 0, 0, 0, 3748, 1668, 110, 360, 1, 'Semiurban'))
    app.run(debug=True)

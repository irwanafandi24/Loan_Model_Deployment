import json
import pickle
import os
import numpy as np

# define global variable
__property = None
__data_columns = None
__model = None


def predict_loan(gender, married, dependents, education, self_employed, applicant_income, coapplicant_income, loan_amount, loan_amount_term, creadit_history, property_area):
    try:
        property_data = __data_columns.index(property_area.lower())
    except:
        property_data = -1

    data = np.zeros(len(__data_columns))
    data[3] = gender
    data[4] = married
    data[5] = dependents
    data[6] = education
    data[7] = self_employed
    data[8] = applicant_income
    data[9] = coapplicant_income
    data[10] = loan_amount
    data[11] = loan_amount_term
    data[12] = creadit_history

    if property_data > 0:
        data[property_data] = 1

    result = __model.predict([data])
    if result == 1:
        return 'Loan Approved'

    return 'Loan Rejected'


def get_property_names():
    new_property = [x for x in __property]
    return new_property


def load_saved_artifacts():
    print("Start to load the artifact...")
    global __data_columns
    global __property
    global __model

    path = os.path.dirname(__file__)
    artifacts = os.path.join(path, "artifacts"),

    # with open('./artifacts/columns.json', 'r') as file: local
    with open(artifacts[0] + "/columns.json", "r") as file:
        __data_columns = json.load(file)['data_columns']
        __property = __data_columns[:3]

    # with open('./artifacts/loan_lr.pickle', 'rb') as file:
    with open(artifacts[0] + "/loan_lr.pickle", 'rb') as file:
        __model = pickle.load(file)
    print("Loading the artifatc is done ...")

load_saved_artifacts()

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_property_names())
    print(predict_loan(0, 0, 0, 0, 0, 3748, 1668, 110, 360, 1, 'Semiurban'))

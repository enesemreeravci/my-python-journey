# complete according to the assignment page!
# given symptoms, age and medical history
from os.path import split

from cupshelpers.debug import nonfatalException
from userpath.cli import append


class HealthDiagnosisSystem:
    def __init__(self):
        self.symptoms = []
        self.age = 0
        self.history = ""
        self.diseases = []
    # list_of_symptoms = ["headache", "sore throat", "rash", "fever", 'cough', 'vomiting']

    def get_user_input(self):
        raw_symptom = input("Enter your symptoms (comma-separated): ")
        list_of_symptoms = []
        list_of_symptoms = raw_symptom.split(",")
        cleaned_symptoms = []
        for i in list_of_symptoms:
            cleaned = i.strip().lower()
            if cleaned:
                cleaned_symptoms.append(cleaned)
        self.symptoms = cleaned_symptoms

        while True:
            user_age = input("Age:")
            if user_age.isnumeric():
                age_int = int(user_age)
                if age_int > 0:
                    self.age = age_int
                else:
                    print("Age must be greater than 0")
            else:
                print("Aga must be numeric!")

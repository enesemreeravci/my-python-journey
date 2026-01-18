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
        self.diseases = {
            "Influenza": "Rest, drink plenty of fluids, and use fever reducers if needed.",
            "Common Cold": "Rest, stay hydrated, and manage symptoms with basic care.",
            "Gastroenteritis": "Drink fluids to prevent dehydration and eat light foods.",
            "Migraine": "Rest in a quiet, dark room and use pain relief if necessary.",
            "Allergy": "Avoid known triggers and consider antihistamines.",
            "Unclear": "No clear diagnosis. Consult a healthcare professional if symptoms persist."
        }

    def get_user_input(self):
        #keep asking until at least one symptom is provided
        while True:
            raw_symptom = input("Enter your symptoms (comma-separated): ")
            list_of_symptoms = raw_symptom.split(",")

            cleaned_symptoms = []
            for i in list_of_symptoms:
                cleaned = i.strip().lower()
                if cleaned:
                    cleaned_symptoms.append(cleaned)

            if cleaned_symptoms:
                self.symptoms = cleaned_symptoms
                break
            else:
                print("Please enter at least one symptom.")

        # keep asking until a valid positive number is provided
        while True:
            user_age = input("Age: ")
            if user_age.isnumeric():
                age_int = int(user_age)
                if age_int > 0:
                    self.age = age_int
                    break
                else:
                    print("Age must be greater than 0.")
            else:
                print("Age must be numeric.")

        #  accept free text, normalize it
        user_history = input("Medical History (or 'none'): ")
        self.history = user_history.strip().lower()

    def categorize_symptoms(self):
        if "fever" in self.symptoms:
            if "cough" in self.symptoms or "sore throat" in self.symptoms:
                return "respiratory"
            elif "vomiting" in self.symptoms:
                return "gastro"
            else:
                return "unclear"
        else:
            if "rash" in self.symptoms:
                return "allergy"
            elif "headache" in self.symptoms:
                return "neurological"
            else:
                return "unclear"

    def diagnose(self, category):
        if category == "respiratory":
            if "fever" in self.symptoms and "cough" in self.symptoms:
                return "Influenza"
            else:
                return "Common Cold"
        elif category == "gastro":
            return "Gastroenteritis"
        elif category == "neurological":
            if "vomiting" in self.symptoms:
                return "Migraine"
            else:
                return "Migraine"
        elif category == "allergy":
            return "Allergy"
        else:
            return "Unclear"

    def risk_warnings(self):
        warnings = []

        if self.age >= 65:
            warnings.append("Higher risk due to age (65+). Consider seeking medical advice sooner.")

        # simple keyword checks in medical history
        if "asthma" in self.history or "diabetes" in self.history or "heart" in self.history:
            warnings.append("Higher risk due to medical history. Consider seeking medical advice sooner.")

        return warnings

    def print_result(self, diagnosis, treatment, warnings):
        print("\n--- Result ---")
        print(f"Symptoms: {', '.join(self.symptoms)}")
        print(f"Age: {self.age}")
        print(f"Medical History: {self.history if self.history else 'none'}")
        print(f"Possible Diagnosis: {diagnosis}")
        print(f"Suggested Treatment: {treatment}")

        if warnings:
            print("\nWarnings:")
            for w in warnings:
                print(f"- {w}")

    def run(self):
        self.get_user_input()
        category = self.categorize_symptoms()
        diagnosis = self.diagnose(category)
        treatment = self.diseases.get(diagnosis, self.diseases["Unclear"])
        warnings = self.risk_warnings()
        self.print_result(diagnosis, treatment, warnings)


if __name__ == "__main__":
    system = HealthDiagnosisSystem()
    system.run()

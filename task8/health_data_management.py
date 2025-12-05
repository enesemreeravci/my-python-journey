import csv

# function help us to load file while using try except.
def load_data(file_name):
    try:
        with open(file_name,   "r", newline="", encoding="utf-8") as file:
            csvFile = csv.reader(file)
            rows = []
            for lines in csvFile:
                rows.append(lines)
            return rows
    except FileNotFoundError:
        print("Error occurred while opening the file")
        return None

# checks if essential values are missed or not, if it's good and return with new version
def process_row(row):
    patient_id = row[0]
    name = row[1]
    age = row[2]
    height = row[3]
    weight = row[4]

    if height == "" or weight == "":
        return [patient_id, name, age, height,weight, "Error: Missing height or weight"]
    try:
        height_numeric = float(height)
        weight_numeric = float(weight)
        if height_numeric == 0:
            return [patient_id, name, age, height, weight, "Error: Height cannot be zero"]
        bmi = weight_numeric / (height_numeric * height_numeric)

        rounded_bmi = round(bmi, 3)
        return [patient_id, name, age, height, weight, rounded_bmi]
    except ValueError:
        return [patient_id, name, age, height, weight, "Error: Invalid number"]

def save_data(processed_rows, output_file):
    # write here
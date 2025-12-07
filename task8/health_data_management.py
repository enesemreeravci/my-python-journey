import csv
from urllib3.filepost import writer

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
    try:
        with open(output_file, "w",  newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Patient ID", "Name", "Age", "Height", "Weight", "BMI"])
            for row in processed_rows:
                writer.writerow(row)
    except FileNotFoundError:
        print("Error occurred while writing the file")
        return None

def main():
    try:
        rows = load_data("patient_data.csv")
        if rows is None:
            print("Input file not found")
            return
        data_rows = rows[1:] # for skipping header row, means write everyhting except header
        processed_rows = []
        for row in data_rows:
            result = process_row(row)
            processed_rows.append(result)
        save_data(processed_rows,"processed_patient_data.csv")
    except Exception as e:
        print("Unexpected Error:", e)


if __name__ == "__main__":
    main()
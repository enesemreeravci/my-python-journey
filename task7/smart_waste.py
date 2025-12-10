from abc import ABC, abstractmethod

from task8.health_data_management import save_data


class Waste(ABC):
    def __init__(self, weight: float):
        self.weight = weight

    @property
    @abstractmethod
    def waste_type(self) -> str:
        pass
    @abstractmethod
    def process(self) -> str:
        pass

    @abstractmethod
    def calculate_fee(self) -> float:
        pass

    @abstractmethod
    def generate_report(self) -> str:
        pass


class OrganicWaste(Waste):
    RATE_PER_KG = 5.0

    @property
    def waste_type(self) -> str:
        return "Organic"

    def process(self) -> str:
        return "Composting"

    def calculate_fee(self) -> float:
        return self.weight * self.RATE_PER_KG

    def generate_report(self) -> str:
        fee = self.calculate_fee()
        return f"{self.waste_type} Waste: {self.weight:.0f}kg, ${fee:.0f}"


class RecyclableWaste(Waste):
    RATE_PER_KG = 2.0

    @property
    def waste_type(self) -> str:
        return "Recyclable"

    def process(self) -> str:
        return "Recycling"

    def calculate_fee(self) -> float:
        return self.weight * self.RATE_PER_KG

    def generate_report(self) -> str:
        fee = self.calculate_fee()
        return f"{self.waste_type} Waste: {self.weight:.0f}kg, ${fee:.0f}"


class HazardousWaste(Waste):
    RATE_PER_KG = 10.0

    @property
    def waste_type(self) -> str:
        return "Hazardous"

    def process(self) -> str:
        return "Specialized disposal"

    def calculate_fee(self) -> float:
        return self.weight * self.RATE_PER_KG

    def generate_report(self) -> str:
        fee = self.calculate_fee()
        return f"{self.waste_type} Waste: {self.weight:.0f}kg, ${fee:.0f}"


def process_waste(waste_list):
    totals = {
        "Organic": {"weight": 0.0, "fee": 0.0},
        "Recyclable": {"weight": 0.0, "fee": 0.0},
        "Hazardous": {"weight": 0.0, "fee": 0.0},
    }

    for waste in waste_list:
        method = waste.process()
        fee = waste.calculate_fee()

        print(
            f"Processing {waste.waste_type} Waste (Weight: {waste.weight:.0f}kg) "
            f"using {method}. Fee: ${fee:.0f}"
        )

        totals[waste.waste_type]["weight"] += waste.weight
        totals[waste.waste_type]["fee"] += fee

    print("--- Summary Report ---")
    total_fee = 0.0

    for wtype in ["Organic", "Recyclable", "Hazardous"]:
        w = totals[wtype]["weight"]
        f = totals[wtype]["fee"]
        if w > 0:
            print(f"{wtype} Waste: {w:.0f}kg, ${f:.0f}")
        total_fee += f

    print(f"Total Fee Collected: ${total_fee:.0f}")


def main():
    waste_items = []

    while True:
        waste_type_input = input(
            "Enter the type of waste (Organic, Recyclable, Hazardous) or 'q' to finish: "
        ).strip().lower()

        if waste_type_input in ("q", "quit", ""):
            break

        if waste_type_input not in ("organic", "recyclable", "hazardous"):
            print("Invalid waste type. Please try again.")
            continue

        weight_str = input("Enter weight of waste (kg): ").strip()
        try:
            weight = float(weight_str)
            if weight <= 0:
                print("Weight must be positive.")
                continue
        except ValueError:
            print("Invalid weight.")
            continue

        if waste_type_input == "organic":
            waste_items.append(OrganicWaste(weight))
        elif waste_type_input == "recyclable":
            waste_items.append(RecyclableWaste(weight))
        else:
            waste_items.append(HazardousWaste(weight))

    if waste_items:
        process_waste(waste_items)
    else:
        print("No waste items entered. Exiting.")


if __name__ == "__main__":
    main()

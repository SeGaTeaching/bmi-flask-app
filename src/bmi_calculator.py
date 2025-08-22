class BMICalculator:
    def calculate_bmi(self, weight, height):
        if height <= 0:
            raise ValueError("Height must be greater than zero.")
        bmi = weight / (height ** 2)
        return round(bmi, 2)

    def get_bmi_category(self, bmi):
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 24.9:
            return "Normal weight"
        elif 25 <= bmi < 29.9:
            return "Overweight"
        else:
            return "Obesity"
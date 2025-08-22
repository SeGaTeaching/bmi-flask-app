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

    def get_health_info(self, bmi):
        if bmi < 18.5:
            return ("Untergewicht", "Achte auf eine ausgewogene Ernährung und konsultiere ggf. einen Arzt.")
        elif 18.5 <= bmi < 24.9:
            return ("Normalgewicht", "Herzlichen Glückwunsch! Halte deinen Lebensstil bei.")
        elif 25 <= bmi < 29.9:
            return ("Übergewicht", "Versuche, mehr Bewegung in deinen Alltag zu integrieren und achte auf deine Ernährung.")
        else:
            return ("Adipositas", "Sprich mit einem Arzt über gesunde Maßnahmen zur Gewichtsreduktion.")
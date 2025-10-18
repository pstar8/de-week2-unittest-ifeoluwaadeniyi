class ArtificialPancreasSystem:
    def __init__(self, glucose_level, insulin_sensitivity = 1.0, target_glucose = 100, tolerance = 10):
        self.glucose_level = glucose_level
        self.insulin_sensitivity = insulin_sensitivity
        self.target_glucose = target_glucose
        self.tolerance = tolerance

        self.total_insulin_delivered = 0.0

    def meal(self, carbs: float):
        """Simulate a meal event (input feature: carbs)."""
        glucose_increase = carbs * 0.5 
        self.glucose_level += glucose_increase


    def exercise(self, duration: float):
     """Simulate physical activity (input feature: duration)."""
     glucose_burn = duration * 0.3
     self.glucose_level -= glucose_burn
     if self.glucose_level < 50:
         self.glucose_level = 50

    def predict_action(self):
        """Predict and apply an appropriate system action. Acts like a decision function in a model."""
        if self.glucose_level > self.target_glucose + self.tolerance:
            excess_glucose = self.glucose_level - self.target_glucose
            insulin_dose = excess_glucose / self.insulin_sensitivity            
            self.glucose_level -= insulin_dose
            self.total_insulin_delivered += insulin_dose
            return("deliver_insulin", self.glucose_level)
        elif self.glucose_level < self.target_glucose - self.tolerance:
            return("warn_low_glucose", self.glucose_level)
        else:
            return("maintain", self.glucose_level)
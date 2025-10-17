from main.artificial_pancreas import ArtificialPancreasSystem

# Test the complete flow
system = ArtificialPancreasSystem(100)
print(f"Initial: {system.glucose_level}")

system.meal(40)
print(f"After meal: {system.glucose_level}")  # Should be 120

action, level = system.predict_action()
print(f"Action: {action}, Level: {level}")  # Should deliver insulin

print(f"Total insulin: {system.total_insulin_delivered}")  # Should be ~20
import pytest

from main.artificial_pancreas import ArtificialPancreasSystem

@pytest.fixture
def system():
    return ArtificialPancreasSystem(glucose_level = 100, insulin_sensitivity = 1.0, target_glucose = 100, tolerance = 10)


# Glucose increases after a meal
def test_glucose_increases_after_meal(system):
    initial_glucose = system.glucose_level
    carbs = 60  # Example carbohydrate intake
    system.meal(carbs)

    assert system.glucose_level == initial_glucose + (carbs * 0.5)

# Glucose never drops below minimum
def test_glucose_never_below_min(system):

   initial_glucose = system.glucose_level
   exercise_duration = 80000

   system.exercise(exercise_duration)

   assert system.glucose_level >= 50

# Glucose decreases after exercise
def test_glucose_decreases_after_exercise(system):
   initial_glucose = system.glucose_level
   exercise_duration = 20

   system.exercise(exercise_duration)

   assert system.glucose_level == initial_glucose - (exercise_duration * 0.3)

# Correct action is returned 
def test_correct_action(system):
    #High glucose
    system.glucose_level = 150
    action, glucose = system.predict_action()
    assert action == "deliver_insulin"
    
    #Low glucose
    system.glucose_level = 80
    action, glucose = system.predict_action()
    assert action == "warn_low_glucose"
    
    #Normal glucose
    system.glucose_level = 100
    action, glucose = system.predict_action()
    assert action == "maintain"

# Total insulin tracking
def test_total_insulin_tracking(system):
    total_insulin_before = system.total_insulin_delivered
    system.glucose_level = 170

    insulin_delivered = (system.glucose_level - system.target_glucose) / system.insulin_sensitivity

    action, glucose = system.predict_action()

    assert system.total_insulin_delivered == total_insulin_before + insulin_delivered


# Multiple sequential events
def test_multiple_sequential_events(system):
    system.meal(100) 
    glucose_after_meal = system.glucose_level

    system.exercise(60) 
    glucose_after_exercise = system.glucose_level

    action, glucose = system.predict_action()


    assert glucose_after_meal == 150
    assert glucose_after_exercise == 132
    assert action == "deliver_insulin"
    assert system.total_insulin_delivered == 32


# Invalid input handling
def test_invalid_input_handling(system):
    system.glucose_level = 100

    system.meal(-50)
    assert system.glucose_level == 75

    system.exercise(-20)
    assert system.glucose_level == 81
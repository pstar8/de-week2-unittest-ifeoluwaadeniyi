# Artificial Pancreas System - Glucose Management Prototype

A simplified Python-based model simulating an Artificial Pancreas System for intelligent glucose regulation. This project demonstrates Object-Oriented Programming principles, algorithmic decision-making, and comprehensive unit testing using pytest.

---

## 📋 About The Project

This project is a prototype model that simulates how an Artificial Pancreas System manages blood glucose levels. The system responds to real-world inputs like meals and exercise, making intelligent decisions about insulin delivery to maintain safe glucose levels.

### What is an Artificial Pancreas System?

For millions of people living with diabetes, managing blood glucose is a constant challenge requiring frequent monitoring and decision-making. An Artificial Pancreas System automates this process by:

- Continuously monitoring glucose levels
- Predicting glucose changes from meals and activity
- Automatically delivering insulin when needed
- Maintaining glucose within a safe target range

This simplified model captures the core logic of such systems, providing insight into how data-driven healthcare technology can support better patient outcomes.

---

## ✨ Features

- **Meal Simulation** - Models glucose increase from carbohydrate intake
- **Exercise Simulation** - Models glucose decrease from physical activity
- **Intelligent Decision Making** - Automatically determines when to:
  - Deliver insulin (high glucose)
  - Warn about low glucose
  - Maintain current state (stable glucose)
- **Insulin Tracking** - Monitors total insulin delivered over time
- **Safety Mechanisms** - Prevents glucose from dropping below critical levels
- **Comprehensive Testing** - 7+ unit tests ensuring system reliability

---

## 🛠️ Technologies Used

- **Python 3.12** - Core programming language
- **pytest 7.0+** - Testing framework for unit tests
- **Git/GitHub** - Version control and collaboration

---

## 📁 Project Structure

python
```
de-week2-unittest-d/
├── main/
│   ├── __init__.py
│   └── artificial_pancreas.py      # Core ArtificialPancreasSystem class
├── tests/
│   ├── __init__.py
│   └── test_artificial_pancreas.py # Comprehensive test suite
├── README.md                        # Project documentation
├── requirements.txt                 # Project dependencies
└── .gitignore                       # Git ignore rules
```

---

## 🚀 Installation

### Prerequisites

- Python 3.12 or higher
- pip (Python package manager)

### Setup Steps

1. **Clone the repository**

   ```bash
   git clone https://github.com/pstar8/de-week2-unittest-d.git
   cd de-week2-unittest-d
   ```

2. **Create a virtual environment (recommended)**

   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On Mac/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

## 🧪 Running Tests

The project includes a comprehensive test suite with 7 core tests covering all system functionality.

### Run all tests

```bash
pytest tests/
```

### Run tests with verbose output

```bash
pytest tests/ -v
```

### Run tests with coverage report

```bash
pytest tests/ --cov=main
```

### Test Coverage

The test suite verifies:

1. ✅ **Glucose increases after meals** - Validates carb intake logic
2. ✅ **Glucose decreases after exercise** - Validates activity logic
3. ✅ **Correct actions are returned** - Tests decision-making for high/low/stable glucose
4. ✅ **Glucose never drops below minimum** - Validates safety floor (50 mg/dL)
5. ✅ **Total insulin tracking** - Ensures accurate insulin delivery monitoring
6. ✅ **Multiple sequential events** - Tests state persistence across event chains
7. ✅ **Invalid input handling** - Documents behavior with negative inputs

---

## 👤 Author

### D

- GitHub: [@pstar8](https://github.com/pstar8)
- Repo: [de-week2-unittest-ifeoluwaadeniyi](https://github.com/pstar8/de-week2-unittest-ifeoluwaadeniyi)

---

## 📄 License

This project is created for educational purposes as part of a programming assignment.

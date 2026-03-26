<div align="center">

# 🚗 Automated Parking System

[![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![University](https://img.shields.io/badge/Arden_University-BSc_Computing-red?style=for-the-badge)](https://arden.ac.uk)
[![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)]()

**A terminal-based parking management system built in Python — simulating real-world car park operations including time simulation, fee calculation, and penalty enforcement.**

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [How It Works](#-how-it-works)
- [Getting Started](#-getting-started)
- [Usage](#-usage)
- [Code Structure](#-code-structure)
- [Skills Demonstrated](#-skills-demonstrated)
- [Academic Context](#-academic-context)

---

## 🔍 Overview

The **Automated Parking System** is a command-line application that simulates the operation of a managed car park. It allows an operator to configure the system, simulate time passing, manage vehicle entry/exit, and generate fee reports — all with input validation and penalty logic built in.

> Developed as part of BSc Computing coursework at **Arden University**, this project applies core Python concepts to a practical, real-world problem.

---

## ✨ Features

| Feature | Description |
|---|---|
| ⚙️ **System Setup** | Configure capacity, hourly rate, max hours, and penalty |
| ⏱️ **Time Simulation** | Advance the internal clock to simulate parking durations |
| 🚘 **Park a Vehicle** | Register a car with its arrival time, reject if full |
| 🏁 **Retrieve a Vehicle** | Calculate and display the charge on exit |
| 📊 **Status Dashboard** | View occupancy, average time, and overstay violations |
| 💰 **Fee & Penalty Engine** | Tiered pricing: minimum charge → hourly rate → penalty |
| 🛡️ **Input Validation** | All inputs validated with helpful error messages |

---

## ⚙️ How It Works

### Fee Calculation Logic

```
Duration < 1 hour   →  Flat minimum charge (1 × hourly rate)
Duration ≤ max hrs  →  hours × hourly_rate
Duration > max hrs  →  (max_hrs × hourly_rate) + (penalty_units × unit_penalty)
```

**Penalty units** are calculated by rounding up the number of exceeded hour-blocks:

```python
penalty_units = (exceeded_hours + max_hours - 1) // max_hours  # ceiling division
```

### System Flow

```
START
  └── Initial Setup (capacity, rate, max hours, penalty)
        └── Main Menu Loop
              ├── 1) Simulate Time    → advance internal clock
              ├── 2) Park a Car       → register vehicle if space available
              ├── 3) Get a Car        → compute charge & remove vehicle
              ├── 4) Show Status      → display occupancy & overstay info
              └── Q) Quit
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed — [Download here](https://python.org/downloads)
- No external libraries required — uses Python's standard library only

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/qadaz/automated-parking-system.git

# 2. Navigate into the directory
cd automated-parking-system

# 3. Run the program
python parking_system.py
```

---

## 💻 Usage

Once launched, you'll be guided through an initial setup, then presented with the main menu:

```
==================================================
INITIAL SYSTEM SETUP
==================================================
Capacity of the car park: 10
Hourly parking rate: 2.50
Maximum hours before penalty: 4
Unit penalty: 15.00

==================================================
AUTOMATED PARKING SYSTEM
==================================================
Time: 0h | Cars: 0/10
--------------------------------------------------
1) Simulate time (operator)
2) Park a car (customer)
3) Get a car (customer)
4) Show car park status (operator)
Q) Quit
--------------------------------------------------
```

### Example Session

```
> Select 2  →  Park "AB12CDE" at time 0h  →  Spaces used: 1/10
> Select 1  →  Simulate 3 hours           →  Total: 3h
> Select 3  →  Retrieve "AB12CDE"         →  TOTAL CHARGE: £7.50
```

---

## 🗂️ Code Structure

```
automated-parking-system/
│
├── parking_system.py            # Main application file
│   ├── initial_system_setup()   # One-time configuration with validation
│   ├── simulate_time()          # Advances the internal clock
│   ├── park_car()               # Handles vehicle entry
│   ├── get_car()                # Handles vehicle exit & fee calculation
│   ├── show_status()            # Displays car park statistics
│   └── main_menu()              # Entry point & main loop
│
└── README.md                    # Project documentation
```

---

## 💡 Skills Demonstrated

- **Python programming** — clean, readable, and well-commented code
- **Control structures** — loops, conditionals, and exception handling
- **Data structures** — dictionaries for O(1) vehicle lookups by registration
- **Input validation** — robust `try/except` blocks on every user input
- **Algorithm design** — ceiling division for penalty unit calculation
- **Modular design** — single-responsibility functions with clear separation of concerns
- **Problem-solving** — translating a real-world system into working software logic

---

## 📚 Academic Context

This project was developed as part of the **BSc Computing** degree at **Arden University**.

The objective was to design and implement a functional automated parking management system using Python, applying core programming principles including:

- Structured problem-solving and requirements analysis
- Modular code design and reusable functions
- Input validation and error handling
- Simulation of real-world business logic (fees, penalties, capacity)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

<div align="center">

Made with ❤️ by [qadaz](https://github.com/qadaz) · BSc Computing — Arden University

</div>

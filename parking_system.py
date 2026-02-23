# File Name: STU185471.py
# Tasks 2 & 3: Complete Automated Parking System

def initial_system_setup():
    """
    TASK 2: Initial system setup with validation.
    Called only once at program start.
    """
    print("\n" + "="*50)
    print("INITIAL SYSTEM SETUP")
    print("="*50)
    
    while True:  # Getting capacity with validation 
        try:
            capacity = int(input("Capacity of the car park: "))
            if capacity > 0:
                break
            else:
                print("Capacity must be positive.")
        except ValueError:
            print("Please enter a valid integer.")
    
    while True:    # Getting hourly rate with validation
        try:
            hourly_rate = float(input("Hourly parking rate: "))
            if hourly_rate > 0:
                break
            else:
                print("Hourly rate must be positive.")
        except ValueError:
            print("Please enter a valid number.")
    
    while True:  # Getting max hours with validation
        try:
            max_hours = int(input("Maximum hours before penalty: "))
            if max_hours > 0:
                break
            else:
                print("Maximum hours must be positive.")
        except ValueError:
            print("Please enter a valid integer.")
    
    min_penalty = hourly_rate * max_hours   # Geting unit penalty with validation
    while True:
        try:
            unit_penalty = float(input("Unit penalty: "))
            if unit_penalty > min_penalty:
                break
            else:
                print(f"Unit penalty must be greater than {min_penalty:.2f}")
        except ValueError:
            print("Please enter a valid number.")
    
    # Initialising variables for Task 3

    total_hours_passed = 0
    parked_cars = {}  # Dictionary: {registration: start_time}
    
    print("\n" + "="*50)
    print("SETUP COMPLETE")
    print("="*50)
    
    return capacity, hourly_rate, max_hours, unit_penalty, total_hours_passed, parked_cars

def simulate_time(total_hours_passed):
    """
    TASK 2: Option 1 - Simulate time passing.
    """
    print("\n" + "-"*40)
    print("SIMULATE TIME")
    print("-"*40)
    
    while True:
        try:
            hours = int(input("Enter hours to simulate: "))
            if hours > 0:
                break
            else:
                print("Hours must be positive.")
        except ValueError:
            print("Please enter a valid integer.")
    
    total_hours_passed += hours
    print(f"Simulated {hours} hours. Total: {total_hours_passed} hours")
    
    return total_hours_passed

def park_car(parked_cars, capacity, total_hours_passed):
    """
    TASK 3, Option 2: Park a car in the system.
    """
    print("\n" + "-"*40)
    print("PARK A CAR")
    print("-"*40)
    
    if len(parked_cars) >= capacity:    # Checking if car park is full
        print("Car park is FULL. Parking rejected.")
        return parked_cars
    
    reg = input("Enter car registration: ").strip().upper()   # Getting car registration number
    
    if reg in parked_cars:   # Checking if car already exists already
        print(f"Car {reg} is already parked.")
        return parked_cars
    
    parked_cars[reg] = total_hours_passed  # Parking the car
    print(f"Car {reg} parked at time {total_hours_passed}.")
    print(f"Spaces used: {len(parked_cars)}/{capacity}")
    
    return parked_cars

def get_car(parked_cars, total_hours_passed, hourly_rate, max_hours, unit_penalty):
    """
    TASK 3, Option 3: Get a parked car and calculate charge.
    """
    print("\n" + "-"*40)
    print("GET A CAR")
    print("-"*40)
    
    reg = input("Enter car registration: ").strip().upper()    # Getting registration number
    
    if reg not in parked_cars:  # Checking if car exists already
        print(f"Car {reg} not found.")
        return parked_cars
    
    start_time = parked_cars[reg]   # Calculating the parking duration
    hours_parked = total_hours_passed - start_time
    
    if hours_parked < 1:  # Calculating charges based on hours duration 
        # Less than 1 hour: minimum charge
        charge = hourly_rate
        print("Parked for less than 1 hour (minimum charge)")
    elif hours_parked <= max_hours:
        # Within maximum hours: normal rate
        charge = hours_parked * hourly_rate
        print(f"Parked for {hours_parked} hours (within limit)")
    else:
        # Exceeded maximum hours: penalty applies
        exceeded_hours = hours_parked - max_hours
        
        # (exceeded_hours + max_hours - 1) // max_hours rounds UP
        penalty_units = (exceeded_hours + max_hours - 1) // max_hours
        
        normal_charge = max_hours * hourly_rate
        penalty_charge = penalty_units * unit_penalty
        charge = normal_charge + penalty_charge
        
        print(f"Parked for {hours_parked} hours (EXCEEDED limit by {exceeded_hours}h)")
        print(f"Penalty units: {penalty_units}")
    
    del parked_cars[reg] # Removing car and displaying the charge
    
    print(f"\nTOTAL CHARGE: £{charge:.2f}")
    print(f"Car {reg} retrieved.")
    
    return parked_cars

def show_status(parked_cars, total_hours_passed, max_hours):
    """
    TASK 3, Option 4: Show car park status.
    """
    print("\n" + "-"*40)
    print("CAR PARK STATUS")
    print("-"*40)
    
    if not parked_cars:   # Checking if any cars are parked
        print("No cars currently parked.")
        return
    
    total_cars = len(parked_cars)  # Calculating statistics
    total_hours = 0
    exceeded_cars = []
    
    for reg, start_time in parked_cars.items():
        hours_parked = total_hours_passed - start_time
        total_hours += hours_parked
        
        if hours_parked > max_hours:
            exceeded_cars.append(reg)
    
    avg_hours = total_hours / total_cars if total_cars > 0 else 0
    
    # Displaying stats 
    print(f"1. Number of cars in car park: {total_cars}")
    print(f"2. Average hours parked: {avg_hours:.1f}")
    print(f"3. Cars exceeded max hours: {len(exceeded_cars)}")
    
    if exceeded_cars:  # Displaying exceeded cars if there is any
        print(f"4. Registration numbers of exceeded cars:")
        for reg in exceeded_cars:
            hours = total_hours_passed - parked_cars[reg]
            print(f"   • {reg} ({hours} hours)")

def main_menu():
    """
    Main menu that integrates ALL Task 2 and Task 3 functionality.
    """
    # TASK 2: Initial Setup (called only once)
    capacity, hourly_rate, max_hours, unit_penalty, total_hours_passed, parked_cars = initial_system_setup()
    
    while True:  # Main loop
        print("\n" + "="*50)
        print("AUTOMATED PARKING SYSTEM")
        print("="*50)
        print(f"Time: {total_hours_passed}h | Cars: {len(parked_cars)}/{capacity}")
        print("-"*50)
        print("1) Simulate time (operator)")
        print("2) Park a car (customer)")
        print("3) Get a car (customer)")
        print("4) Show car park status (operator)")
        print("Q) Quit")
        print("-"*50)
        
        choice = input("Select (1/2/3/4/Q): ").strip().upper()
        
        if choice == "1":
            # TASK 2: Option 1
            total_hours_passed = simulate_time(total_hours_passed)
        elif choice == "2":
            # TASK 3: Option 2
            parked_cars = park_car(parked_cars, capacity, total_hours_passed)
        elif choice == "3":
            # TASK 3: Option 3
            parked_cars = get_car(parked_cars, total_hours_passed, hourly_rate, max_hours, unit_penalty)
        elif choice == "4":
            # TASK 3: Option 4
            show_status(parked_cars, total_hours_passed, max_hours)
        elif choice == "Q":
            print("\nGoodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":  # Using this to run the program automatically 
    main_menu()
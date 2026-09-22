name = input("What is your name? ")
print("Hello, " + name + "! Welcome to the vehicle performance calculator.")
while True:
    print("\nPlease select an option:")
    print("1. Calculate distance traveled")
    print("2. Calculate power to mass ratio")
    print("3. Calculate the vehicle power from the force and speed")
    print("4. Calculate vehicle weight")
    print("5. Calculate vehicle speed")
    print("6. Calculate vehicle acceleration")
    print("7. Calculate vehicle acceleration from force and mass")
    print("8. Exit")    

    choice = input("Enter your choice (1-8): ")
    if choice == '1':   
        def calculate_distance(speed, time):
            return speed * time
        speed = float(input("Enter the speed of the vehicle in m/s: "))
        time = float(input("Enter the time traveled in seconds: "))
        distance = calculate_distance(speed, time)
        print("The distance traveled is", distance, "m")

    elif choice == '2':
        def calculate_power_to_mass_ratio(power, mass):
            return power / mass
        power = float(input("Enter the power of the vehicle in watts: "))
        mass = float(input("Enter the mass of the vehicle in kilograms: "))
        ratio = calculate_power_to_mass_ratio(power, mass)
        print("Power to mass ratio is", ratio, "W/kg")

    elif choice == '3':
        def calculate_power(force, speed):
            return force * speed
        force = float(input("Enter the driving force in newtons: "))
        speed = float(input("Enter the speed of the vehicle in m/s: "))
        power = calculate_power(force, speed)
        print("The power of the vehicle is", power, "W")
        
    elif choice == '4':
        def calculate_weight(mass):
            return mass * 9.81
        mass = float(input("Enter the mass of the vehicle in kilograms: "))
        weight = calculate_weight(mass)
        print("The weight of the vehicle is", weight, "N")

    elif choice == '5':
        def calculate_speed(distance, time):
            return distance / time
        distance = float(input("Enter the distance traveled in meters: "))
        time = float(input("Enter the time traveled in seconds: "))
        speed = calculate_speed(distance, time)         
        print("The speed of the vehicle is", speed, "m/s")

    elif choice == '6':
        def calculate_acceleration(initial_speed, final_speed, time):
            return (final_speed - initial_speed) / time
        initial_speed = float(input("Enter the initial speed of the vehicle in m/s: "))
        final_speed = float(input("Enter the final speed of the vehicle in m/s: "))
        time = float(input("Enter the time taken to change speed in seconds: "))
        acceleration = calculate_acceleration(initial_speed, final_speed, time)   

        print("The acceleration of the vehicle is", acceleration, "m/s²")
    elif choice == '7':
        def calculate_acceleration(force, mass):
            return force / mass
        force = float(input("Enter the driving force in newtons: "))
        mass = float(input("Enter the vehicle mass in kilograms: "))
        acceleration = calculate_acceleration(force, mass)
        print("The vehicle acceleration is", acceleration, "m/s²")

    elif choice == '8':
        print("Exiting the vehicle performance calculator. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 8.")

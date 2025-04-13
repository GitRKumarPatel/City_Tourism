# Base Class: Transport
class Transport:
    def __init__(self, transport_type, route, capacity, base_fare):
        self.transport_type = transport_type
        self.route = route
        self.capacity = capacity
        self.base_fare = base_fare

    def display_info(self):
        print("\n--- Transport Information ---")
        print(f"Transport Type : {self.transport_type}")
        print(f"Route          : {self.route}")
        print(f"Capacity       : {self.capacity}")
        print(f"Base Fare/km   : ₹{self.base_fare}")

    def calculate_fare(self, distance):
        return self.base_fare * distance


# Derived Class: Bus
class Bus(Transport):
    def __init__(self, route, capacity, base_fare, bus_number):
        super().__init__('Bus', route, capacity, base_fare)
        self.bus_number = bus_number

    def display_info(self):
        super().display_info()
        print(f"Bus Number     : {self.bus_number}")


# Derived Class: Train
class Train(Transport):
    def __init__(self, route, capacity, base_fare, train_name):
        super().__init__('Train', route, capacity, base_fare)
        self.train_name = train_name

    def display_info(self):
        super().display_info()
        print(f"Train Name     : {self.train_name}")


# Derived Class: Taxi
class Taxi(Transport):
    def __init__(self, route, capacity, base_fare, driver_name):
        super().__init__('Taxi', route, capacity, base_fare)
        self.driver_name = driver_name

    def display_info(self):
        super().display_info()
        print(f"Driver Name    : {self.driver_name}")


# Main Program Starts Here
print("Welcome to City Tourism - Transport Booking System")
print("Select a transport type:")
print("1. Bus\n2. Train\n3. Taxi")
choice = input("Enter your choice (1/2/3): ")

route = input("Enter route (e.g., City Center to Airport): ")
capacity = int(input("Enter capacity: "))
base_fare = float(input("Enter base fare per km (₹): "))
distance = float(input("Enter distance to travel (in km): "))

# Handle choice and create corresponding object
if choice == '1':
    bus_number = input("Enter bus number: ")
    transport = Bus(route, capacity, base_fare, bus_number)
elif choice == '2':
    train_name = input("Enter train name: ")
    transport = Train(route, capacity, base_fare, train_name)
elif choice == '3':
    driver_name = input("Enter driver name: ")
    transport = Taxi(route, capacity, base_fare, driver_name)
else:
    print("Invalid choice. Please restart the program.")
    exit()

# Show transport details and fare
transport.display_info()
fare = transport.calculate_fare(distance)
print(f"\nTotal Fare for {distance} km: ₹{fare:.2f}")
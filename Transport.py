class Transport:
    def __init__(self, transport_type, route, capacity, base_fare):
        self.transport_type = transport_type
        self.route = route
        self.capacity = capacity
        self.base_fare = base_fare

    def display_info(self):
        print(f"Transport Type: {self.transport_type}")
        print(f"Route: {self.route}")
        print(f"Capacity: {self.capacity}")
        print(f"Base Fare: ₹{self.base_fare}")

    def calculate_fare(self, distance):
        return self.base_fare * distance

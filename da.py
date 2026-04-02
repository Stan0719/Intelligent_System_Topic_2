class DeliveryAgent:
    def __init__(self, agent_id, capacity):
        self.agent_id = agent_id
        self.capacity = capacity
        self.assigned_route = []

    def send_capacity(self):
        return self.capacity

    def receive_route(self, route):
        self.assigned_route = route

    def display_route(self):
        print(f"\nDelivery Agent {self.agent_id}")
        print(f"Capacity: {self.capacity}")
        print("Assigned Route:")
        for location in self.assigned_route:
            print(location)
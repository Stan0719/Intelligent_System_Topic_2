class DeliveryAgent:
    def __init__(self, agent_id, capacity):
        self.agent_id = agent_id
        self.capacity = capacity
        self.assigned_deliveries = []

    def send_capacity(self):
        return {"agent_id": self.agent_id, "capacity": self.capacity}

    def receive_route(self, deliveries):
        self.assigned_deliveries = deliveries

    def show_route(self):
        names = [d[0] for d in self.assigned_deliveries]
        return f"{self.agent_id}: {names}"
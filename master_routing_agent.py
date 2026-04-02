class MasterRoutingAgent:
    def __init__(self):
        self.agent_capacities = {}

    def receive_capacity(self, info):
        self.agent_capacities[info["agent_id"]] = info["capacity"]

    def assign_deliveries(self, deliveries, agents):
        delivery_index = 0

        for agent in agents:
            capacity = self.agent_capacities[agent.agent_id]
            assigned = deliveries[delivery_index:delivery_index + capacity]
            agent.receive_route(assigned)
            delivery_index += capacity
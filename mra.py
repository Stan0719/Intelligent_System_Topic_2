from utils import total_route_distance

class MasterRoutingAgent:
    def __init__(self, warehouse=(0, 0)):
        self.warehouse = warehouse
        self.delivery_agents = []
        self.parcels = []

    def register_agent(self, agent):
        self.delivery_agents.append(agent)

    def receive_parcels(self, parcel_list):
        self.parcels = parcel_list

    def collect_capacities(self):
        capacities = {}
        for agent in self.delivery_agents:
            capacities[agent.agent_id] = agent.send_capacity()
        return capacities

    def assign_routes(self):
        """
        Simple basic assignment:
        Assign parcels to each DA based on capacity in order.
        """
        parcel_index = 0

        for agent in self.delivery_agents:
            assigned = []
            for _ in range(agent.capacity):
                if parcel_index < len(self.parcels):
                    assigned.append(self.parcels[parcel_index])
                    parcel_index += 1
            agent.receive_route(assigned)

    def display_all_routes(self):
        print("\n=== FINAL ROUTE ASSIGNMENT ===")
        for agent in self.delivery_agents:
            distance = total_route_distance(agent.assigned_route, self.warehouse)
            print(f"\nAgent {agent.agent_id}")
            print(f"Route: {agent.assigned_route}")
            print(f"Total Distance: {distance:.2f}")
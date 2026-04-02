from data import warehouse, deliveries, vehicles
from delivery_agent import DeliveryAgent
from master_routing_agent import MasterRoutingAgent
from routing_utils import route_distance

def main():
    # Create delivery agents
    agents = []
    for v in vehicles:
        agents.append(DeliveryAgent(v["id"], v["capacity"]))

    # Create master routing agent
    mra = MasterRoutingAgent()

    # Agents send capacities to MRA
    for agent in agents:
        mra.receive_capacity(agent.send_capacity())

    # MRA assigns deliveries
    mra.assign_deliveries(deliveries, agents)

    # Show results
    print("Warehouse:", warehouse[0])
    print()

    for agent in agents:
        print(agent.show_route())
        dist = route_distance(warehouse, agent.assigned_deliveries)
        print("Total distance:", round(dist, 4))
        print()

if __name__ == "__main__":
    main()
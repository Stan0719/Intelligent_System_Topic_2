from da import DeliveryAgent
from mra import MasterRoutingAgent

def main():
    # Step 1: Create Master Routing Agent
    mra = MasterRoutingAgent(warehouse=(0, 0))

    # Step 2: Create Delivery Agents
    da1 = DeliveryAgent(agent_id="DA1", capacity=2)
    da2 = DeliveryAgent(agent_id="DA2", capacity=2)

    # Step 3: Register Delivery Agents to MRA
    mra.register_agent(da1)
    mra.register_agent(da2)

    # Step 4: Example parcel locations
    parcels = [
        (2, 3),
        (5, 1),
        (6, 7),
        (1, 8)
    ]

    # Step 5: Send parcels to MRA
    mra.receive_parcels(parcels)

    # Step 6: Collect capacities
    capacities = mra.collect_capacities()
    print("Collected Capacities:", capacities)

    # Step 7: Assign routes
    mra.assign_routes()

    # Step 8: Show final routes
    mra.display_all_routes()

    # Step 9: Each DA displays their own route
    da1.display_route()
    da2.display_route()

if __name__ == "__main__":
    main()
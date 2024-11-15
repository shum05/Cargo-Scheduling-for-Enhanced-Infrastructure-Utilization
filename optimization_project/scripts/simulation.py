import pandas as pd
import numpy as np

def simulate_traffic(traffic_data, duration=10):
    simulation_results = []
    for _ in range(duration):
        traffic_data['vehicle_count'] += np.random.randint(-5, 5, size=len(traffic_data))
        simulation_results.append(traffic_data.copy())
    return simulation_results

if __name__ == "__main__":
    traffic_data = pd.read_csv("../data/Cleaned_Traffic_Flow.csv")
    results = simulate_traffic(traffic_data)
    for day in results:
        print(day.head())

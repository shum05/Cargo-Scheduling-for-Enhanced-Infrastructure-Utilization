import pandas as pd

def optimize_cargo_schedule(file_path):
    data = pd.read_csv(file_path)
    high_priority = data[data['priority'] == 'High']
    high_priority.sort_values(by='schedule_time', inplace=True)
    print("Optimized High Priority Cargo Schedule:")
    print(high_priority[['cargo_id', 'origin', 'destination', 'schedule_time']])

if __name__ == "__main__":
    optimize_cargo_schedule("../data/Cargo_Schedule.csv")

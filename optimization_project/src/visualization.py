import matplotlib.pyplot as plt

def plot_vehicle_count_over_time(data):
    plt.plot(data['timestamp'], data['vehicle_count'])
    plt.title("Vehicle Count Over Time")
    plt.xlabel("Timestamp")
    plt.ylabel("Vehicle Count")
    plt.show()

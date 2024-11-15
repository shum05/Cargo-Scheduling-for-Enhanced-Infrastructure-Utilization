import pandas as pd

def clean_traffic_data(file_path):
    data = pd.read_csv(file_path)
    data.dropna(inplace=True)
    data['timestamp'] = pd.to_datetime(data['timestamp'])
    data = data[data['avg_speed'] > 0]  # Remove erroneous data
    return data

if __name__ == "__main__":
    cleaned_data = clean_traffic_data("../data/Traffic_Flow.csv")
    cleaned_data.to_csv("../data/Cleaned_Traffic_Flow.csv", index=False)

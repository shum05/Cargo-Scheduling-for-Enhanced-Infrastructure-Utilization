from scripts.data_cleaning import clean_traffic_data
from scripts.traffic_model import train_traffic_model
from scripts.cargo_optimization import optimize_cargo_schedule

def main():
    print("Starting data cleaning...")
    cleaned_traffic_data = clean_traffic_data("../data/Traffic_Flow.csv")
    cleaned_traffic_data.to_csv("../data/Cleaned_Traffic_Flow.csv", index=False)

    print("Training traffic prediction model...")
    model = train_traffic_model("../data/Cleaned_Traffic_Flow.csv")

    print("Optimizing cargo schedule...")
    optimize_cargo_schedule("../data/Cargo_Schedule.csv")

if __name__ == "__main__":
    main()

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def train_traffic_model(file_path):
    data = pd.read_csv(file_path)
    X = data[['vehicle_count']]
    y = data['avg_speed']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)
    print(f"Model R-squared: {score}")

    return model

if __name__ == "__main__":
    model = train_traffic_model("../data/Cleaned_Traffic_Flow.csv")

import os

# Define the folder structure as a dictionary
folders = {
    "optimization_project": [
        "data",
        "notebooks",
        "scripts",
        "src",
        "reports",
        "reports/visualizations"
    ]
}

files = {
    "optimization_project": ["README.md", "requirements.txt", "LICENSE"],
    "optimization_project/data": [
        "Traffic_Flow.csv",
        "Cargo_Schedule.csv",
        "Weather_Data.csv",
        "Incident_Report.csv",
        "Road_Network.csv"
    ],
    "optimization_project/notebooks": [
        "data_exploration.ipynb",
        "traffic_analysis.ipynb",
        "cargo_schedule_optimization.ipynb",
        "simulation.ipynb"  # Notebook for interactive simulation
    ],
    "optimization_project/scripts": [
        "data_cleaning.py",
        "traffic_model.py",
        "cargo_optimization.py",
        "utils.py",
        "main.py",
        "simulation.py"  # Script for core simulation logic
    ],
    "optimization_project/src": [
        "visualization.py"
    ],
    "optimization_project/reports": [
        "findings_summary.md"
    ],
    "optimization_project/reports/visualizations": [
        "traffic_flow.png",
        "cargo_schedule.png"
    ]
}


# Function to create folders and files
def create_project_structure(base_dir, folders, files):
    # Create base directories
    for folder, subfolders in folders.items():
        base_folder_path = os.path.join(base_dir, folder)
        for subfolder in subfolders:
            path = os.path.join(base_folder_path, subfolder)
            os.makedirs(path, exist_ok=True)
    
    # Create files
    for folder, file_list in files.items():
        for file_name in file_list:
            file_path = os.path.join(base_dir, folder, file_name)
            with open(file_path, "w") as f:
                f.write("")  # Create an empty file

# Define the base directory for the project (current directory here)
base_dir = os.getcwd()

# Create the folder structure
create_project_structure(base_dir, folders, files)

print(f"Project structure created at {base_dir}/optimization_project")

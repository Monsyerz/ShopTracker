#Creating a project to manage taks and deadlines around the project.
#At first i creat the class with the name "Project" and then i create the init method to initialize the project with a name, description, and deadline.

from datetime import datetime
#add the json module to save the project details in a json file - before the SQL (just to test if it's working)
import json
#use pathlib to create a path for the json file and to make sure that the file is created in the same directory as the main.py file.
from pathlib import Path
class  Project:
    def __init__(self,name,description,start_date,due_date,status=None):
        self.name = name
        self.description = description
        self.start_date = start_date
        self.due_date = due_date
        self.status = status if status is not None else "Not Started"

#add method show_details to display the project details in a formatted way.    
    def show_details(self):
        print("\n--- Project Details ---")
        print(f"Name: {self.name}")
        print(f"Description: {self.description}")
        print(f"Start date: {self.start_date}")
        print(f"Due date: {self.due_date}")
        print(f"Status: {self.status}")
#add methof to_dictionary to convert the project details into a dictionary format, which can be useful for saving the data in a JSON file or other formats.

    def to_dictionary(self):
        return {
            "name": self.name,
            "description": self.description,
            "start_date": self.start_date,
            "due_date": self.due_date,
            "status": self.status
        }

#Add a method to input users files.
#After adding the input method, i creat a loop to validate the input and make sure that the user enters a valid project name etc. 
#Validate loop works by checking if the input is empty or not.
#I also added a dictionary allowed statuses to be sure that the user enters a valid status and to avoid laters errors in the code.

def input_project_details():
    while True:
        name = input("Enter project name: ").strip()
        if name:
            break
        print ("Project name cannot be empty. Please enter a valid name.")

    while True:    
        description = input("Enter project description: ").strip()      
        if description:
            break
        print("Project description cannot be empty. Please enter a valid description.")

#For the start_date and due_date, I used datetime.stiptime to validate the input and make sure that the user enters a valid date in the format MM/DD/YYYY.
#Also start_date and due_date are cheked by while look but with try and except to catch the ValueError exception if the user enters an invalid date.
    # Validate the start date and convert it into a datetime object.
# The datetime object will later be used to compare the start date with the due date.
    while True:
        start_date = input("Enter start date (MM/DD/YYYY): ").strip()

        try:
            start_date_object = datetime.strptime(start_date, "%m/%d/%Y")
            break
        except ValueError:
            print(
                "Invalid date. Use MM/DD/YYYY, "
                "for example 07/16/2026."
            )


    # Validate the due date and make sure it is later than the start date.
    while True:
        due_date = input("Enter due date (MM/DD/YYYY): ").strip()

        try:
            due_date_object = datetime.strptime(due_date, "%m/%d/%Y")

            # The project cannot finish before or on the same day it starts.
            if due_date_object <= start_date_object:
                print("Due date must be later than the start date.")
                continue

            break

        except ValueError:
            print(
                "Invalid date. Use MM/DD/YYYY, "
                "for example 09/30/2026."
            )
        allowed_statuses = {
                "not started": "Not Started",
                "active": "Active",
                "on hold": "On Hold",
                "completed": "Completed"
            }

    while True:
            status_input = input(
                "Enter status (Not Started, Active, On Hold, Completed): "
            ).strip().lower()

            if status_input in allowed_statuses:
                status = allowed_statuses[status_input]
                break

            print("Invalid status.")
    return Project(
        name,
        description,
        start_date,
        due_date,
        status
    )
def save_project_to_json(projects):
    projects_data=[]

    for project in projects:
        projects_data.append(project.to_dictionary())
    
    file_path = Path(__file__).parent / "projects.json"

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(projects_data, file, indent=4)


projects = []
project=input_project_details()
projects.append(project)

save_project_to_json(projects)

project.show_details()
print("\nProject details saved to projects.json.")

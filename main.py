# Create a project to manage tasks and deadlines around the project.
# First, create the Project class and use the __init__ method to initialize
# each project with a name, description, dates, and status.

from datetime import datetime
import json
from pathlib import Path


class Project:
    def __init__(self, name, description, start_date, due_date, status=None):
        self.name = name
        self.description = description
        self.start_date = start_date
        self.due_date = due_date
        self.status = status if status is not None else "Not Started"

    # Display the project details in a formatted way.
    def show_details(self):
        print("\n--- Project Details ---")
        print(f"Name: {self.name}")
        print(f"Description: {self.description}")
        print(f"Start date: {self.start_date}")
        print(f"Due date: {self.due_date}")
        print(f"Status: {self.status}")

    # Convert the project details into a dictionary for JSON storage.
    def to_dictionary(self):
        return {
            "name": self.name,
            "description": self.description,
            "start_date": self.start_date,
            "due_date": self.due_date,
            "status": self.status,
        }


# Collect project details and use loops to reject invalid input.
def input_project_details():
    while True:
        name = input("Enter project name: ").strip()
        if name:
            break
        print("Project name cannot be empty. Please enter a valid name.")

    while True:
        description = input("Enter project description: ").strip()
        if description:
            break
        print("Project description cannot be empty. Please enter a valid description.")

    # Use datetime.strptime to validate dates entered in MM/DD/YYYY format.
    while True:
        start_date = input("Enter start date (MM/DD/YYYY): ").strip()

        try:
            start_date_object = datetime.strptime(start_date, "%m/%d/%Y")
            break
        except ValueError:
            print("Invalid date. Use MM/DD/YYYY, for example 07/20/2026.")

    # The due date must be strictly later than the start date.
    while True:
        due_date = input("Enter due date (MM/DD/YYYY): ").strip()

        try:
            due_date_object = datetime.strptime(due_date, "%m/%d/%Y")
            if due_date_object <= start_date_object:
                print("Due date must be later than the start date.")
                continue
            break
        except ValueError:
            print("Invalid date. Use MM/DD/YYYY, for example 09/30/2026.")

    allowed_statuses = {
        "not started": "Not Started",
        "active": "Active",
        "on hold": "On Hold",
        "completed": "Completed",
    }

    while True:
        status_input = input(
            "Enter status (Not Started, Active, On Hold, Completed): "
        ).strip().lower()

        if status_input in allowed_statuses:
            status = allowed_statuses[status_input]
            break

        print("Invalid status.")

    return Project(name, description, start_date, due_date, status)


def save_project_to_json(projects):
    projects_data = []

    for project in projects:
        projects_data.append(project.to_dictionary())

    file_path = Path(__file__).parent / "projects.json"

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(projects_data, file, indent=4)


projects = []
project = input_project_details()
projects.append(project)

save_project_to_json(projects)

project.show_details()
print("\nProject details saved to projects.json.")

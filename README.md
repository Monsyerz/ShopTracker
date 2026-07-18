# ShopFlow

ShopFlow is a beginner-friendly Python project created to manage projects, deadlines, statuses, and project-related tasks.

The application is currently being developed as a command-line program. Its purpose is to help users create projects, validate project information, display project details, and eventually store project data permanently.

This project is also part of my Python learning journey. I am building it step by step, starting with core Python concepts and gradually introducing file storage, databases, testing, APIs, and deployment.

## Current Features

* Create a new project
* Enter a project name and description
* Enter a project start date
* Enter an expected completion date
* Assign a project status
* Validate empty project names and descriptions
* Validate dates in the `MM/DD/YYYY` format
* Validate project statuses
* Display formatted project details
* Convert project objects into dictionaries for future JSON storage

## Project Information

Each project currently contains:

* Project name
* Project description
* Start date
* Due date
* Status

Available project statuses:

* `Not Started`
* `Active`
* `On Hold`
* `Completed`

## Technologies

* Python
* Python `datetime` module
* JSON storage — currently being implemented

Future versions will also use:

* SQLite
* SQL
* pytest
* FastAPI
* PostgreSQL
* Docker

## Current Project Structure

```text
shopflow/
├── main.py
├── README.md
└── TODO.md
```

The project structure will be expanded as new features are added.

## How to Run the Project

Make sure Python is installed on your computer.

Clone the repository:

```bash
git clone https://github.com/Monsyerz/ShopTracker.git
```

Open the project directory:

```bash
cd shopflow
```

Run the application:

```bash
python main.py
```

The program will ask you to enter project information through the console.

## Example

```text
Enter project name: 27 Bridge Street
Enter project description: Glass vestibule installation
Enter start date (MM/DD/YYYY): 07/17/2026
Enter due date (MM/DD/YYYY): 09/30/2026
Enter status (Not Started, Active, On Hold, Completed): Active

--- Project Details ---
Name: 27 Bridge Street
Description: Glass vestibule installation
Start date: 07/17/2026
Due date: 09/30/2026
Status: Active
```

## Development Roadmap

Planned features include:

* Support for multiple projects
* Main application menu
* Saving projects to a JSON file
* Loading projects when the program starts
* Editing existing projects
* Deleting projects
* Unique project IDs
* Project tasks and deadlines
* SQLite database integration
* Automated tests
* REST API built with FastAPI
* PostgreSQL database
* Docker support
* Application deployment

More detailed development progress is available in [`TODO.md`](TODO.md).

## Learning Goals

This project is designed to help me practice:

* Python classes and objects
* Functions and methods
* Loops and conditional statements
* User input validation
* Exception handling
* Lists and dictionaries
* Reading and writing JSON files
* Object-oriented programming
* SQL and database integration
* Automated testing
* Backend API development

## Project Status

ShopFlow is currently under active development.

The first version focuses on creating and validating individual projects through the command line. Future versions will introduce persistent storage, multiple projects, tasks, and database integration.

## Author

Created as a Python portfolio and learning project.

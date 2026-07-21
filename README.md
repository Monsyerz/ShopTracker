# ShopTracker

ShopTracker is a beginner-friendly command-line Python project for creating one project per program run and recording its name, description, dates, and status.

This project is part of my Python learning journey. It is being built step by step, starting with core Python concepts.

## Current Features

* Create one project per run
* Validate project names and descriptions
* Validate dates in the `MM/DD/YYYY` format
* Require the due date to be later than the start date
* Validate project statuses
* Display formatted project details
* Save project details to `projects.json`

Available project statuses are `Not Started`, `Active`, `On Hold`, and `Completed`.

Dates are stored as `MM/DD/YYYY` strings in the project and JSON file.

## Project Structure

```text
ShopTracker/
|-- main.py
|-- projects.example.json
|-- README.md
`-- TODO.md
```

The generated `projects.json` file is stored beside `main.py` and is ignored by Git.

## How to Run the Project

Make sure Python is installed, clone the repository, and open the project directory:

```bash
git clone https://github.com/Monsyerz/ShopTracker.git
cd ShopTracker
```

Run the application:

```bash
python main.py
```

## Example

```text
Enter project name: Harbor Point Offices
Enter project description: 145 Harbor Avenue, Brooklyn, NY
Enter start date (MM/DD/YYYY): 07/20/2026
Enter due date (MM/DD/YYYY): 09/30/2026
Enter status (Not Started, Active, On Hold, Completed): Active

--- Project Details ---
Name: Harbor Point Offices
Description: 145 Harbor Avenue, Brooklyn, NY
Start date: 07/20/2026
Due date: 09/30/2026
Status: Active
```

## Roadmap

Future work is tracked in [`TODO.md`](TODO.md). Multiple-project support, menus, JSON loading, editing, deleting, IDs, tasks, databases, tests, APIs, and deployment are not implemented yet.

## Learning Goals

ShopTracker currently practices Python classes, functions, loops, input validation, exception handling, lists, dictionaries, and JSON writing.

## Project Status

ShopTracker is under active development. The current version creates one project per run, validates its details, displays them, and saves them to JSON.

## Author

Created as a Python portfolio and learning project.

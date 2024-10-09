# Task Manager CLI

A simple command-line interface (CLI) application for managing tasks. You can add, update, delete, mark tasks with statuses, and list them with structured output in the terminal.

[Project Reference: Task Tracker](https://roadmap.sh/projects/task-tracker)

## Table of Contents

- [Features](#features)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Command Examples with Output](#command-examples-with-output)

## Features

- Add new tasks with a description.
- Update task descriptions.
- Delete tasks by ID.
- Mark tasks as "in-progress" or "done."
- List tasks, filtered by their status.
- All tasks are stored in a `tasks.json` file locally.

## Setup and Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/SonaVarshney/task-manager-cli
cd task-manager-cli
```

### Step 2: Install Dependencies

Ensure you have Python installed on your machine. Then, install any required libraries (in this case, none are required beyond Python's built-in libraries).

```bash
python --version  # Should return Python 3.x.x
```

### Step 3: Run the Project

You can run the CLI app by invoking `python` in the terminal:

```bash
python task_manager.py --help
```

## Usage

Here are the commands you can use to interact with the task manager:

1. **Add a Task**
2. **Update a Task**
3. **Delete a Task**
4. **Mark a Task as In-Progress or Done**
5. **List Tasks (Filtered by Status)**

### Basic Command Structure

```bash
python task_manager.py <command> [arguments]
```

## Command Examples with Output

### 1. Add a Task

To add a new task with a description:

```bash
python task_manager.py add "Finish the project report"
```

#### Output:

```bash
Task added successfully (ID: 1)
```

### 2. Update a Task

To update the description of an existing task:

```bash
python task_manager.py update 1 "Submit the project report"
```

#### Output:

```bash
Task 1 updated successfully.
```

### 3. Delete a Task

To delete a task by its ID:

```bash
python task_manager.py delete 1
```

#### Output:

```bash
Task 1 deleted successfully.
```

### 4. Mark a Task as In-Progress

To mark a task as "in-progress":

```bash
python task_manager.py mark-in-progress 1
```

#### Output:

```bash
Task 1 marked as in-progress.
```

### 5. Mark a Task as Done

To mark a task as "done":

```bash
python task_manager.py mark-done 1
```

#### Output:

```bash
Task 1 marked as done.
```

### 6. List Tasks

To list all tasks:

```bash
python task_manager.py list
```

#### Output:

```bash
ID    | Description                 | Status       | Created At           | Updated At           
----------------------------------------------------------------------------------------------------
1     | Submit the project report    | in-progress  | 2024-10-09 15:23:45  | 2024-10-09 16:05:12  
2     | Buy groceries                | todo         | 2024-10-09 15:25:21  | 2024-10-09 15:25:21
```

To list tasks filtered by status:

```bash
python task_manager.py list done
```

#### Output:

```bash
ID    | Description                 | Status       | Created At           | Updated At           
----------------------------------------------------------------------------------------------------
1     | Submit the project report    | done         | 2024-10-09 15:23:45  | 2024-10-09 16:05:12  
```

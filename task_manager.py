import argparse
import json
import os
from datetime import datetime

# Define constants
TASK_FILE = "tasks.json"
DEFAULT_STATUS = "todo"


# Helper functions for file handling
def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            tasks = json.load(file)
            if tasks:
                max_id = max(int(task_id) for task_id in tasks.keys())
                return tasks, max_id
    return (
        {},
        0,
    )  # Return an empty dictionary and 0 as the max_id if no tasks are present


def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


# Task management functions
def add_task(description):
    tasks, max_id = load_tasks()
    task_id = str(max_id + 1)  # Increment the max ID by 1
    task = {
        "id": task_id,
        "description": description,
        "status": DEFAULT_STATUS,
        "createdAt": str(datetime.now()),
        "updatedAt": str(datetime.now()),
    }
    tasks[task_id] = task  # Use the string ID as the key
    save_tasks(tasks)
    print(f"Task added successfully (ID: {task_id})")


def update_task(task_id, new_description):
    tasks, _ = load_tasks()
    task = tasks.get(str(task_id))  # Convert task_id to string for lookup
    if task:
        task["description"] = new_description
        task["updatedAt"] = str(datetime.now())
        save_tasks(tasks)
        print(f"Task {task_id} updated successfully.")
    else:
        print(f"Task {task_id} not found.")


def delete_task(task_id):
    tasks, _ = load_tasks()
    if str(task_id) in tasks:  # Convert task_id to string for lookup
        del tasks[str(task_id)]
        save_tasks(tasks)
        print(f"Task {task_id} deleted successfully.")
    else:
        print(f"Task {task_id} not found.")


def mark_task(task_id, status):
    tasks, _ = load_tasks()
    task = tasks.get(str(task_id))  # Convert task_id to string for lookup
    if task:
        task["status"] = status
        task["updatedAt"] = str(datetime.now())
        save_tasks(tasks)
        print(f"Task {task_id} marked as {status}.")
    else:
        print(f"Task {task_id} not found.")


def list_tasks(status=None):
    tasks, _ = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    print(
        "ID    | Description                    | Status       | Created At           | Updated At"
    )
    print("-" * 100)
    for task in tasks.values():
        if status is None or task["status"] == status:
            print(
                f"{task['id']: <5} | {task['description']: <30} | {task['status']: <12} | {task['createdAt']} | {task['updatedAt']}"
            )


# Command-line interface
def main():
    parser = argparse.ArgumentParser(description="Task Management CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Add a task
    parser_add = subparsers.add_parser("add", help="Add a new task")
    parser_add.add_argument("description", type=str, help="Description of the task")

    # Update a task
    parser_update = subparsers.add_parser("update", help="Update a task description")
    parser_update.add_argument("id", type=int, help="ID of the task to update")
    parser_update.add_argument(
        "description", type=str, help="New description of the task"
    )

    # Delete a task
    parser_delete = subparsers.add_parser("delete", help="Delete a task")
    parser_delete.add_argument("id", type=int, help="ID of the task to delete")

    # Mark a task as in-progress
    parser_mark_in_progress = subparsers.add_parser(
        "mark-in-progress", help="Mark a task as in-progress"
    )
    parser_mark_in_progress.add_argument(
        "id", type=int, help="ID of the task to mark as in-progress"
    )

    # Mark a task as done
    parser_mark_done = subparsers.add_parser("mark-done", help="Mark a task as done")
    parser_mark_done.add_argument("id", type=int, help="ID of the task to mark as done")

    # List tasks
    parser_list = subparsers.add_parser("list", help="List tasks")
    parser_list.add_argument(
        "status",
        nargs="?",
        choices=["todo", "in-progress", "done"],
        help="Status of tasks to list",
    )

    # Parse the arguments
    args = parser.parse_args()

    # Execute the appropriate function based on the command
    if args.command == "add":
        add_task(args.description)
    elif args.command == "update":
        update_task(args.id, args.description)
    elif args.command == "delete":
        delete_task(args.id)
    elif args.command == "mark-in-progress":
        mark_task(args.id, "in-progress")
    elif args.command == "mark-done":
        mark_task(args.id, "done")
    elif args.command == "list":
        list_tasks(args.status)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

# Todo Task Planner 🚀

This is a mini project for practicing object-oriented programming in Python. The app helps you plan and manage tasks by setting a task name, start date, duration, description, location, and status.

## Features ✨

- **Task Creation:** Create tasks with built-in data validation (name, start date, duration).
- **Task Status:** Manage task statuses (`New`, `In Progress`, `Completed`, `Failed`) using an `Enum`.
- **Status Toggling:** Easily toggle a task's status with the `toggle_status()` method.
- **Task List Management:**
  - Shift all tasks by one day.
  - Search for tasks by name or description.
  - Filter tasks using multiple criteria (status, location, date range).
  - Sort tasks by a specified property.

## Project Structure 📁

- **`status_enum.py`**  
  Defines the available task statuses using Python's `Enum`.

- **`task.py`**  
  Contains the `Task` class which represents an individual task. It uses data descriptors for validating properties (e.g., name, start date, duration) and includes a `toggle_status()` method.

- **`task_list.py`**  
  Contains the `TaskList` class for managing a collection of tasks. It provides functionality for filtering, sorting, searching, and modifying the status of multiple tasks at once.

## Notes 📝

- **Start Date:** Must be at least **15 minutes** in the future.  
- **Duration:** Each task must last at least **15 minutes**.  
- **Data Validation:** The `Task` class ensures that the provided information is **valid**, reducing potential runtime errors.  

## Object Descriptors 🏗️  

The `Task` class utilizes **object descriptors** to manage attribute validation dynamically. Descriptors help ensure that:  

- The **title** is a non-empty string.  
- The **start_time** is a valid `datetime` object and is at least **15 minutes in the future**.  
- The **duration** is an integer and at least **15 minutes** long.  
- The **location** and **description** (if provided) are strings and properly formatted.  

Using descriptors enhances **encapsulation, validation, and maintainability** of the `Task` class, ensuring safer data handling.  

---

🛠 **Author:** [Piotr Lipinski]  
📅 **Last Updated:** February 2025  

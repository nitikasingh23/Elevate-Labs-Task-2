# Elevate-Labs-Task-2

# 📋 To-Do List Application (Console-based)

A simple yet fully functional command-line To-Do List manager built with Python. Tasks are **saved automatically to a text file** so they persist even after you close the app. Built as part of a Python CLI mini-task series.

---

## 📌 Features

| Feature | Description |
|---|---|
| ➕ Add Task | Add any task by typing its description |
| 👁️ View Tasks | See all tasks with numbered index |
| 🗑️ Remove Task | Delete a specific task by number |
| ✔️ Mark as Done | Mark tasks complete with a `[DONE]` tag |
| 🧹 Clear All | Wipe all tasks at once (with confirmation) |
| 💾 Auto-Save | Tasks saved to `tasks.txt` automatically |
| ⚠️ Error Handling | Handles empty input, bad numbers, missing file |

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python 3 | Core language |
| `open()` / File I/O | Persistent task storage in `tasks.txt` |
| VS Code | Code editor |
| Terminal | Running the app |

---

## 🚀 How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/todo-cli.git
cd todo-cli
```

### 2. Run the Script
```bash
python todo.py
```

> ✅ No external libraries needed — uses only built-in Python!  
> 📁 A `tasks.txt` file will be created automatically in the same folder.

---

## 🖥️ Sample Output

```
=============================================
  👋  Welcome to the To-Do List App!
      Your tasks are saved automatically.
=============================================

─────────────────────────────────────────────
  📌  MENU
─────────────────────────────────────────────
  1️⃣   View Tasks
  2️⃣   Add Task
  3️⃣   Remove Task
  4️⃣   Mark Task as Done
  5️⃣   Clear All Tasks
  6️⃣   Exit
─────────────────────────────────────────────
  👉  Enter your choice (1-6): 2

  ✏️  Enter task description: Complete Python Assignment
  ✅  Task added: "Complete Python Assignment"

  👉  Enter your choice (1-6): 1

=============================================
         📋  YOUR TO-DO LIST
=============================================
   1. 🔲  Complete Python Assignment
   2. 🔲  Push code to GitHub
=============================================
```

---

## 📂 Project Structure

```
todo-cli/
│
├── todo.py       # Main Python script
├── tasks.txt     # Auto-generated task storage file
└── README.md     # Project documentation
```

---

## 💡 What I Did — Step-by-Step Explanation

### 🔹 1. Used a List to Store Tasks
Tasks are loaded into a Python **list** at startup and all operations (add, remove, mark done) work on this list in memory.

```python
tasks = load_tasks()  # Returns a Python list like ["Buy milk", "Study Python"]
```

---

### 🔹 2. File Persistence with `open()`

Tasks are saved to and loaded from a plain text file (`tasks.txt`) using Python's built-in `open()` function.

**Loading tasks (on startup):**
```python
def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            tasks = [line.strip() for line in f.readlines() if line.strip()]
        return tasks
    except FileNotFoundError:
        return []  # Start fresh if file doesn't exist
```
- `"r"` mode = read the file
- `line.strip()` = removes newline characters from each line
- `FileNotFoundError` is caught so the app doesn't crash on first run

**Saving tasks (after every change):**
```python
def save_tasks(tasks):
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")
```
- `"w"` mode = overwrites the file with the current list every time a change is made
- Each task is written on its own line

---

### 🔹 3. Add / Remove / View Functionality

**Add Task** — uses `list.append()`:
```python
def add_task(tasks):
    task = input("Enter task: ").strip()
    tasks.append(task)
    save_tasks(tasks)
```

**View Tasks** — uses `enumerate()` for numbered display:
```python
def view_tasks(tasks):
    for i, task in enumerate(tasks, start=1):
        print(f"  {i}. {task}")
```

**Remove Task** — uses `list.pop()` with index:
```python
def remove_task(tasks):
    num = int(input("Enter task number to remove: "))
    removed = tasks.pop(num - 1)  # list is 0-indexed, menu is 1-indexed
    save_tasks(tasks)
```

---

### 🔹 4. Mark as Done
Instead of deleting a task, it **prefixes** it with `[DONE]` so you can still see what you completed:

```python
def mark_done(tasks):
    tasks[num - 1] = "[DONE] " + tasks[num - 1]
    save_tasks(tasks)
```

---

### 🔹 5. Input Validation and Error Handling
- `try/except ValueError` — catches non-number input when asking for task numbers
- Empty string check — prevents adding blank tasks
- Range check — validates the task number is within the list bounds
- `FileNotFoundError` — gracefully handles missing `tasks.txt` on first run

---

### 🔹 6. `while True` Loop + Menu
The app keeps running in a loop, showing the menu each time, and only exits when the user picks option **6**.

```python
while True:
    show_menu()
    choice = input("Enter choice: ")
    if choice == '6':
        break
```

---

## 🧠 Key Python Concepts Used

| Concept | Where Used |
|---|---|
| `list` | Storing all tasks in memory |
| `open()` with `"r"` / `"w"` | Reading and writing `tasks.txt` |
| `append()`, `pop()` | Adding and removing tasks |
| `enumerate()` | Numbered task display |
| `try / except` | Handling bad input and missing file |
| `while True` + `break` | Main app loop |
| `strip()` | Cleaning user input and file lines |
| `f-strings` | Formatted terminal output |

---



---

## 📄 License

Open source — free to use for learning and personal projects.

# ============================================
#       To-Do List Application (Console)
#       Built with Python 🐍
# ============================================

TODO_FILE = "tasks.txt"

# ─── File Operations ────────────────────────

def load_tasks():
    """Load tasks from the text file into a list."""
    try:
        with open(TODO_FILE, "r") as f:
            tasks = [line.strip() for line in f.readlines() if line.strip()]
        return tasks
    except FileNotFoundError:
        return []  # If file doesn't exist yet, start fresh

def save_tasks(tasks):
    """Save the current task list back to the text file."""
    with open(TODO_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

# ─── Core Functions ─────────────────────────

def view_tasks(tasks):
    """Display all tasks with their index numbers."""
    print("\n" + "=" * 45)
    print("         📋  YOUR TO-DO LIST")
    print("=" * 45)
    if not tasks:
        print("  ✅  No tasks yet! Add something to do.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"  {i:>2}. 🔲  {task}")
    print("=" * 45)

def add_task(tasks):
    """Add a new task to the list."""
    task = input("\n  ✏️  Enter task description: ").strip()
    if task == "":
        print("  ⚠️  Task cannot be empty!")
        return
    tasks.append(task)
    save_tasks(tasks)
    print(f"  ✅  Task added: \"{task}\"")

def remove_task(tasks):
    """Remove a task by its number."""
    view_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("\n  🗑️  Enter task number to remove: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"  ✅  Removed: \"{removed}\"")
        else:
            print(f"  ⚠️  Invalid number! Enter between 1 and {len(tasks)}.")
    except ValueError:
        print("  ⚠️  Please enter a valid number.")

def mark_done(tasks):
    """Mark a task as done (adds ✔ prefix)."""
    view_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("\n  ✔️  Enter task number to mark as done: "))
        if 1 <= num <= len(tasks):
            if tasks[num - 1].startswith("[DONE] "):
                print("  ℹ️  Task is already marked as done!")
            else:
                tasks[num - 1] = "[DONE] " + tasks[num - 1]
                save_tasks(tasks)
                print(f"  ✅  Marked as done: \"{tasks[num - 1]}\"")
        else:
            print(f"  ⚠️  Invalid number! Enter between 1 and {len(tasks)}.")
    except ValueError:
        print("  ⚠️  Please enter a valid number.")

def clear_all_tasks(tasks):
    """Clear all tasks after confirmation."""
    if not tasks:
        print("\n  ℹ️  No tasks to clear.")
        return
    confirm = input("\n  ⚠️  Are you sure you want to clear ALL tasks? (yes/no): ").strip().lower()
    if confirm == "yes":
        tasks.clear()
        save_tasks(tasks)
        print("  ✅  All tasks cleared!")
    else:
        print("  ↩️  Cancelled.")

# ─── Menu ───────────────────────────────────

def show_menu():
    """Display the main menu."""
    print("\n" + "─" * 45)
    print("  📌  MENU")
    print("─" * 45)
    print("  1️⃣   View Tasks")
    print("  2️⃣   Add Task")
    print("  3️⃣   Remove Task")
    print("  4️⃣   Mark Task as Done")
    print("  5️⃣   Clear All Tasks")
    print("  6️⃣   Exit")
    print("─" * 45)

# ─── Main ───────────────────────────────────

def main():
    print("\n" + "=" * 45)
    print("  👋  Welcome to the To-Do List App!")
    print("      Your tasks are saved automatically.")
    print("=" * 45)

    tasks = load_tasks()  # Load existing tasks from file on startup

    while True:
        show_menu()
        choice = input("  👉  Enter your choice (1-6): ").strip()

        if   choice == '1': view_tasks(tasks)
        elif choice == '2': add_task(tasks)
        elif choice == '3': remove_task(tasks)
        elif choice == '4': mark_done(tasks)
        elif choice == '5': clear_all_tasks(tasks)
        elif choice == '6':
            print("\n  👋  Goodbye! Stay productive! 💪\n")
            break
        else:
            print("  ⚠️  Invalid choice! Please enter 1–6.")

if __name__ == "__main__":
    main()

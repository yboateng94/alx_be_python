# daily_reminder.py

# Prompt the user for a single task description
task = input("Enter your task: ")

# Prompt for the task's priority
priority = input("Enter the priority of the task (high, medium, low): ").strip().lower()

# Ask if the task is time-bound
time_bound = input("Is the task time-bound? (yes or no): ").strip().lower()


# Process the task based on priority and time sensitivity
def generate_reminder(task, priority, time_bound):
    match priority:
        case 'high':
            reminder = f"Task: {task} (Priority: High)"
        case 'medium':
            reminder = f"Task: {task} (Priority: Medium)"
        case 'low':
            reminder = f"Task: {task} (Priority: Low)"
        case _:
            reminder = "Invalid priority entered. Please use 'high', 'medium', or 'low'."
            return reminder

    if time_bound == 'yes' and priority in ['high', 'medium', 'low']:
        reminder += " - that requires immediate attention today!"

    return reminder


# Generate and display the customized reminder
customized_reminder = generate_reminder(task, priority, time_bound)
print(customized_reminder)

def daily_reminder():
    # Prompt for task details
    task = input("Enter the task description: ")
    priority = input("Enter the task priority (high, medium, low): ").lower()
    time_bound = input("Is the task time-bound? (yes or no): ").lower()

    # Process based on priority
    match priority:
        case "high":
            reminder = f"Task: {task} (Priority: High) - Ensure this task is handled urgently."
        case "medium":
            reminder = f"Task: {task} (Priority: Medium) - Address this task soon."
        case "low":
            reminder = f"Task: {task} (Priority: Low) - This task can wait."
        case _:
            reminder = f"Task: {task} (Priority: Unknown) - Please review the priority."

    # Check if the task is time-bound
    if time_bound == "yes":
        reminder += " This task requires immediate attention today!"

    # Print the customized reminder
    print(reminder)

# Run the function
if __name__ == "__main__":
    daily_reminder()

def daily_reminder():
    # Prompt for task details
    task = input("Enter the task description: ")
    priority = input("Enter the task priority (high/medium/low): ")
    time_bound = input("Is the task time-bound? (yes/no): ")

    # Process based on priority
    match priority:
        case "high":
            reminder = f"Task: {task} (Priority: High)"
        case "medium":
            reminder = f"Task: {task} (Priority: Medium) - Address this task soon."
        case "low":
            reminder = f"Task: {task} (Priority: Low) - Consider completing it when you have free time."
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

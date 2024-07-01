# daily_reminder.py

# Prompt for a single task
task = input("Enter your task: ")

# Prompt for the task's priority
priority = input("Priority (high/medium/low): ").lower()

# Prompt for the time sensitivity of the task
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task based on priority and time sensitivity
reminder = f"'{task}' is a {priority} priority task."

match priority:
    case 'high':
        if time_bound == 'yes':
            reminder += " It requires immediate attention today!"
        else:
            reminder += " Make sure to complete it as soon as possible."
    case 'medium':
        if time_bound == 'yes':
            reminder += " Try to complete it soon."
        else:
            reminder += " Plan to complete it in the next few days."
    case 'low':
        if time_bound == 'yes':
            reminder += " It's time-bound, but not urgent."
        else:
            reminder += " Consider completing it when you have free time."
    case _:
        reminder = "Invalid priority entered."

# Print the customized reminder
print("Reminder:", reminder)

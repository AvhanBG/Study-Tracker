from session_manager import SessionManager
from stats_engine import Stats
from storage import Storage

storage = Storage()
manager = SessionManager()

def menu():
    print("\nStudy Tracker")
    print("1. Start a study session")
    print("2. End a study session")
    print("3. View statistics")
    print("4. Exit")

while True:
    menu()
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a number.")
        continue

    if choice == 1:
        manager.start_session()
        print("Session started")

    elif choice == 2:
        completed_session = manager.end_session()
        print("Session ended")
        if completed_session:
            storage.save_session(completed_session)
            print("Session saved")
        else:
            print("No active session")

    elif choice == 3:
        sessions = storage.load_sessions()
        stats = Stats(sessions)
        print(f"Daily total: {stats.daily_total()} minutes.")
        print(f"Weekly total: {stats.weekly_total()} minutes.")
        print(f"Average session: {stats.average_session()} minutes.")
        print(f"Current streak: {stats.calculate_streak()} days.")

    elif choice == 4:
        print("Exiting...")
        break
    else:
        print("Invalid choice!")

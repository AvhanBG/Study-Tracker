from datetime import datetime
from study_session import StudySession

class SessionManager:

    def __init__(self):
        self.current_session = None
        self.next_id = 1

    def start_session(self):
        self.current_session = StudySession(self.next_id)
        self.current_session.start_time = datetime.now()
        self.current_session.date = self.current_session.start_time.date()

    def end_session(self):
        if self.current_session is None:
            print("No active session")
            return None

        self.current_session.end_time = datetime.now()
        self.current_session.calculate_duration()
        completed_session = self.current_session
        self.current_session = None
        return completed_session
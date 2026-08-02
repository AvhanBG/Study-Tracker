import math

class StudySession:

    def __init__(self, session_id):
        self.id = session_id
        self.start_time = None
        self.end_time = None
        self.duration_minutes = 0
        self.date = None

    def calculate_duration(self):
        elapsed = self.end_time - self.start_time
        minutes = elapsed.total_seconds() / 60
        self.duration_minutes = math.ceil(minutes)

    def get_duration(self):
        return {
            "id": self.id,
            "date": str(self.date),
            "start_time": str(self.start_time),
            "end_time": str(self.end_time),
            "duration_minutes": self.duration_minutes,
        }
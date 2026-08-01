from datetime import datetime, date, timedelta

class Stats:

    def __init__(self, sessions):
        self.sessions = sessions

    def daily_total(self):
        today = datetime.now().date()
        total = 0
        for session in self.sessions:
            if session.date() == today:
                total += session.daily_total()
        return total

    def weekly_total(self):
        today = date.today()
        week_start = today - timedelta(days=6)
        total = 0
        for session in self.sessions:
            if week_start <= session.date <= today:
                total += session.duration_minutes
        return total

    def average_session(self):
        if len(self.sessions) == 0:
            return 0
        total = 0
        for session in self.sessions:
            total += session.duration_minutes
        return total / len(self.sessions)

    def calculate_streak(self):
        dates = []
        for session in self.sessions:
            dates.append(session.date())
        if len(dates) == 0:
            return 0
        dates = list(set(dates))
        dates.sort(reverse=True)
        if dates[0] != date.today():
            return 0
        streak = 1
        for i in range(len(dates)-1):
            if dates[i] - dates[i+1] == timedelta(days=1):
                streak += 1
            else:
                break
        return streak
from datetime import datetime

class SecurityReport:
    def __init__(self, guard_name: str, description: str):
        self.guard_name = guard_name
        self.description = description
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    def __str__(self):
        return f"[{self.timestamp}] Report by {self.guard_name}: {self.description}"

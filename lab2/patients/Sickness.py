class Sickness:
    def __init__(self, name: str, symptoms: list[str], severity: str):
        self.name = name
        self.symptoms = symptoms
        self.severity = severity  

    def __str__(self):
        return f"{self.name} ({self.severity}) — Symptoms: {', '.join(self.symptoms)}"

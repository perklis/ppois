class Analysis:
    def __init__(self, analysis_type: str, result: str, doctor_name: str, date: str):
        self.analysis_type = analysis_type
        self.result = result
        self.doctor_name = doctor_name
        self.date = date

    def __str__(self):
        return f"{self.analysis_type} on {self.date}: {self.result} (by {self.doctor_name})"

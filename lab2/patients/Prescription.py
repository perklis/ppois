class Prescription:
    def __init__(self, medication_name: str, dosage: str, duration: str, doctor_name: str):
        self.medication_name = medication_name
        self.dosage = dosage
        self.duration = duration
        self.doctor_name = doctor_name

    def __str__(self):
        return f"{self.medication_name} ({self.dosage}, {self.duration}) — prescribed by {self.doctor_name}"

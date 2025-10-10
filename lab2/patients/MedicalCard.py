# from Patient import Patient
# from MedicalCardGenerator import MedicalCardGenerator

# class MedicalCard:
#     def __init__(self, patient: Patient, generator_of_number=None):
#         self.patient = patient
#         if generator_of_number is None:
#             generator_of_number = MedicalCardGenerator()

#         self.card_number = generator_of_number.generate(
#             birth_year=patient.birth_year if hasattr(patient, 'birth_year') else None
#         )
#         self.visits = []
#         self.allergies = []
    
#     def add_visit(self, date: str, doctor: str, diagnosis: str, prescriptions=None):
#         self.visits.append({
#             "date": date,
#             "doctor": doctor,
#             "diagnosis": diagnosis,
#             "prescriptions": prescriptions or []
#         })
    
#     def get_visits(self):
#         return self.visits

#     def add_allergy(self, allergy: str):
#         self.allergies.append(allergy)

#     def get_info(self) -> str:
#         return (f"Medical Card: {self.card_number}\nPatient: {self.patient.name}\n"
#                 f"Allergies: {', '.join(self.allergies) if self.allergies else 'None'}\n"
#                 f"Amount of visits: {len(self.visits)}\n")
    
from patients.MedicalCardGenerator import MedicalCardGenerator
from patients.Prescription import Prescription
from patients.Sickness import Sickness
from patients.Analysis import Analysis

class MedicalCard:
    def __init__(self, patient_name: str, birth_year: int, generator: MedicalCardGenerator | None = None):
        self.patient_name = patient_name
        self.birth_year = birth_year
        self.generator = generator or MedicalCardGenerator()
        self.card_number = self.generator.generate(birth_year)
        
        self.visits: list[dict] = []
        self.allergies: list[str] = []
        self.prescriptions: list[Prescription] = []
        self.sicknesses: list[Sickness] = []
        self.analyses: list[Analysis] = []

    def add_visit(self, date: str, doctor: str, diagnosis: str, prescriptions: list[Prescription] | None = None):
        self.visits.append({
            "date": date,
            "doctor": doctor,
            "diagnosis": diagnosis,
            "prescriptions": prescriptions or []
        })

    def add_allergy(self, allergy: str):
        self.allergies.append(allergy)

    def add_prescription(self, prescription: Prescription):
        self.prescriptions.append(prescription)

    def add_sickness(self, sickness: Sickness):
        self.sicknesses.append(sickness)

    def add_analysis(self, analysis: Analysis):
        self.analyses.append(analysis)

    def get_visits(self):
        return self.visits

    def get_info(self) -> str:
        return (
            f"Medical Card: {self.card_number}\n"
            f"Patient: {self.patient_name}\n"
            f"Allergies: {', '.join(self.allergies) if self.allergies else 'None'}\n"
            f"Visits: {len(self.visits)}\n"
            f"Sicknesses: {len(self.sicknesses)}\n"
            f"Prescriptions: {len(self.prescriptions)}\n"
            f"Analyses: {len(self.analyses)}"
        )

    def __str__(self):
        return self.get_info()


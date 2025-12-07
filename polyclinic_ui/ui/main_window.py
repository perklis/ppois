from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt
from .doctor_login_window import DoctorLoginWindow
from .patient_login_window import PatientLoginWindow

class MainWindow(QWidget):
    def __init__(self, doctors, appointments, patients_records):
        super().__init__()
        self.setWindowTitle("Поликлиника — Выбор роли")
        self.doctors = doctors
        self.appointments = appointments
        self.patients_records = patients_records
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        title_btn = QPushButton("🏥 Добро пожаловать в поликлинику!\n\nВыберите свою роль")
        title_btn.setStyleSheet("font-size: 32px; padding: 50px; color: #333;")
        title_btn.setEnabled(False)

        doctor_btn = QPushButton("👨‍⚕️ Доктор")
        doctor_btn.setStyleSheet("font-size: 28px; padding: 30px; background-color: #4CAF50; color: white; border-radius: 10px;")
        doctor_btn.clicked.connect(self.open_doctor_login)

        patient_btn = QPushButton("🧑‍🦽 Пациент")
        patient_btn.setStyleSheet("font-size: 28px; padding: 30px; background-color: #03A9F4; color: white; border-radius: 10px;")
        patient_btn.clicked.connect(self.open_patient_login)

        exit_btn = QPushButton("❌ Выйти")
        exit_btn.setStyleSheet("font-size: 26px; padding: 25px; background-color: #f44336; color: white; border-radius: 10px;")
        exit_btn.clicked.connect(self.close)

        for button in [title_btn, doctor_btn, patient_btn, exit_btn]:
            layout.addWidget(button)

        self.setLayout(layout)

    def open_doctor_login(self):
        self.doctor_login = DoctorLoginWindow(self)
        self.doctor_login.showFullScreen()
        self.hide()

    def open_patient_login(self):
        self.patient_login = PatientLoginWindow(self, self.doctors, self.appointments, self.patients_records)
        self.patient_login.showFullScreen()
        self.hide()

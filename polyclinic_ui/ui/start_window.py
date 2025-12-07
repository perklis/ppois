from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from ui.doctor_login_window import DoctorLoginWindow
from ui.patient_login_window import PatientLoginWindow
from ui.pharmacist_login_window import PharmacistLoginWindow
from ui.registrar_login_window import RegistrarLoginWindow

class StartWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Поликлиника — Выбор роли")
        self.showMaximized()

        layout = QVBoxLayout()
        layout.setSpacing(30)

        label = QLabel("Добро пожаловать в поликлинику!\nВыберите свою роль:")
        label.setFont(QFont("Arial", 32))
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

        #доктор
        doctor_btn = QPushButton("Доктор")
        doctor_btn.setFont(QFont("Arial", 24))
        doctor_btn.setStyleSheet("background-color:#4CAF50; color:white; padding:20px; border-radius:10px;")
        doctor_btn.clicked.connect(self.open_doctor)
        layout.addWidget(doctor_btn)

        #пациент
        patient_btn = QPushButton("Пациент")
        patient_btn.setFont(QFont("Arial", 24))
        patient_btn.setStyleSheet("background-color:#03A9F4; color:white; padding:20px; border-radius:10px;")
        patient_btn.clicked.connect(self.open_patient)
        layout.addWidget(patient_btn)

        #аптекарь
        pharmacist_btn = QPushButton("Аптекарь")
        pharmacist_btn.setFont(QFont("Arial", 24))
        pharmacist_btn.setStyleSheet("background-color:#9C27B0; color:white; padding:20px; border-radius:10px;")
        pharmacist_btn.clicked.connect(self.open_pharmacist)
        layout.addWidget(pharmacist_btn)

        #регистратура
        registrar_btn = QPushButton("Регистратура")
        registrar_btn.setFont(QFont("Arial", 24))
        registrar_btn.setStyleSheet("background-color:#FF5722; color:white; padding:20px; border-radius:10px;")
        registrar_btn.clicked.connect(self.open_registrar)
        layout.addWidget(registrar_btn)

        #выйти
        exit_btn = QPushButton("❌ Выйти")
        exit_btn.setFont(QFont("Arial", 20))
        exit_btn.setStyleSheet("background-color:#f44336; color:white; padding:15px; border-radius:10px;")
        exit_btn.clicked.connect(self.close)
        layout.addWidget(exit_btn)

        self.setLayout(layout)

    def open_doctor(self):
        self.doctor_login = DoctorLoginWindow()
        self.doctor_login.showMaximized()
        self.close()

    def open_patient(self):
        self.patient_login = PatientLoginWindow()
        self.patient_login.showMaximized()
        self.close()

    def open_pharmacist(self):
        self.pharmacist_login = PharmacistLoginWindow()
        self.pharmacist_login.showMaximized()
        self.close()
    
    def open_registrar(self):
        self.registrar_login = RegistrarLoginWindow()
        self.registrar_login.showMaximized()
        self.close()
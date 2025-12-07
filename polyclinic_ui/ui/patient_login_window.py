from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from ui.patient_window import PatientWindow

class PatientLoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Авторизация Пациента")
        self.showMaximized()

        layout = QVBoxLayout()
        layout.setSpacing(20)

        label = QLabel("Введите ФИО пациента")
        label.setFont(QFont("Arial",28))
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

        self.name_input = QLineEdit()
        self.name_input.setFont(QFont("Arial",20))
        self.name_input.setPlaceholderText("Иванова Анна Сергеевна")
        layout.addWidget(self.name_input, alignment=Qt.AlignCenter)

        login_btn = QPushButton("Войти")
        login_btn.setFont(QFont("Arial",22))
        login_btn.setStyleSheet("background-color:#03A9F4; color:white; padding:15px; border-radius:10px;")
        login_btn.clicked.connect(self.login)
        layout.addWidget(login_btn, alignment=Qt.AlignCenter)

        back_btn = QPushButton("Назад")
        back_btn.setFont(QFont("Arial",20))
        back_btn.setStyleSheet("background-color:#FFC107; color:black; padding:15px; border-radius:10px;")
        back_btn.clicked.connect(self.go_back)
        layout.addWidget(back_btn, alignment=Qt.AlignCenter)

        self.setLayout(layout)

    def login(self):
        name = self.name_input.text().strip()
        if not name:
            QMessageBox.warning(self,"Ошибка","Введите ФИО!")
            return
        self.patient_window = PatientWindow(patient_name=name)
        self.patient_window.showMaximized()
        self.close()

    def go_back(self):
        from ui.start_window import StartWindow
        self.start = StartWindow()
        self.start.showMaximized()
        self.close()

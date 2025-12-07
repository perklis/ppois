from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from .doctor_window import DoctorWindow
from .doctor_login_window import DoctorLoginWindow

class RoleSelectWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Поликлиника — Выбор роли")
        self.showFullScreen()  # Открываем на весь экран

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)

        # Заголовок
        label = QLabel("Добро пожаловать в нашу Поликлинику!\nВыберите свою роль:")
        label.setFont(QFont("Arial", 32, QFont.Bold))
        label.setStyleSheet("color: #004d80; margin-bottom: 50px;")
        label.setAlignment(Qt.AlignCenter)

        # Кнопка Доктор
        doctor_button = QPushButton("🩺 Доктор")
        doctor_button.setFont(QFont("Arial", 24, QFont.Bold))
        doctor_button.setStyleSheet("""
            QPushButton {
                background-color: #73c2fb;
                color: white;
                border-radius: 15px;
                padding: 25px;
            }
            QPushButton:hover {
                background-color: #4ea3d4;
            }
        """)
        doctor_button.clicked.connect(self.open_doctor_window)

        layout.addWidget(label)
        layout.addWidget(doctor_button)

    def open_doctor_window(self):
        self.login_window = DoctorLoginWindow()
        self.login_window.show()
        self.close()
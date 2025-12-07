from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from ui.registrar_window import RegistrarWindow
from ui.registrars_db import REGISTRARS_DB

class RegistrarLoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Авторизация Регистратора")
        self.showMaximized()

        layout = QVBoxLayout()
        layout.setSpacing(20)

        label = QLabel("Введите ФИО регистратора")
        label.setFont(QFont("Arial",28))
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

        self.name_input = QLineEdit()
        self.name_input.setFont(QFont("Arial",20))
        self.name_input.setPlaceholderText("Козлова Елена")
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
        if name not in REGISTRARS_DB:
            QMessageBox.warning(self,"Ошибка","Регистратор не найден в базе!")
            return
        self.registrar_window = RegistrarWindow(registrar_name=name)
        self.registrar_window.showMaximized()
        self.close()

    def go_back(self):
        from ui.start_window import StartWindow
        self.start = StartWindow()
        self.start.showMaximized()
        self.close()

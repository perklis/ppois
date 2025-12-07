from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget, QPushButton, QTextEdit, QMessageBox, QLineEdit
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from ui.patient_window import appointments
from ui.inventory import PRESCRIPTIONS

class DoctorWindow(QWidget):
    def __init__(self, doctor_name="Доктор", specialization="Не указано"):
        super().__init__()
        self.doctor_name = doctor_name
        self.specialization = specialization
        self.setWindowTitle(f"{doctor_name} — {specialization}")
        self.showMaximized()

        layout = QVBoxLayout()
        layout.setSpacing(15)

        title = QLabel(f"Доктор: {self.doctor_name} ({self.specialization})")
        title.setFont(QFont("Arial",26))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        self.patient_list = QListWidget()
        self.patient_list.setFont(QFont("Arial",18))
        layout.addWidget(self.patient_list)

        self.note_edit = QTextEdit()
        self.note_edit.setFont(QFont("Arial",16))
        self.note_edit.setPlaceholderText("Заметка о пациенте / Диагноз / Лечение")
        layout.addWidget(self.note_edit)

        # Добавляем поле рецепта
        self.prescription_input = QLineEdit()
        self.prescription_input.setFont(QFont("Arial",16))
        self.prescription_input.setPlaceholderText("Выписать рецепт (название лекарства)")
        layout.addWidget(self.prescription_input)

        save_btn = QPushButton("Сохранить диагноз и рецепт")
        save_btn.setFont(QFont("Arial",18))
        save_btn.setStyleSheet("background-color:#4CAF50; color:white; padding:10px; border-radius:10px;")
        save_btn.clicked.connect(self.save_note)
        layout.addWidget(save_btn)

        back_btn = QPushButton("Назад в меню ролей")
        back_btn.setFont(QFont("Arial",18))
        back_btn.setStyleSheet("background-color:#FFC107; color:black; padding:10px; border-radius:10px;")
        back_btn.clicked.connect(self.go_back)
        layout.addWidget(back_btn)

        self.setLayout(layout)
        self.update_patient_list()

    def update_patient_list(self):
        self.patient_list.clear()
        for (date,spec), lst in sorted(appointments.items()):
            for r in lst:
                if r.get("doctor_name") == self.doctor_name:
                    self.patient_list.addItem(f"{r['patient']} - {date} {r['time']}")

    def save_note(self):
        item = self.patient_list.currentItem()
        if not item:
            return
        note = self.note_edit.toPlainText().strip()
        prescription = self.prescription_input.text().strip()
        patient_name = item.text().split(" - ")[0]
        if note:
            QMessageBox.information(self, "Сохранено", f"Заметка для {patient_name} сохранена!")
            self.note_edit.clear()
        if prescription:
            # Добавляем рецепт в словарь
            PRESCRIPTIONS.setdefault(patient_name, []).append(prescription)
            QMessageBox.information(self, "Рецепт", f"Рецепт для {patient_name} выписан: {prescription}")
            self.prescription_input.clear()


    def go_back(self):
        from ui.start_window import StartWindow
        self.start = StartWindow()
        self.start.showMaximized()
        self.close()

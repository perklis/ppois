from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QComboBox, QCalendarWidget, QPushButton, QListWidget, QMessageBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QDate, Qt
from ui.doctors_db import DOCTORS_DB
from ui.inventory import INVENTORY, PRESCRIPTIONS

appointments = {}

class PatientWindow(QWidget):
    def __init__(self, patient_name):
        super().__init__()
        self.patient_name = patient_name
        self.setWindowTitle(f"Пациент — {self.patient_name}")
        self.showMaximized()

        layout = QVBoxLayout()
        layout.setSpacing(15)

        title = QLabel(f"Пациент: {self.patient_name}")
        title.setFont(QFont("Arial",26))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        self.specialty_select = QComboBox()
        self.specialty_select.addItems(set(DOCTORS_DB.values()))
        self.specialty_select.setFont(QFont("Arial",18))
        layout.addWidget(self.specialty_select, alignment=Qt.AlignCenter)

        self.doctor_select = QComboBox()
        self.doctor_select.setFont(QFont("Arial",18))
        layout.addWidget(self.doctor_select, alignment=Qt.AlignCenter)
        self.specialty_select.currentTextChanged.connect(self.update_doctors)
        self.update_doctors(self.specialty_select.currentText())

        self.calendar = QCalendarWidget()
        self.calendar.setGridVisible(True)
        self.calendar.setMinimumDate(QDate(2025,1,1))
        self.calendar.setMaximumDate(QDate(2026,12,31))
        layout.addWidget(self.calendar)

        self.book_btn = QPushButton("Записаться на приём")
        self.book_btn.setFont(QFont("Arial",20))
        self.book_btn.setStyleSheet("background-color:#4CAF50; color:white; padding:15px; border-radius:10px;")
        self.book_btn.clicked.connect(self.book_slot)
        layout.addWidget(self.book_btn, alignment=Qt.AlignCenter)

        self.app_list = QListWidget()
        self.app_list.setFont(QFont("Arial",16))
        layout.addWidget(self.app_list)

        self.cancel_btn = QPushButton("Отменить запись")
        self.cancel_btn.setFont(QFont("Arial",18))
        self.cancel_btn.setStyleSheet("background-color:#f44336; color:white; padding:10px; border-radius:10px;")
        self.cancel_btn.clicked.connect(self.cancel_appointment)
        layout.addWidget(self.cancel_btn, alignment=Qt.AlignCenter)

        self.buy_btn = QPushButton("Купить лекарство")
        self.buy_btn.setFont(QFont("Arial",18))
        self.buy_btn.setStyleSheet("background-color:#9C27B0; color:white; padding:10px; border-radius:10px;")
        self.buy_btn.clicked.connect(self.buy_medicine)
        layout.addWidget(self.buy_btn, alignment=Qt.AlignCenter)

        self.back_btn = QPushButton("Выйти в меню ролей")
        self.back_btn.setFont(QFont("Arial",18))
        self.back_btn.setStyleSheet("background-color:#FFC107; color:black; padding:10px; border-radius:10px;")
        self.back_btn.clicked.connect(self.go_back)
        layout.addWidget(self.back_btn, alignment=Qt.AlignCenter)

        self.setLayout(layout)
        self.update_appointments_view()

    def update_doctors(self, specialty):
        self.doctor_select.clear()
        self.doctor_select.addItems([name for name,spec in DOCTORS_DB.items() if spec==specialty])

    def book_slot(self):
        date = self.calendar.selectedDate().toString("yyyy-MM-dd")
        specialty = self.specialty_select.currentText()
        doctor_name = self.doctor_select.currentText()

        slots = [f"{h:02d}:{m:02d}" for h in range(8,16) for m in (0,30)]

        booked = [r["time"] for r in appointments.get((date, doctor_name),[])]
        free_slots = [s for s in slots if s not in booked]

        if not free_slots:
            QMessageBox.information(self,"Нет мест","На выбранный день всё занято!")
            return

        from PyQt5.QtWidgets import QDialog, QListWidget, QVBoxLayout, QPushButton
        dialog = QDialog(self)
        dialog.setWindowTitle("Выберите время")
        dialog.setModal(True)
        dialog.resize(400, 300)

        layout = QVBoxLayout()

        time_list = QListWidget()
        for slot in free_slots[:10]:  
            time_list.addItem(slot)
        layout.addWidget(time_list)

        ok_btn = QPushButton("Записаться")
        ok_btn.clicked.connect(dialog.accept)
        layout.addWidget(ok_btn)

        dialog.setLayout(layout)
        dialog.exec_()

        if dialog.result() == QDialog.Accepted:
            selected_item = time_list.currentItem()
            if selected_item:
                time = selected_item.text()
                appointments.setdefault((date, doctor_name), []).append({
                    "patient": self.patient_name,
                    "time": time,
                    "specialization": specialty,
                    "doctor_name": doctor_name
                })
                self.update_appointments_view()
                QMessageBox.information(self,"Успешно",f"Вы записаны к {doctor_name} на {date} в {time}")

    def update_appointments_view(self):
        self.app_list.clear()
        for (date, doctor), lst in appointments.items():
            for r in lst:
                if r["patient"]==self.patient_name:
                    self.app_list.addItem(f"{date}, {r['doctor_name']}, {r['time']}")

    def cancel_appointment(self):
        selected = self.app_list.currentItem()
        if not selected: return
        text = selected.text()
        date, doctor_name, time = [t.strip() for t in text.split(",")]
        appointments[(date, doctor_name)] = [
            r for r in appointments[(date, doctor_name)]
            if not (r["patient"]==self.patient_name and r["time"]==time)
        ]
        self.update_appointments_view()

    def buy_medicine(self):
        medicines = PRESCRIPTIONS.get(self.patient_name, [])
        if not medicines:
            QMessageBox.information(self,"Ошибка","У вас нет выписанных рецептов!")
            return
        bought = []
        for med in medicines[:]: 
            if INVENTORY.get(med,0) > 0:
                INVENTORY[med] -= 1 
                bought.append(med)
                medicines.remove(med) 
        if bought:
            QMessageBox.information(self,"Куплено","Вы купили: "+", ".join(bought))
        else:
            QMessageBox.information(self,"Ошибка","Нет доступных лекарств по рецептам")
    
    def go_back(self):
        from ui.start_window import StartWindow
        self.start = StartWindow()
        self.start.showMaximized()
        self.close()

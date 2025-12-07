from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QListWidget, QMessageBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QDate
from ui.patient_window import appointments

class RegistrarWindow(QWidget):
    def __init__(self, registrar_name):
        super().__init__()
        self.registrar_name = registrar_name
        self.setWindowTitle(f"Регистратура — {self.registrar_name}")
        self.showMaximized()

        layout = QVBoxLayout()
        layout.setSpacing(15)

        title = QLabel(f"Регистратор: {self.registrar_name}")
        title.setFont(QFont("Arial",26))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        self.report_btn = QPushButton("Создать отчёт за текущую неделю")
        self.report_btn.setFont(QFont("Arial",18))
        self.report_btn.setStyleSheet("background-color:#4CAF50; color:white; padding:10px; border-radius:10px;")
        self.report_btn.clicked.connect(self.create_weekly_report)
        layout.addWidget(self.report_btn)

        self.patient_list = QListWidget()
        self.patient_list.setFont(QFont("Arial",16))
        layout.addWidget(self.patient_list)

        self.record_btn = QPushButton("Записать пациента на анализы")
        self.record_btn.setFont(QFont("Arial",18))
        self.record_btn.setStyleSheet("background-color:#03A9F4; color:white; padding:10px; border-radius:10px;")
        self.record_btn.clicked.connect(self.add_lab_test)
        layout.addWidget(self.record_btn)

        back_btn = QPushButton("Назад в меню ролей")
        back_btn.setFont(QFont("Arial",18))
        back_btn.setStyleSheet("background-color:#FFC107; color:black; padding:10px; border-radius:10px;")
        back_btn.clicked.connect(self.go_back)
        layout.addWidget(back_btn)

        self.setLayout(layout)
        self.update_patient_list()

    def update_patient_list(self):
        self.patient_list.clear()
        patients_set = set()
        for (date, doctor), lst in appointments.items():
            for r in lst:
                patients_set.add(r["patient"])
        for p in sorted(patients_set):
            self.patient_list.addItem(p)

    def create_weekly_report(self):
        from datetime import datetime, timedelta
        today = QDate.currentDate()
        start_of_week = today.addDays(-today.dayOfWeek()+1) 
        end_of_week = start_of_week.addDays(6) 

        report_lines = []
        for (date_str, doctor), lst in appointments.items():
            date = QDate.fromString(date_str, "yyyy-MM-dd")
            if start_of_week <= date <= end_of_week:
                for r in lst:
                    report_lines.append(f"{date_str}, {r['time']}, {r['patient']}, {doctor}")

        if report_lines:
            QMessageBox.information(self,"Отчёт за неделю","\n".join(report_lines))
        else:
            QMessageBox.information(self,"Отчёт за неделю","Записей на текущую неделю нет")

    def add_lab_test(self):
        item = self.patient_list.currentItem()
        if not item:
            return
        patient_name = item.text()
        for (date, doctor), lst in appointments.items():
            for r in lst:
                if r["patient"] == patient_name:
                    r.setdefault("lab_tests", []).append("Назначен анализ")
        QMessageBox.information(self,"Успешно",f"Пациент {patient_name} записан на анализы")

    def go_back(self):
        from ui.start_window import StartWindow
        self.start = StartWindow()
        self.start.showMaximized()
        self.close()

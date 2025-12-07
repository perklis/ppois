from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget, QPushButton, QMessageBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from ui.inventory import INVENTORY, PRESCRIPTIONS

class PharmacistWindow(QWidget):
    def __init__(self, pharmacist_name):
        super().__init__()
        self.pharmacist_name = pharmacist_name
        self.setWindowTitle(f"Аптекарь — {self.pharmacist_name}")
        self.showMaximized()

        layout = QVBoxLayout()
        layout.setSpacing(15)

        title = QLabel(f"Аптекарь: {self.pharmacist_name}")
        title.setFont(QFont("Arial",26))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        self.inventory_list = QListWidget()
        self.inventory_list.setFont(QFont("Arial",16))
        layout.addWidget(self.inventory_list)

        refresh_btn = QPushButton("Обновить склад")
        refresh_btn.setFont(QFont("Arial",18))
        refresh_btn.setStyleSheet("background-color:#03A9F4; color:white; padding:10px; border-radius:10px;")
        refresh_btn.clicked.connect(self.update_inventory)
        layout.addWidget(refresh_btn)

        back_btn = QPushButton("Назад в меню ролей")
        back_btn.setFont(QFont("Arial",18))
        back_btn.setStyleSheet("background-color:#FFC107; color:black; padding:10px; border-radius:10px;")
        back_btn.clicked.connect(self.go_back)
        layout.addWidget(back_btn)

        self.setLayout(layout)
        self.update_inventory()

    def update_inventory(self):
        self.inventory_list.clear()
        for med, count in INVENTORY.items():
            self.inventory_list.addItem(f"{med}: {count} шт.")
        self.inventory_list.addItem("=== Выписанные рецепты ===")
        for patient, meds in PRESCRIPTIONS.items():
            if meds:
                self.inventory_list.addItem(f"{patient}: {', '.join(meds)}")

    def go_back(self):
        from ui.start_window import StartWindow
        self.start = StartWindow()
        self.start.showMaximized()
        self.close()

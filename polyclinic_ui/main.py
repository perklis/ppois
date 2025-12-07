import sys
from PyQt5.QtWidgets import QApplication
from ui.start_window import StartWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet("""
        QWidget {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                stop:0 #e3f2fd, stop:1 #bbdefb);
            font-family: 'Segoe UI', Arial;
        }
    """)

    window = StartWindow()
    window.showMaximized()
    sys.exit(app.exec_())

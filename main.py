import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QWidget
from PyQt6.QtCore import QTextStream, Qt
from PyQt6.QtGui import QTextCursor
import io
import contextlib

class OutputRedirector(io.StringIO):
    def __init__(self, text_widget):
        super().__init__()
        self.text_widget = text_widget

    def write(self, text):
        self.text_widget.moveCursor(QTextCursor.MoveOperation.End)
        self.text_widget.insertPlainText(text)
        self.text_widget.moveCursor(QTextCursor.MoveOperation.End)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Terminal-like Log Viewer")
        self.setGeometry(100, 100, 800, 600)

        # Create a central widget and set the layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Create a QTextEdit to display the logs
        self.log_text_edit = QTextEdit()
        self.log_text_edit.setReadOnly(True)
        layout.addWidget(self.log_text_edit)

        # Redirect stdout to the QTextEdit
        self.redirector = OutputRedirector(self.log_text_edit)
        sys.stdout = self.redirector

        # Example prints
        print("Iniciando o programa...")
        print("Este é um exemplo de log.")
        print("Você pode ver todos os prints aqui.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
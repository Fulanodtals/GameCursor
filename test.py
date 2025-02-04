from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout, QGridLayout
)
from PyQt6.QtGui import QFont
import sys
import webbrowser


class GameCursorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GameCursor")
        self.setGeometry(100, 100, 500, 400)

        # Layout principal
        layout = QVBoxLayout()

        # Título
        title = QLabel("GameCursor")
        title.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        title.setStyleSheet("text-align: center;")
        layout.addWidget(title)

        subtitle = QLabel("controle seu mouse com o controle")
        layout.addWidget(subtitle)

        # Informações do controle
        control_info = QLabel("Controle:\nNome: x\nTipo: y\nStatus: ativo")
        layout.addWidget(control_info)

        # Configurações de velocidade
        speed_layout = QGridLayout()
        self.mouse_speed_input = QLineEdit("70")
        self.scroll_speed_input = QLineEdit("0.9")

        speed_layout.addWidget(QLabel("Velocidade do mouse:"), 0, 0)
        speed_layout.addWidget(self.mouse_speed_input, 0, 1)
        speed_layout.addWidget(QLabel("Velocidade do scroll:"), 1, 0)
        speed_layout.addWidget(self.scroll_speed_input, 1, 1)

        layout.addLayout(speed_layout)

        # Output do console (logs)
        self.console_output = QTextEdit()
        self.console_output.setReadOnly(True)
        self.console_output.setPlaceholderText("Output do console aqui mostrando os logs")
        layout.addWidget(self.console_output)

        # Configuração de botões
        buttons_layout = QGridLayout()
        self.left_button_input = QLineEdit("a")
        self.right_button_input = QLineEdit("x")
        self.double_click_input = QLineEdit("b")
        self.press_button_input = QLineEdit("y")

        buttons_layout.addWidget(QLabel("Botão esquerdo:"), 0, 0)
        buttons_layout.addWidget(self.left_button_input, 0, 1)
        buttons_layout.addWidget(QLabel("Click duplo:"), 0, 2)
        buttons_layout.addWidget(self.double_click_input, 0, 3)
        buttons_layout.addWidget(QLabel("Botão direito:"), 1, 0)
        buttons_layout.addWidget(self.right_button_input, 1, 1)
        buttons_layout.addWidget(QLabel("Botão pressionar:"), 1, 2)
        buttons_layout.addWidget(self.press_button_input, 1, 3)

        layout.addLayout(buttons_layout)

        # Botão para site
        self.site_button = QPushButton("Acesse: www.siteaqui.com.br")
        self.site_button.clicked.connect(self.open_website)
        layout.addWidget(self.site_button)

        # Botão para função personalizada
        self.hide_button = QPushButton("Ocultar Janela")
        self.hide_button.clicked.connect(self.custom_function)
        layout.addWidget(self.hide_button)

        self.setLayout(layout)

    def open_website(self):
        webbrowser.open("https://www.siteaqui.com.br")

    def custom_function(self):
        self.console_output.append("Função personalizada executada!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GameCursorApp()
    window.show()
    sys.exit(app.exec())

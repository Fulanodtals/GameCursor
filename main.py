from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QGridLayout, QSystemTrayIcon, QMenu, QCheckBox
from PyQt6.QtGui import QFont, QAction, QIcon
from GameCursor import MouseController
from settings import Config
from PyQt6.QtCore import Qt
import webbrowser
import pygame
import sys

pygame.init() #Inicia o pygame
pygame.joystick.init() #Inicia a configuracao do pygame para controles


global joystick
joystick = MouseController.connect_controller()

class ConsoleOutput:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, text):
        self.text_widget.moveCursor(self.text_widget.textCursor().MoveOperation.End)
        self.text_widget.insertPlainText(text)

    def flush(self):
        pass  # Necessário para compatibilidade com sys.stdout


class GameCursorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GameCursor")
        self.setGeometry(100, 100, 500, 400)
        self.setFixedSize(350, 450)
        
        layout = QVBoxLayout() # Layout principal
        
        #Configuração do ícone da bandeja do sistema
        self.tray_icon = QSystemTrayIcon(QIcon("icon.png"), self)
        self.tray_icon.setToolTip("GameCursor")

        #menu do ícone da bandeja
        menu = QMenu()
        restore_action = QAction("Restaurar", self)
        restore_action.triggered.connect(self.show_window)
        exit_action = QAction("Sair", self)
        exit_action.triggered.connect(sys.exit)

        menu.addAction(restore_action)
        menu.addAction(exit_action)
        self.tray_icon.setContextMenu(menu)
        self.tray_icon.activated.connect(self.tray_activated)

        self.tray_icon.show()

        # Header
        title = QLabel("(: GameCursor :)")
        subtitle = QLabel("Controle seu mouse com o controle!")
        title.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)
        layout.addWidget(subtitle)

        # Conectando com o controle para pegar os dados
        controller_info = QLabel(f"""
                                    \nNome: {joystick.get_name()}
                                    \nBateria: {joystick.get_power_level()}
                                    \nStatus: {'ativo'}""")
        print("Controle conectado!")
        layout.addWidget(controller_info)

        # Output do console (logs)
        self.console_output = QTextEdit()
        self.console_output.setReadOnly(True)
        self.console_output.setPlaceholderText("Output do console aqui mostrando os logs")
        layout.addWidget(self.console_output)
        
        sys.stdout = ConsoleOutput(self.console_output)

        # Mostra o guia de botões
        buttons_layout = QGridLayout()
        buttons_layout.addWidget(QLabel("Click esquerdo: A"), 0, 0)
        buttons_layout.addWidget(QLabel("Click direito:      B"), 1, 0)
        buttons_layout.addWidget(QLabel("Click duplo:       X"), 0, 1)
        buttons_layout.addWidget(QLabel("Pressionar:         Y"), 1, 1)
        buttons_layout.addWidget(QLabel("Diminuir vel/:    LB"), 2, 0)
        buttons_layout.addWidget(QLabel("Aumentar vel/:  RB"), 2, 1)
        layout.addLayout(buttons_layout)

        # Botão para site
        self.site_button = QPushButton("Acesse: bit.ly/joaosantoslink")
        self.site_button.clicked.connect(self.open_website)
        layout.addWidget(self.site_button)

        # Botão para ocultar janela
        self.hide_button = QPushButton("Ocultar Janela")
        self.hide_button.clicked.connect(self.hide_window)
        layout.addWidget(self.hide_button)
        
        self.setLayout(layout)# Mostra a janela

        self.hide() # Inicia com a janela oculta

        # Inicia o programa depois de renderizar o app:
        MouseController.controller_moves()
    

    def open_website(self):
        webbrowser.open("https://bit.ly/joaosantoslink")

    def hide_window(self):
        self.hide()

    def show_window(self):
        self.show()
        self.activateWindow()

    def tray_activated(self, reason):
        if reason == QSystemTrayIcon.ActivationReason.Trigger:
            self.show_window()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GameCursorApp()
    sys.exit(app.exec())

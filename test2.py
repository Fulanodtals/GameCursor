import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QLabel, QMessageBox
from PyQt6.QtCore import Qt, QTimer
import GameCursor

class JoystickControlWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Joystick Control Customizer")
        self.setGeometry(100, 100, 400, 200)

        # Variáveis para armazenar as ações dos botões
        self.a_action = "Botão A (Padrão)"
        self.b_action = "Botão B (Padrão)"

        # Layout principal
        main_layout = QVBoxLayout()

        # Área para o botão A
        a_layout = QHBoxLayout()
        self.a_label = QLabel("Botão A (Padrão):")
        self.a_button = QPushButton("Clique para redefinir")
        self.a_button.clicked.connect(lambda: self.capture_button("A"))
        a_layout.addWidget(self.a_label)
        a_layout.addWidget(self.a_button)

        # Área para o botão B
        b_layout = QHBoxLayout()
        self.b_label = QLabel("Botão B (Padrão):")
        self.b_button = QPushButton("Clique para redefinir")
        self.b_button.clicked.connect(lambda: self.capture_button("B"))
        b_layout.addWidget(self.b_label)
        b_layout.addWidget(self.b_button)

        # Botão para aplicar as configurações
        self.apply_button = QPushButton("Aplicar Configurações")
        self.apply_button.clicked.connect(self.apply_settings)

        # Adicionando os layouts ao layout principal
        main_layout.addLayout(a_layout)
        main_layout.addLayout(b_layout)
        main_layout.addWidget(self.apply_button)

        # Widget central
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # Timer para capturar eventos do joystick
        self.timer = QTimer()
        self.timer.timeout.connect(self.check_joystick_events)
        self.capturing_for = None  # Indica para qual botão estamos capturando (A ou B)

    def capture_button(self, button):
        self.capturing_for = button
        QMessageBox.information(self, "Captura de Botão", f"Pressione um botão no controle para redefinir o botão {button}.")
        self.timer.start(100)  # Verifica eventos do joystick a cada 100ms

    def check_joystick_events(self):
        """Verifica os eventos do joystick para capturar o botão pressionado."""
        try:
            events = inputs.get_gamepad()
            for event in events:
                if event.ev_type == "Key" and event.state == 1:  # Botão pressionado
                    button_name = event.code
                    if self.capturing_for == "A":
                        self.a_action = button_name
                        self.a_button.setText(button_name)
                        self.timer.stop()
                        self.capturing_for = None
                        QMessageBox.information(self, "Sucesso", f"Botão A redefinido para: {button_name}")
                    elif self.capturing_for == "B":
                        self.b_action = button_name
                        self.b_button.setText(button_name)
                        self.timer.stop()
                        self.capturing_for = None
                        QMessageBox.information(self, "Sucesso", f"Botão B redefinido para: {button_name}")
        except inputs.UnpluggedError:
            QMessageBox.warning(self, "Erro", "Nenhum controle conectado.")
            self.timer.stop()
            self.capturing_for = None

    def apply_settings(self):
        """Aplica as configurações escolhidas pelo usuário."""
        print(f"Ação do Botão A: {self.a_action}")
        print(f"Ação do Botão B: {self.b_action}")
        QMessageBox.information(self, "Configurações Aplicadas", "As configurações foram aplicadas com sucesso!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = JoystickControlWindow()
    window.show()
    sys.exit(app.exec())
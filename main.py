import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QSystemTrayIcon, QMenu
from PyQt6.QtGui import QAction, QIcon

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("App em Segundo Plano")
        self.setGeometry(100, 100, 300, 200)

        # Botão para ocultar a janela
        self.btn_hide = QPushButton("Ocultar", self)
        self.btn_hide.setGeometry(100, 80, 100, 30)
        self.btn_hide.clicked.connect(self.hide_window)

        # Criando o ícone da bandeja do sistema
        self.tray_icon = QSystemTrayIcon(QIcon("icon.png"), self)
        self.tray_icon.setToolTip("Aplicação em Segundo Plano")
        
        # Criando o menu do ícone da bandeja
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
    window = MyApp()
    window.show()
    sys.exit(app.exec())

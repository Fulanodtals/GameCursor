import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit

class ConsoleOutput:
    """Redireciona os prints para um QTextEdit."""
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, text):
        self.text_widget.moveCursor(self.text_widget.textCursor().MoveOperation.End)
        self.text_widget.insertPlainText(text)

    def flush(self):
        pass  # Necessário para compatibilidade com sys.stdout

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        
        layout = QVBoxLayout(self)
        
        # Criando a área de logs
        self.console_output = QTextEdit()
        self.console_output.setReadOnly(True)
        self.console_output.setPlaceholderText("Output do console aqui mostrando os logs")
        layout.addWidget(self.console_output)
        
        # Redirecionando stdout
        sys.stdout = ConsoleOutput(self.console_output)

        # Teste: prints de diferentes lugares
        print("Log 1: Teste de print() dentro da classe principal")
        self.teste()

    def teste(self):
        print("Log 2: Print dentro de outro método.")

if __name__ == "__main__":
    app = QApplication([])
    window = MyApp()
    window.show()
    
    # Teste fora da classe (simulando print em outro lugar do código)
    print("Log 3: Print feito fora da classe")

    app.exec()

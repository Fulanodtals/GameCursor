from settings import Config as settings
from plyer import notification
from time import sleep
import pyautogui
import pygame
import sys


#pygame.init() #Inicia o pygame
#pygame.joystick.init() #Inicia a configuracao do pygame para controles

# Variável de controle global
running = True


# funcao que altera o estado - (rodando o programa ou nao)
def toggle_running():
    global running
    running = not running
    
    
class MouseController:
    @staticmethod
    def messages(action): #Funcao para mostrar as mensagens 
        if action == 'good_connection':
            notification.notify(
                title="Conexão bem-sucedida :)",
                message='Controle conectado',
                app_name="MouseControl",
                timeout=5 
            )
        elif action == 'bad_connection':
            notification.notify(
                title="Conexão mal-sucedida :(",
                message='Nenhum controle conectado',
                app_name="MouseControl",
                timeout=5 
            )
        elif action == 'stopping_control':
            notification.notify(
                title="Parando ações com o controle ;) ",
                message='O controle não executará mais ações!',
                app_name="MouseControl",
                timeout=5
            )
        elif action == 'running_control':
            notification.notify(
                title="De volta ao normal :)",
                message='Você pode executar ações com o controle!',
                app_name="MouseControl",
                timeout=5
            )
        
        
    def connect_controller(): #Funcao que conecta o controle
        while pygame.joystick.get_count() == 0: #Faz uma varredura para achar os controles
            print('Procurando controle...')
            pygame.joystick.quit() #Fecha a varredura antiga
            pygame.joystick.init() #Inicia uma nova varredura
            sleep(10) #Time de 10s para verificar novamente
        else:
            print('Controle conectado!')
            MouseController.messages('good_connection')

        joystick = pygame.joystick.Joystick(0) #Adiciona o primeiro joystick a variavel
        joystick.init() #Anicia as acoes do controle
        return joystick
    

    def controller_moves(): #funcao que verifica os movimentos e faz as acoes
        joystick = MouseController.connect_controller() #conecta com o controle
        LEFT_BUTTON = 0 #    A
        RIGHT_BUTTON = 1 #   B
        DUBBLE_BUTTON = 2 #  X
        HOLDING_BUTTON = 3 # Y
        holding = False
        
        
        try:
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                        
                #variaveis que serao manipuladas
                mouse_speed = int(settings.getValue('mouse_speed'))
                scroll_speed = 0.9
                
                #condicao que pausa ou continua o programa
                if joystick.get_button(6) and joystick.get_button(7): #Botão start + menu
                    toggle_running()
                    if running:
                        MouseController.messages('running_control')
                    else:
                        MouseController.messages('stopping_control')
                    sleep(1) #tempo para não travar
                if not running:
                    sleep(0.5) #Tempo para o programa voltar
                    continue


                # Pega os dados do mouse:
                x_axis = joystick.get_axis(0)  # Eixo horizontal
                y_axis = joystick.get_axis(1)  # Eixo vertical
                current_x, current_y = pyautogui.position()  # Posição do mouse

                # Calcula aS posições do cursor
                new_x = current_x + int(x_axis * mouse_speed)
                new_y = current_y + int(y_axis * mouse_speed)
                pyautogui.FAILSAFE = False #necessario para movimentacao da tela
                pyautogui.moveTo(new_x, new_y)

                #Ações de click do controle
                if joystick.get_button(HOLDING_BUTTON): #click para precionar
                    if not holding: #condicao para ver se esta clicando
                        pyautogui.mouseDown()
                        holding = True
                else:
                    if holding: #ou selecionando
                        pyautogui.mouseUp()
                        holding = False

                if joystick.get_button(LEFT_BUTTON): #click esquerdo
                    pyautogui.click()
                    sleep(0.1) #deley para nao haver interferencia
                if joystick.get_button(RIGHT_BUTTON): #click direito
                    pyautogui.rightClick()
                    sleep(0.1) #deley para nao haver interferencia
                if joystick.get_button(DUBBLE_BUTTON): #click duplo
                    pyautogui.doubleClick()
                    sleep(0.1) #deley para nao haver interferencia


                # movimentacoes de scroll
                right_stick_y = joystick.get_axis(3)  # Eixo vertical do stick direito
                if right_stick_y > scroll_speed:
                    pyautogui.scroll(-60)  # Scroll para baixo
                elif right_stick_y <- scroll_speed:
                    pyautogui.scroll(60)  # Scroll para cima

                #Adulteracao da velocidade do cursor 
                if joystick.get_button(5) and mouse_speed <= 200:  # Botão RB
                    settings.changeSpeed('mouse_speed', mouse_speed + 5)
                    print(f"Velocidade aumentada para: {mouse_speed}")
                elif joystick.get_button(4) and mouse_speed >= 0:  # Botão LB
                    settings.changeSpeed('mouse_speed', mouse_speed - 5)
                    print(f"Velocidade reduzida para: {mouse_speed}")
    
        except Exception as e:
            exc_type, exc_value, exc_tb = sys.exc_info()
            print(f"\n\nOps, Algo deu errado!\n")
            print(f"Tipo de erro: {exc_type.__name__}")
            print(f"Mensagem de erro: {e}")
            print(f"Erro ocorrido no arquivo: {exc_tb.tb_frame.f_code.co_filename}")
            print(f"Na linha: {exc_tb.tb_lineno}")
            print("\nO programa será encerrado em 10 segundos...")
            print(e)
            sleep(10)
        finally:
            pygame.quit()
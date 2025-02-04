from settings import config as settings
from plyer import notification
from time import sleep
import pyautogui
import pygame

pygame.init() #inicia o pygame
pygame.joystick.init() #inicia a configuracao do pygame para controles

# Variável de controle global
running = True


# funcao que altera o estado - (rodando o programa ou nao)
def toggle_running():
    global running
    running = not running
    
    
class MouseController:
    @staticmethod
    def messages(action): #funcao para mostrar as mensagens 
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
        
        
    def conect_controller(): #funcao que conecta o controle
        while pygame.joystick.get_count() == 0:# faz uma varredura para achar os controles
            print('Procurando controle...')
            pygame.joystick.quit()#Fecha a varredura antiga
            pygame.joystick.init()#inicia uma nova varredura
            sleep(10)#time de 10s para verificar novamente
        else:
            print('Controle conectado!')
            MouseController.messages('good_connection')

        joystick = pygame.joystick.Joystick(0)#adiciona o primeiro joystick a variavel
        joystick.init()#inicia as acoes do controle
        return joystick
    

    def controller_moves(): #funcao que verifica os movimentos e faz as acoes
        joystick = MouseController.conect_controller() #conecta com o controle
        mouse_speed = settings.getValue('mouse_speed')
        scroll_speed = settings.getValue('scroll_speed')
        holding = False
        
        try:
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()

                #condicao que pausa ou continua o programa
                if joystick.get_button(6) and joystick.get_button(7): #Botão start + menu
                    toggle_running()
                    if running:
                        MouseController.messages('running_control')
                    else:
                        MouseController.messages('stopping_control')
                    sleep(1) #tempo para não travar se clicar varias vezes
                if not running:
                    sleep(0.5) #Tempo para o programa voltar
                    continue


                # Pega os dados do mouse:
                x_axis = joystick.get_axis(0)  # Eixo horizontal
                y_axis = joystick.get_axis(1)  # Eixo vertical
                current_x, current_y = pyautogui.position()  # Posição do mouse

                # Calcula a nova posição do cursor
                new_x = current_x + int(x_axis * mouse_speed)
                new_y = current_y + int(y_axis * mouse_speed)
                pyautogui.FAILSAFE = False #necessario para movimentacao da tela
                pyautogui.moveTo(new_x, new_y)

                #Ações de click do controle
                if joystick.get_button(3): #click para precionar
                    if not holding: #condicao para ver se esta clicando
                        pyautogui.mouseDown()
                        holding = True
                else:
                    if holding: #ou selecionando
                        pyautogui.mouseUp()
                        holding = False

                if joystick.get_button(0): #click esquerdo
                    pyautogui.click()
                    sleep(0.1)
                if joystick.get_button(2): #click direito
                    pyautogui.rightClick()

                '''if joystick.get_button(7): #atalho para abrir o teclado virtual
                    pyautogui.hotkey('win', 'ctrl', 'o')
                    keyboard = True'''

                # movimentacoes de scroll
                right_stick_y = joystick.get_axis(3)  # Eixo vertical do stick direito
                if right_stick_y > scroll_speed:
                    pyautogui.scroll(-60)  # Scroll para baixo
                elif right_stick_y <- scroll_speed:
                    pyautogui.scroll(60)  # Scroll para cima

                #Adulteracao da velocidade do cursor 
                if joystick.get_button(5):  # Botão RB
                    mouse_speed += 5
                    print(f"Velocidade aumentada para: {mouse_speed}")
                elif joystick.get_button(4):  # Botão LB
                    mouse_speed = max(1, mouse_speed - 5)
                    print(f"Velocidade reduzida para: {mouse_speed}")
        
        except Exception as e:
            print(f"Ops, Algo deu errado!\n    {e}\n\n O programa sera encerrado em 10 segundos")
            sleep(10)
        finally:
            pygame.quit()

if __name__ == "__main__":
    MouseController.controller_moves()

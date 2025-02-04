'''
Aqui é onde tem as configuracoes que acessam o arquivo txt
'''
from anyio import value
import pygame

pygame.init()
pygame.joystick.init()

PATH = './config.txt'

class config():
    def getValue(variable):
        with open(PATH, "r") as f:
            for row in f:
                if row.startswith(variable + "="):
                    value = row.strip().split("=")[1] 
                    return float(value)
        return None
    
    def changeSpeed(variable, value):
        new_speed = []
        with open(PATH, "r") as f:
            for row in f:
                if row.startswith(variable + "="):
                    new_speed.append(f"{variable}={value}\n")  # Modifica a row
                else:
                    new_speed.append(row)

        with open(PATH, "w") as f:
            f.writelines(new_speed)
    
    @staticmethod
    def selectButton():
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
        
        num_buttons = joystick.get_numbuttons()
        while True:
            pygame.event.pump()
            for i in range(num_buttons):
                if joystick.get_button(i):
                    print(f"Botão {i} pressionado")
                    return i
            
            pygame.time.wait(100)
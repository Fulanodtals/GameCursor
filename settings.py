import pygame
import os

pygame.init()
pygame.joystick.init()

current_dir = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(current_dir, "config.txt")

class Config():
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
                    new_speed.append(f"{variable}={value}\n")
                else:
                    new_speed.append(row)

        with open(PATH, "w") as f:
            f.writelines(new_speed)
    
    #funcao não usada
    def selectButton():#funcao para mostrar os botoes quando clika
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
        
        num_buttons = joystick.get_numbuttons()
        while True:
            pygame.event.pump()
            for i in range(num_buttons):
                if joystick.get_button(i):
                    print(f"Botão precionado: {i}")
            
            pygame.time.wait(100)
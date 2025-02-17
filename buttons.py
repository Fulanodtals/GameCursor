import pygame

# Este código não é usado no programa, é apenas para testes do controle

def main():
    pygame.init()
    pygame.joystick.init()
    
    if pygame.joystick.get_count() == 0:
        print("Nenhum controle encontrado.")
        return
    
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    print(f"Controle detectado: {joystick.get_name()}")
    print(f"ID: {joystick.get_id()}")
    print(f"Nivel de bateria: {joystick.get_power_level()}")

    num_buttons = joystick.get_numbuttons()
    print(f"Número de botões: {num_buttons}")
    print(f"Número de eixos: {joystick.get_numaxes()}")


    print("Pressione os botões para ver o índice correspondente")
    while True:
        pygame.event.pump()
        for i in range(num_buttons):
            if joystick.get_button(i):
                print(f'botao: {joystick.get_button(i)} | index {i}')
                
        pygame.time.wait(100)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nSaindo...")
        pygame.quit()

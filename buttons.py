import pygame

def main():
    pygame.init()
    pygame.joystick.init()
    
    if pygame.joystick.get_count() == 0:
        print("Nenhum controle encontrado.")
        return
    
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    
    print(f"Controle detectado: {joystick.get_name()}")
    
    num_buttons = joystick.get_numbuttons()
    print(f"Número de botões: {num_buttons}")
    
    print("Pressione os botões para ver o índice correspondente (CTRL+C para sair).")
    
    running = True
    while running:
        pygame.event.pump()
        for i in range(num_buttons):
            if joystick.get_button(i):
                print(f"Botão {i} pressionado")
        
        pygame.time.wait(100)  # Pequena pausa para evitar uso excessivo da CPU

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nSaindo...")
        pygame.quit()

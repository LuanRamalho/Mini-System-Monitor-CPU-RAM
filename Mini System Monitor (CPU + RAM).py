import psutil, time, os

while True:
    # Limpa o console: 'cls' para Windows, 'clear' para outros (Linux/macOS)
    os.system("cls" if os.name == "nt" else "clear")
    
    # Imprime o uso atual da CPU
    print(f"CPU Usage: {psutil.cpu_percent()} %")
    
    # Imprime o uso atual da RAM (memória virtual)
    print(f"RAM Usage: {psutil.virtual_memory().percent} %")
    
    # Pausa por 1 segundo antes de atualizar
    time.sleep(1)

input()
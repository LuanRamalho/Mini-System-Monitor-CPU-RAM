import psutil
import time
import os
import tkinter as tk
from tkinter import font as tkfont # Para gerenciar fontes

# --- Configurações da GUI ---
BG_COLOR = "#2c3e50"    # Azul Escuro / Cinza (Fundo)
CPU_COLOR = "#e74c3c"   # Vermelho (CPU)
RAM_COLOR = "#3498db"   # Azul Claro (RAM)
TEXT_COLOR = "#ecf0f1"  # Cinza Claro (Texto Principal)

class SystemMonitorApp:
    def __init__(self, master):
        self.master = master
        master.title("Mini Monitor de Sistema (CPU + RAM)")
        master.configure(bg=BG_COLOR)
        
        # O Tkinter principal usa 'self.master.after' para chamar a função de atualização
        # em um loop, eliminando a necessidade do 'while True' no código principal.
        
        # 1. Configurar Fontes
        self.large_font = tkfont.Font(family="Helvetica", size=24, weight="bold")
        self.medium_font = tkfont.Font(family="Helvetica", size=16, weight="normal")

        # 2. Rótulos de Título
        tk.Label(master, text="Uso da CPU", font=self.medium_font, bg=BG_COLOR, fg=CPU_COLOR).pack(pady=(20, 5))
        
        # 3. Rótulo de Uso da CPU (Valor)
        self.cpu_label = tk.Label(master, text="0.0 %", font=self.large_font, bg=CPU_COLOR, fg=TEXT_COLOR, width=10)
        self.cpu_label.pack(pady=5, padx=30)

        # 4. Rótulos de Título
        tk.Label(master, text="Uso da RAM", font=self.medium_font, bg=BG_COLOR, fg=RAM_COLOR).pack(pady=(20, 5))
        
        # 5. Rótulo de Uso da RAM (Valor)
        self.ram_label = tk.Label(master, text="0.0 %", font=self.large_font, bg=RAM_COLOR, fg=TEXT_COLOR, width=10)
        self.ram_label.pack(pady=5, padx=30)

        # Inicia a atualização
        self.update_stats()

    def update_stats(self):
        """Busca as estatísticas e atualiza os rótulos."""
        
        # 1. Coleta os dados
        cpu_percent = psutil.cpu_percent(interval=None) # Não espera, obtém o valor imediatamente
        ram_percent = psutil.virtual_memory().percent
        
        # 2. Atualiza a CPU
        self.cpu_label.config(text=f"{cpu_percent:.1f} %")
        # Altera a cor de fundo dinamicamente para indicar alto uso
        if cpu_percent > 80:
            self.cpu_label.config(bg="#c0392b") # Vermelho Escuro
        elif cpu_percent > 50:
            self.cpu_label.config(bg="#f39c12") # Laranja
        else:
            self.cpu_label.config(bg=CPU_COLOR) # Cor padrão
            
        # 3. Atualiza a RAM
        self.ram_label.config(text=f"{ram_percent:.1f} %")
        # Altera a cor de fundo dinamicamente para indicar alto uso
        if ram_percent > 80:
            self.ram_label.config(bg="#2980b9") # Azul Escuro
        elif ram_percent > 50:
            self.ram_label.config(bg="#1abc9c") # Verde Água
        else:
            self.ram_label.config(bg=RAM_COLOR) # Cor padrão

        # Agenda a próxima atualização após 1000 milissegundos (1 segundo)
        self.master.after(1000, self.update_stats)

# --- Cria e Inicia a Janela ---
root = tk.Tk()
app = SystemMonitorApp(root)
root.mainloop()
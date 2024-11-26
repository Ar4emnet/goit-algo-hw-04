import tkinter as tk
from tkinter import (messagebox)
import random
import matplotlib.pyplot as plt
from math import prod
def runprogram():
    try:        # Retrieve user input for a and b
        a = int(entry_a.get())
        b = int(entry_b.get())
        if a > b:
            messagebox.showerror("Chyba", "Hodnota a musí byť menšia alebo rovná hodnote b.")
            return
        # Generate 60 random numbers based on a and b
        numbers = [random.randint(a, b) for _ in range(60)]
        # Calculate sum and product
        summ = sum(numbers)
        mutiplication = prod(numbers)
        # Add 5 to each number
        fixedNumbers = [x + 5 for x in numbers]
        # Display results in a message box
        messagebox.showinfo("Výsledky", f"Súčet: {summ}\nSúčin: {mutiplication}")
        # Plot the graph
        plt.figure(figsize=(10, 6))
        plt.plot(fixedNumbers, marker='o', label='Pôvodné hodnoty')
        plt.title("Graf pôvodných hodnôt")
        plt.xlabel("Index")
        plt.ylabel("Hodnota")
        plt.legend()
        plt.grid()
        plt.show()
    except ValueError:        messagebox.showerror("Chyba", "Prosím, zadajte platné čísla pre a a b.")

# Set up the main window
okno = tk.Tk()
okno.title("Programovacie techniky")
okno.geometry("400x300")
# Add labels and input fields for a and b
label_a = tk.Label(okno, text="Zadajte hodnotu a (dolná hranica):")
label_a.pack(pady=5)
entry_a = tk.Entry(okno)
entry_a.pack(pady=5)
label_b = tk.Label(okno, text="Zadajte hodnotu b (horná hranica):")
label_b.pack(pady=5)
entry_b = tk.Entry(okno)
entry_b.pack(pady=5)
# Description text
legend = tk.Label(okno,
                  text="Programovacie techniky\n"                       "Meno: Aliaksandr\n"
                       "Priezvisko: Varapayeu\n"                       "Zadanie úlohy: Vygenerujte pole 60 náhodných čísiel, "
                       "spočítajte a tiež vynásobte všetky čísla a vypíšte obidve výsledky, "                       "ku každému číslu prirátajte hodnotu 5 a vykreslite graf všetkých neupravených hodnôt.",
                  wraplength=380, justify="left")
legend.pack(pady=10)
# Button to run the program
button = tk.Button(okno, text="Spustiť program", command=runprogram)
button.pack(pady=20)
# Start the main loop
okno.mainloop()
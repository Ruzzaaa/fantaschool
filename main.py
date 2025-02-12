import tkinter as tk
from tkinter import ttk, Menu, messagebox
import webbrowser

def open_window(title, create_func):
    window = tk.Toplevel()
    window.title(title)
    window.geometry("400x700")
    create_func(window)

def create_registrazione(window):
    window.configure(bg="#1e1e2f")
    tk.Label(window, text="Registrazione", font=("Helvetica", 24, "bold"), fg="#FF79C6", bg="#1e1e2f").pack(pady=20)

    fields = ["Nome e Cognome", "Email", "Cellulare", "Data di Nascita"]
    for field in fields:
        tk.Label(window, text=field, bg="#1e1e2f", fg="#8BE9FD", font=("Helvetica", 12)).pack(pady=5)
        tk.Entry(window, width=30, font=("Helvetica", 12), bg="#282a36", fg="#f8f8f2", insertbackground="#f8f8f2").pack(pady=5)

    tk.Button(window, text="Accedi con Google", bg="#FF5555", fg="white", font=("Helvetica", 12), width=20, relief="flat", command=accedi_google).pack(pady=10)
    tk.Button(window, text="Registrati Ora", bg="#50FA7B", fg="white", font=("Helvetica", 12), width=20, relief="flat").pack(pady=10)

def accedi_google():
    webbrowser.open("https://accounts.google.com/signin/v2/identifier")

def create_esplora(window):
    window.configure(bg="#282a36")
    tk.Label(window, text="Esplora", font=("Helvetica", 24, "bold"), fg="#FFB86C", bg="#282a36").pack(pady=20)

    tk.Label(window, text="Campionato", bg="#282a36", fg="#8BE9FD", font=("Helvetica", 12)).pack(pady=5)
    tk.Entry(window, width=30, font=("Helvetica", 12), bg="#44475a", fg="#f8f8f2", insertbackground="#f8f8f2").pack(pady=5)

    tk.Button(window, text="Inserisci Formazione", bg="#6272a4", fg="white", font=("Helvetica", 12), width=20, relief="flat").pack(pady=10)

def create_formazione(window):
    window.configure(bg="#1e1e2f")
    tk.Label(window, text="Formazione", font=("Helvetica", 24, "bold"), fg="#FFB86C", bg="#1e1e2f").pack(pady=20)

    canvas = tk.Canvas(window, width=350, height=200, bg="#282a36", highlightthickness=0)
    canvas.pack(pady=10)

    canvas.create_rectangle(20, 20, 330, 180, outline="#50FA7B", width=3)
    canvas.create_line(175, 20, 175, 180, fill="#50FA7B", width=2)
    canvas.create_oval(140, 70, 210, 130, outline="#50FA7B", width=2)

    for i in range(5):
        x_offset = i * 60 + 20
        for j in range(2):
            y_offset = j * 40 + 40
            canvas.create_oval(x_offset, y_offset, x_offset+10, y_offset+10, fill="#FF79C6", outline="white")

    tk.Label(window, text="Giocatori", bg="#1e1e2f", fg="#8BE9FD", font=("Helvetica", 14)).pack(pady=10)
    for i in range(1, 5):
        tk.Label(window, text=f"Giocatore {i}", bg="#1e1e2f", fg="#f8f8f2", font=("Helvetica", 12)).pack(pady=5)

    tk.Label(window, text="Riserve", bg="#1e1e2f", fg="#8BE9FD", font=("Helvetica", 14)).pack(pady=10)

def create_calendario(window):
    window.configure(bg="#282a36")
    tk.Label(window, text="Calendario", font=("Helvetica", 24, "bold"), fg="#BD93F9", bg="#282a36").pack(pady=20)

    canvas = tk.Canvas(window, width=350, height=300, bg="#282a36", highlightthickness=0)
    canvas.pack(pady=10)

    days = [f"Giornata {i}: Squadra A vs Squadra B" for i in range(1, 6)]
    for i, day in enumerate(days):
        y_offset = i * 50 + 20
        canvas.create_rectangle(20, y_offset, 330, y_offset+40, outline="#FF79C6", width=2)
        canvas.create_text(175, y_offset+20, text=day, fill="#F8F8F2", font=("Helvetica", 12))

def create_utente(window):
    window.configure(bg="#1e1e2f")
    tk.Label(window, text="Utente", font=("Helvetica", 24, "bold"), fg="#50FA7B", bg="#1e1e2f").pack(pady=20)

    tk.Label(window, text="Storico", bg="#1e1e2f", fg="#8BE9FD", font=("Helvetica", 14)).pack(pady=10)
    buttons = [
        ("Informazioni Personali", create_informazioni_personali),
        ("Pagamenti", create_pagamenti),
        ("Lingua", create_lingua),
        ("Sicurezza", create_sicurezza),
    ]
    for btn_text, btn_command in buttons:
        tk.Button(window, text=btn_text, bg="#6272a4", fg="white", font=("Helvetica", 12), width=20, relief="flat", command=lambda cmd=btn_command: open_window(btn_text, cmd)).pack(pady=5)

def create_informazioni_personali(window):
    window.configure(bg="#1e1e2f")
    tk.Label(window, text="Informazioni Personali", font=("Helvetica", 24, "bold"), fg="#50FA7B", bg="#1e1e2f").pack(pady=20)
    tk.Label(window, text="Dettagli sulle informazioni personali.", bg="#1e1e2f", fg="#8BE9FD", font=("Helvetica", 12)).pack(pady=5)

def create_pagamenti(window):
    window.configure(bg="#1e1e2f")
    tk.Label(window, text="Pagamenti", font=("Helvetica", 24, "bold"), fg="#50FA7B", bg="#1e1e2f").pack(pady=20)
    tk.Label(window, text="Dettagli sui pagamenti.", bg="#1e1e2f", fg="#8BE9FD", font=("Helvetica", 12)).pack(pady=5)

def create_lingua(window):
    window.configure(bg="#1e1e2f")
    tk.Label(window, text="Lingua", font=("Helvetica", 24, "bold"), fg="#50FA7B", bg="#1e1e2f").pack(pady=20)
    tk.Label(window, text="Opzioni per la lingua.", bg="#1e1e2f", fg="#8BE9FD", font=("Helvetica", 12)).pack(pady=5)

def create_sicurezza(window):
    window.configure(bg="#1e1e2f")
    tk.Label(window, text="Sicurezza", font=("Helvetica", 24, "bold"), fg="#50FA7B", bg="#1e1e2f").pack(pady=20)
    tk.Label(window, text="Opzioni di sicurezza e protezione.", bg="#1e1e2f", fg="#8BE9FD", font=("Helvetica", 12)).pack(pady=5)

def on_exit():
    root.quit()

root = tk.Tk()
root.title("Fantaschool")
root.geometry("500x800")
root.configure(bg="#282a36")

# Menu bar
menu_bar = Menu(root, background="yellow", foreground="black", activebackground="orange", activeforeground="black", font=("Helvetica", 12))
root.config(menu=menu_bar)

opzioni_menu = Menu(menu_bar, tearoff=0, background="yellow", foreground="black", activebackground="orange", activeforeground="black", font=("Helvetica", 12))
menu_bar.add_cascade(label="Opzioni", menu=opzioni_menu)

def mostra_aiuto():
    messagebox.showinfo("Aiuto", "Se hai dubbi puoi consultare il manuale utente all'indirizzo www.grazieprofnonsoveramentecomeringraziarla.com")

def mostra_contatti():
    contatti = "Email: alessandro.ruzza06@gmail.com\nTelefono: +39 347 938 0751\nSito Web: www.grazieprof.com"
    messagebox.showinfo("Contattaci", contatti)

opzioni_menu.add_command(label="Aiuto", command=mostra_aiuto)
opzioni_menu.add_command(label="Contattaci", command=mostra_contatti)
opzioni_menu.add_separator()
opzioni_menu.add_command(label="Esci", command=root.quit)

frame = tk.Frame(root, bg="#FF79C6", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.9, relheight=0.1, anchor="n")

title = tk.Label(frame, text="Benvenuto su Fantaschool", font=("Helvetica", 18, "bold"), fg="#1e1e2f", bg="#FF79C6")
title.pack(fill="both", expand=True)

button_frame = tk.Frame(root, bg="#282a36")
button_frame.place(relx=0.5, rely=0.3, relwidth=0.9, relheight=0.6, anchor="n")

buttons = [
    ("Registrazione", lambda: open_window("Registrazione", create_registrazione), "#FF5555"),
    ("Esplora", lambda: open_window("Esplora", create_esplora), "#6272a4"),
    ("Formazione", lambda: open_window("Formazione", create_formazione), "#FFB86C"),
    ("Utente", lambda: open_window("Utente", create_utente), "#50FA7B"),
    ("Calendario", lambda: open_window("Calendario", create_calendario), "#BD93F9"),
]

for text, command, color in buttons:
    tk.Button(
        button_frame, 
        text=text, 
        command=command, 
        font=("Helvetica", 14), 
        bg=color, 
        fg="white", 
        relief="raised", 
        bd=3, 
        width=20
    ).pack(pady=10)

footer = tk.Label(root, text="Fantaschool © 2025", font=("Helvetica", 10), bg="#282a36", fg="#f8f8f2")
footer.pack(side="bottom", pady=10)

root.mainloop()

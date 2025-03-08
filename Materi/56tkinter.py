# GUI -->> Graphical User Interface

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

###INIT
window = tk.Tk()
window.configure(bg="white")
window.geometry("300x200")
window.resizable(False, False)
window.title("Game Sederhana")

###VARIABEL DAN FUNGSI
nama_depan = tk.StringVar()
nama_belakang = tk.StringVar()

def tombol_klik():
    '''fungsi ini akan dipanggil oleh tombol'''
    pesan = f"Selamat Datang {nama_depan.get()} {nama_belakang.get()}, Mari kita mulai!"
    showinfo(title="Welcome", message=pesan)

###FRAME INPUT
input_frame = ttk.Frame(window)
# Penempatan Grid, Pack, Place
input_frame.pack(padx=10, pady=10, fill="x", expand=True)

###KOMPONEN-KOMPONEN
#1. Label nama depan
namadepan_label = ttk.Label(input_frame, text = "Nama Depan :")
namadepan_label.pack(padx=10, fill='x', expand=True)

#2. Entry nama depan
namadepan_entry = ttk.Entry(input_frame, textvariable=nama_depan)
namadepan_entry.pack(padx=10, fill='x',expand = True)

#3. Label nama belakang
namabelakang_label = ttk.Label(input_frame, text="Nama Belakang :")
namabelakang_label.pack(padx=10, fill='x', expand=True)

#4. Entry nama belakang
namabelakang_entry = ttk.Entry(input_frame, textvariable=nama_belakang)
namabelakang_entry.pack(padx=10, fill='x', expand=True)

#5. Tombol
tombol_sapa = ttk.Button(input_frame, text="Login", command=tombol_klik)
tombol_sapa.pack(fill='x', expand=True, padx=10, pady=10)

###MAIN LOOP WINDOW
window.mainloop()

# Appelle des bibilothèques
import tkinter as tk
import os
import fnmatch
from pygame import mixer
from tkinter import filedialog

# Function pour l'ouverture a ouvrir
def ouverture():
    fichier_nom = filedialog.askopenfilename(initialdir="/",
                                            title="Selectionne un fichier",
                                            filetypes=(("Fichier text",
                                            "*.txt*"),
                                            ("Toutes les fichiers",
                                            "*.*")))

#definition de la commande volume
def volume(event):
    mixer.music.set_volume(volume_musique.get())

# Controle de lecture pour le volume
def lecture():
    label.config(text=listBox.get("anchor"))
    mixer.music.load(rootpath + "\\" + listBox.get("anchor"))
    mixer.music.play()


def boucle():
    label.config(text=listBox.get("anchor"))
    mixer.music.load(rootpath + "\\" + listBox.get("anchor"))
    mixer.music.play(loops=-1)

# Créations de la fenetre tkinter
canvas = tk.Tk()
canvas.title("Musique player")
canvas.geometry("600x600")
canvas.config(bg='white')
# Musique a sélectionner
rootpath = "musiquepython"
pattern = "*.mp3"

# Initialiser la musique a jouer
mixer.init()

# Liste de msuic
listBox = tk.Listbox(canvas, fg="cyan", bg="black", width=100, font=('arial', 14))
listBox.pack(padx=15, pady=15)

# Definir la racine root
for root, dirs, files in os.walk(rootpath):
    for filename in fnmatch.filter(files, pattern):
        listBox.insert('end', filename)  # Refaire une nouvelle liste qui va inserer les musique


# Définition play
def select():
    label.config(text=listBox.get("anchor"))
    mixer.music.load(rootpath + "\\" + listBox.get("anchor"))
    mixer.music.play()


# definition stop
def stop():
    mixer.music.stop()
    listBox.select_clear('active')


# Définition suivant
def suv():
    suiv_song = listBox.curselection()
    suiv_song = suiv_song[0] + 1
    suiv_song_nom = listBox.get(suiv_song)

    label.config(text=suiv_song_nom)

    mixer.music.load(rootpath + "\\" + suiv_song_nom)
    mixer.music.play()
    # La ligne bleu va chercher le song et le selectionner
    listBox.select_clear(0, 'end')
    listBox.activate(suiv_song)
    listBox.select_set(suiv_song)


# Définition précédant
def prec():
    avant_song = listBox.curselection()
    avant_song_song = avant_song[0] - 1
    avant_song_nom = listBox.get(avant_song_song)

    label.config(text=avant_song_nom)

    mixer.music.load(rootpath + "\\" + avant_song_nom)
    mixer.music.play()
    # La ligne bleu va chercher le song et le selectionner
    listBox.select_clear(0, 'end')
    listBox.activate(avant_song)
    listBox.select_set(avant_song)


# Définition bouton pause
def pause():
    if pauseButton["text"] == "pause":
        mixer.music.pause()
        pauseButton["text"] = "play"

    else:
        mixer.music.unpause()
        pauseButton["text"] = "pause"

# Volume musique
volume_musique = tk.Scale(canvas, from_=0, to_=1.0, orient="horizontal", resolution=0.1,showvalue=0, command=volume)
volume_musique.set(0.8)
volume_musique.pack()

# Création de LabelFrame
label = tk.Label(canvas, text="", bg='black', fg='blue', font=('arial', 18))
label.pack(pady=15)
# Création d'un frame
top = tk.Frame(canvas, bg='blue')
top.pack(padx=10, pady=5, anchor='center')

# Création des boutons
precButton = tk.Button(canvas, text="prec", command=prec)
precButton.pack(pady=15, in_=top, side="left")
stopButton = tk.Button(canvas, text="stop", command=stop)
stopButton.pack(pady=15, in_=top, side="left")
playButton = tk.Button(canvas, text="play", command=select)
playButton.pack(pady=15, in_=top, side="left")
pauseButton = tk.Button(canvas, text="pause", command=pause)
pauseButton.pack(pady=15, in_=top, side="left")
suvButton = tk.Button(canvas, text="suv", command=suv)
suvButton.pack(pady=15, in_=top, side="left")
bclButton = tk.Button(canvas, text="Boucle", command=boucle)
bclButton.pack(ipady=15, in_=top, side="left")
ouv_btn = tk.Button(canvas, text="Ajouter", command=ouverture)
ouv_btn.pack(pady=15, in_=top, side="left")
# Fermeture de la carte graphique
canvas.mainloop()

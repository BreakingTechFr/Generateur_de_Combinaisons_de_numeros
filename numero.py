import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import itertools
import csv
import json
import threading
import multiprocessing

class ApplicationCombinaisons(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Générateur de Combinaisons")
        self.configure(bg="#000000")  # Couleur de fond noire
        
        # Définition du style pour le fond noir
        self.style = ttk.Style()
        self.style.theme_use("clam")  # Changer de thème pour contourner le problème
        self.style.configure(".", background="#000000", foreground="#ffffff")
        self.style.configure("TFrame", background="#000000")
        self.style.configure("TButton", background="#000000", foreground="#ffffff")
        self.style.configure("TEntry", background="#000000", foreground="#ffffff")
        self.style.map("TButton", background=[("active", "#333333")])  # Changer la couleur lorsqu'il est activé
        self.style.configure("TCombobox", arrowcolor="white")  # Couleur de la flèche
        
        # Cadre principal
        self.cadre_principal = ttk.Frame(self)
        self.cadre_principal.grid(row=1, column=0, padx=20, pady=20)
        
        # Logo
        self.logo_image = Image.open("logo.jpg")
        self.logo_image = self.logo_image.resize((200, 200), Image.ANTIALIAS)
        self.logo_photo = ImageTk.PhotoImage(self.logo_image)
        self.logo_label = tk.Label(self, image=self.logo_photo, bg="#000000")
        self.logo_label.grid(row=0, column=0, pady=10)
        
        # Libellé
        ttk.Label(self.cadre_principal, text="Numéro Initial :", foreground="#ffffff").grid(row=0, column=0, sticky="w")
        ttk.Label(self.cadre_principal, text="\u0332".join("Ecrivez un X pour chaque inconnu dans le numéro"), font=("TkDefaultFont", 9, "italic"), foreground="#ffffff").grid(row=1, column=0, columnspan=2, sticky="w")
        ttk.Label(self.cadre_principal, text="Format de Sortie :", foreground="#ffffff").grid(row=2, column=0, sticky="w")
        
        # Entrée
        self.entree_numero_initial = ttk.Entry(self.cadre_principal)
        self.entree_numero_initial.grid(row=0, column=1, sticky="w")
        self.entree_numero_initial.insert(0, "06XX456944")  # Ajouter un exemple
        self.entree_numero_initial.config(foreground="white")  # Changer ici
        
        self.combobox_format_sortie = ttk.Combobox(self.cadre_principal, values=["txt", "csv", "json"])
        self.combobox_format_sortie.grid(row=2, column=1, sticky="w")
        self.combobox_format_sortie.set("txt")  # Choisir txt par défaut
        self.combobox_format_sortie.config(foreground="white")  # Changer ici
        
        # Boutons
        self.bouton_generer = ttk.Button(self.cadre_principal, text="Générer", command=self.generer_combinaisons)
        self.bouton_generer.grid(row=3, column=0, pady=10)
        
        self.bouton_quitter = ttk.Button(self.cadre_principal, text="Quitter", command=self.quitter_application)
        self.bouton_quitter.grid(row=3, column=1, pady=10)
    
    def generer_combinaisons(self):
        numero_initial = self.entree_numero_initial.get()
        format_sortie = self.combobox_format_sortie.get()
        
        if 'X' not in numero_initial:
            messagebox.showerror("Erreur", "Le numéro initial doit contenir au moins un 'X' pour représenter un chiffre inconnu.")
            return
        
        nb_processus = multiprocessing.cpu_count()
        fichier_sortie = f"combinaisons_{numero_initial}.{format_sortie}"
        threading.Thread(target=self.generer_toutes_combinaisons, args=(numero_initial, format_sortie, fichier_sortie, nb_processus)).start()
    
    def generer_toutes_combinaisons(self, numero_initial, format_sortie, fichier_sortie, nb_processus):
        combinaisons = []
        chiffres_inconnus = numero_initial.count('X')
        for comb in itertools.product("0123456789", repeat=chiffres_inconnus):
            new_number = numero_initial.replace("X" * chiffres_inconnus, "".join(comb))
            combinaisons.append(new_number)
        
        self.after(0, self.afficher_message_succes)
        self.ecrire_sortie(combinaisons, fichier_sortie, format_sortie)
    
    def afficher_message_succes(self):
        messagebox.showinfo("Succès", "Génération des combinaisons terminée.")
    
    def ecrire_sortie(self, combinaisons, fichier_sortie, format_sortie):
        if format_sortie == 'txt':
            self.ecrire_txt(combinaisons, fichier_sortie)
        elif format_sortie == 'csv':
            self.ecrire_csv(combinaisons, fichier_sortie)
        elif format_sortie == 'json':
            self.ecrire_json(combinaisons, fichier_sortie)
    
    def ecrire_txt(self, combinaisons, fichier_sortie):
        with open(fichier_sortie, 'w') as fichier:
            for combinaison in combinaisons:
                fichier.write(combinaison + "\n")
    
    def ecrire_csv(self, combinaisons, fichier_sortie):
        with open(fichier_sortie, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for combinaison in combinaisons:
                writer.writerow([combinaison])
    
    def ecrire_json(self, combinaisons, fichier_sortie):
        with open(fichier_sortie, 'w') as jsonfile:
            json.dump(combinaisons, jsonfile, indent=4)
    
    def quitter_application(self):
        self.destroy()

if __name__ == "__main__":
    app = ApplicationCombinaisons()
    app.mainloop()

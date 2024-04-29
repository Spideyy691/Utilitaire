import webbrowser
import tkinter as tk

def start_move(event):
    fenetre.x = event.x
    fenetre.y = event.y

def stop_move(event):
    fenetre.x = None
    fenetre.y = None

def do_move(event):
    dx = event.x - fenetre.x
    dy = event.y - fenetre.y
    x = fenetre.winfo_x() + dx
    y = fenetre.winfo_y() + dy
    fenetre.geometry(f"+{x}+{y}")

# Créer une fenêtre
fenetre = tk.Tk()

# Changer le thème en sombre
fenetre.configure(bg='black')

# Ajouter la fonctionnalité de déplacement de la fenêtre
fenetre.bind("<ButtonPress-1>", start_move)
fenetre.bind("<ButtonRelease-1>", stop_move)
fenetre.bind("<B1-Motion>", do_move)

# Définir les liens
liens = {
    "3cx": "https://fidulyon.my3cx.fr/webclient",
    "7zip": "https://www.7-zip.org/download.html",
    "Teams": "https://www.microsoft.com/fr-fr/microsoft-teams/download-app",
    "Adobe": "https://get.adobe.com/fr/reader/",
    "Java": "https://www.java.com/fr/",
    "PDF24": "https://tools.pdf24.org/fr/creator#download",
    "office mdp": "https://login.microsoftonline.com/common/oauth2/authorize?client_id=0000000c-0000-0000-c000-000000000000&redirect_uri=https%3a%2f%2faccount.activedirectory.windowsazure.com%2f&response_mode=form_post&response_type=code+id_token&scope=openid+profile&state=OpenIdConnect.AuthenticationProperties%3dAQAAAAIAAAAJLnJlZGlyZWN0RGh0dHBzOi8vYWNjb3VudC5hY3RpdmVkaXJlY3Rvcnkud2luZG93c2F6dXJlLmNvbS9DaGFuZ2VQYXNzd29yZC5hc3B4Hk9wZW5JZENvbm5lY3QuQ29kZS5SZWRpcmVjdFVyacABeGo4Rk1xcVRVdDZuc25uTTdzbTJ6aHB5T1ZkME1iWHAzNGFydjZjendRRDE3ZEw1b0NjalB0aU5qWmxxY0lZYWNqeW0zRmhra0lpbkFPSmJXZkV4UlUtcWZGNTA1d3g4eVh0WXpCb1Btb2YwRl94LUF4a1kydHBWN0JpU2VLaFduQmJzQkdPZDZvZF9Mc0VmSVAzaXFQWUxnNVVjTER0T2FXLWFCM0D",
    "Driver Dell": "https://www.dell.com/support/home/fr-fr?app=drivers",
    # Ajoutez vos propres liens ici
}

# Créer un bouton pour chaque lien
for nom, url in liens.items():
    bouton = tk.Button(fenetre, text=nom, command=lambda url=url: webbrowser.open(url), bg='grey', fg='white')
    bouton.pack(padx=10, pady=10)  # Ajouter des espaces autour des boutons

# Ajouter une signature
signature = tk.Label(fenetre, text="Fait par Adam FARADJI", bg='black', fg='white')
signature.pack(pady=10)

# Lancer la boucle principale
fenetre.mainloop()

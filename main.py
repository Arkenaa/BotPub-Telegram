import os
from telethon import TelegramClient
from colorama import Fore, Style, init

init(autoreset=True)

api_id = ''  #Entre ton API_ID, regarde ce site : https://my.telegram.org/auth
api_hash = ''  #Entre ton API_HASH, regarde ce site : https://my.telegram.org/auth
client = TelegramClient('session_name', api_id, api_hash)
nom_utilisateur = os.getlogin()

def afficher_banniere():
    print(Fore.RED + r"""
        ▄███████▄ ▄██   ▄       ███        ▄█    █▄     ▄██████▄  ███▄▄▄▄      ▄███████▄ ███    █▄  ▀█████████▄  
       ███    ███ ███   ██▄ ▀█████████▄   ███    ███   ███    ███ ███▀▀▀██▄   ███    ███ ███    ███   ███    ███ 
       ███    ███ ███▄▄▄███    ▀███▀▀██   ███    ███   ███    ███ ███   ███   ███    ███ ███    ███   ███    ███ 
       ███    ███ ▀▀▀▀▀▀███     ███   ▀  ▄███▄▄▄▄███▄▄ ███    ███ ███   ███   ███    ███ ███    ███  ▄███▄▄▄██▀  
     ▀█████████▀  ▄██   ███     ███     ▀▀███▀▀▀▀███▀  ███    ███ ███   ███ ▀█████████▀  ███    ███ ▀▀███▀▀▀██▄  
       ███        ███   ███     ███       ███    ███   ███    ███ ███   ███   ███        ███    ███   ███    ██▄ 
       ███        ███   ███     ███       ███    ███   ███    ███ ███   ███   ███        ███    ███   ███    ███ 
      ▄████▀       ▀█████▀     ▄████▀     ███    █▀     ▀██████▀   ▀█   █▀   ▄████▀      ████████▀  ▄█████████▀  
                                      
                                    by @arkenahousee / @tokyohq
                                 1 = Utiliser le script / 2 = Quitter
    """ + Style.RESET_ALL)

async def utiliser_script():
    print(f"{Fore.WHITE}│{nom_utilisateur}@root - Connectez-vous à Telegram...\n├─ {Style.RESET_ALL}")
    
    source_group = input(f"{Fore.WHITE}│{nom_utilisateur}@root - Entrez le nom d'utilisateur du groupe source\n├─ {Style.RESET_ALL}")
    target_groups = input(f"{Fore.WHITE}│{nom_utilisateur}@root - Entrez les groupes cibles (séparés par des virgules)\n├─ {Style.RESET_ALL}").split(',')
    message_id = int(input(f"{Fore.WHITE}│{nom_utilisateur}@root - Entrez l'ID du message à transférer\n├─ {Style.RESET_ALL}"))
    
    await client.start()
    
    try:
        for group in target_groups:
            print(f"{Fore.WHITE}│{nom_utilisateur}@root - Transfert vers {group.strip()}...\n├─ ")
            await client.forward_messages(group.strip(), message_id, source_group)
            print(f"{Fore.WHITE}│{nom_utilisateur}@root - Message transféré vers {group.strip()}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.WHITE}│{nom_utilisateur}@root - Erreur lors du transfert\n├─ {e}{Style.RESET_ALL}")

def menu_principal():
    while True:
        afficher_banniere()
        choix = input(f"{Fore.WHITE}│{nom_utilisateur}@root - Entrez votre choix\n├─ {Style.RESET_ALL}")
        if choix == "1":
            with client:
                client.loop.run_until_complete(utiliser_script())
        elif choix == "2":
            print(f"{Fore.WHITE}│{nom_utilisateur}@root - A bientot !{Style.RESET_ALL}")
            break
        else:
            print(f"{Fore.WHITE}│{nom_utilisateur}@root - Invalide ├─ {Style.RESET_ALL}")

menu_principal()

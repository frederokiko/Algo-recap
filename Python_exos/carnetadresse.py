import json

def display_menu():
    print("\nCarnet d'adresses:")
    print("1. Ajouter une adresse")
    print("2. Voir toutes les adresses")
    print("3. Modifier une adresse")
    print("4. Supprimer une adresse")
    print("5. Sauvegarder les adresses")
    print("6. Charger les adresses")
    print("7. Quitter")
    return input("Choisissez une option: ")

def add_address(address_book):
    name = input("Entrez le nom: ")
    address = input("Entrez l'adresse: ")
    address_book[name] = address
    print(f"Adresse ajoutée pour {name}.")

def view_addresses(address_book):
    if not address_book:
        print("Aucune adresse trouvée.")
    else:
        for name, address in address_book.items():
            print(f"Nom: {name}, Adresse: {address}")

def update_address(address_book):
    name = input("Entrez le nom de l'adresse à modifier: ")
    if name in address_book:
        new_address = input(f"Entrez la nouvelle adresse pour {name}: ")
        address_book[name] = new_address
        print(f"Adresse mise à jour pour {name}.")
    else:
        print(f"Aucune adresse trouvée pour {name}.")

def delete_address(address_book):
    name = input("Entrez le nom de l'adresse à supprimer: ")
    if name in address_book:
        del address_book[name]
        print(f"Adresse supprimée pour {name}.")
    else:
        print(f"Aucune adresse trouvée pour {name}.")

def save_addresses(address_book, filename="address_book.txt"):
    with open(filename, "w") as file:
        json.dump(address_book, file)
    print("Adresses sauvegardées.")

def load_addresses(filename="address_book.txt"):
    try:
        with open(filename, "r") as file:
            address_book = json.load(file)
        print("Adresses chargées.")
    except FileNotFoundError:
        print("Aucun fichier trouvé. Un nouveau carnet d'adresses sera créé.")
        address_book = {}
    return address_book

def main():
    address_book = load_addresses()
    while True:
        choice = display_menu()
        if choice == '1':
            add_address(address_book)
        elif choice == '2':
            view_addresses(address_book)
        elif choice == '3':
            update_address(address_book)
        elif choice == '4':
            delete_address(address_book)
        elif choice == '5':
            save_addresses(address_book)
        elif choice == '6':
            address_book = load_addresses()
        elif choice == '7':
            save_addresses(address_book)
            print("Au revoir!")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()

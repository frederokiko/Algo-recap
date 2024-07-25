import json
import os

# Chemin du fichier de sauvegarde
FILENAME = "todo_list.txt"

def display_menu():
    print("\nTo-Do List:")
    print("1. Ajouter une tache")
    print("2. Voir toutes les tâches")
    print("3. Modifier une tâche")
    print("4. Supprimer une tâche")
    print("5. Sauvegarder les tâches")
    print("6. Charger les tâches")
    print("7. Quitter")
    return input("Choisissez une option: ")

def add_task(todo_list):
    new_id = len(todo_list) + 1
    date = input("Entrez la date de rendez-vous: ")
    name = input("Entrez le nom: ")
    description = input("Entrez la description: ")
    task = {
        "id": new_id,
        "date": date,
        "name": name,
        "description": description
    }
    todo_list.append(task)
    print(f"Tâche ajoutée avec l'ID {new_id}.")

def view_tasks(todo_list):
    if not todo_list:
        print("Aucune tâche trouvée.")
    else:
        for task in todo_list:
            print(f"ID: {task['id']}, Date: {task['date']}, Nom: {task['name']}, Description: {task['description']}")

def update_task(todo_list):
    task_id = int(input("Entrez l'ID de la tâche à modifier: "))
    for task in todo_list:
        if task['id'] == task_id:
            task['date'] = input(f"Entrez la nouvelle date de rendez-vous pour l'ID {task_id} (actuelle: {task['date']}): ")
            task['name'] = input(f"Entrez le nouveau nom pour l'ID {task_id} (actuel: {task['name']}): ")
            task['description'] = input(f"Entrez la nouvelle description pour l'ID {task_id} (actuelle: {task['description']}): ")
            print(f"Tâche mise à jour pour l'ID {task_id}.")
            return
    print(f"Aucune tâche trouvée avec l'ID {task_id}.")

def delete_task(todo_list):
    task_id = int(input("Entrez l'ID de la tâche à supprimer: "))
    for i, task in enumerate(todo_list):
        if task['id'] == task_id:
            del todo_list[i]
            print(f"Tâche supprimée avec l'ID {task_id}.")
            return
    print(f"Aucune tâche trouvée avec l'ID {task_id}.")

def save_tasks(todo_list, filename=FILENAME):
    with open(filename, "w") as file:
        json.dump(todo_list, file)
    print("Tâches sauvegardées.")

def load_tasks(filename=FILENAME):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            todo_list = json.load(file)
        print("Tâches chargées.")
    else:
        print("Aucun fichier trouvé. Une nouvelle liste de tâches sera créée.")
        todo_list = []
    return todo_list

def main():
    todo_list = load_tasks()
    while True:
        choice = display_menu()
        if choice == '1':
            add_task(todo_list)
        elif choice == '2':
            view_tasks(todo_list)
        elif choice == '3':
            update_task(todo_list)
        elif choice == '4':
            delete_task(todo_list)
        elif choice == '5':
            save_tasks(todo_list)
        elif choice == '6':
            todo_list = load_tasks()
        elif choice == '7':
            save_tasks(todo_list)
            print("Au revoir!")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()

import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

# Chemin du fichier de sauvegarde
FILENAME = "todo_list.txt"

def add_task(todo_list, listbox):
    new_id = len(todo_list) + 1
    date = simpledialog.askstring("Input", "Entrez la date de rendez-vous:")
    name = simpledialog.askstring("Input", "Entrez le nom:")
    description = simpledialog.askstring("Input", "Entrez la description:")
    task = {
        "id": new_id,
        "date": date,
        "name": name,
        "description": description
    }
    todo_list.append(task)
    listbox.insert(tk.END, f"ID: {task['id']}, Date: {task['date']}, Nom: {task['name']}, Description: {task['description']}")
    messagebox.showinfo("Info", f"Tâche ajoutée avec l'ID {new_id}.")

def view_tasks(todo_list, listbox):
    listbox.delete(0, tk.END)
    if not todo_list:
        listbox.insert(tk.END, "Aucune tâche trouvée.")
    else:
        for task in todo_list:
            listbox.insert(tk.END, f"ID: {task['id']}, Date: {task['date']}, Nom: {task['name']}, Description: {task['description']}")

def update_task(todo_list, listbox):
    task_id = simpledialog.askinteger("Input", "Entrez l'ID de la tâche à modifier:")
    for task in todo_list:
        if task['id'] == task_id:
            task['date'] = simpledialog.askstring("Input", f"Entrez la nouvelle date de rendez-vous pour l'ID {task_id} (actuelle: {task['date']}):")
            task['name'] = simpledialog.askstring("Input", f"Entrez le nouveau nom pour l'ID {task_id} (actuel: {task['name']}):")
            task['description'] = simpledialog.askstring("Input", f"Entrez la nouvelle description pour l'ID {task_id} (actuelle: {task['description']}):")
            messagebox.showinfo("Info", f"Tâche mise à jour pour l'ID {task_id}.")
            view_tasks(todo_list, listbox)
            return
    messagebox.showerror("Error", f"Aucune tâche trouvée avec l'ID {task_id}.")

def delete_task(todo_list, listbox):
    task_id = simpledialog.askinteger("Input", "Entrez l'ID de la tâche à supprimer:")
    for i, task in enumerate(todo_list):
        if task['id'] == task_id:
            del todo_list[i]
            messagebox.showinfo("Info", f"Tâche supprimée avec l'ID {task_id}.")
            view_tasks(todo_list, listbox)
            return
    messagebox.showerror("Error", f"Aucune tâche trouvée avec l'ID {task_id}.")

def save_tasks(todo_list):
    with open(FILENAME, "w") as file:
        json.dump(todo_list, file)
    messagebox.showinfo("Info", "Tâches sauvegardées.")

def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            todo_list = json.load(file)
        messagebox.showinfo("Info", "Tâches chargées.")
    else:
        messagebox.showinfo("Info", "Aucun fichier trouvé. Une nouvelle liste de tâches sera créée.")
        todo_list = []
    return todo_list

def main():
    root = tk.Tk()
    root.title("To-Do List")

    todo_list = load_tasks()

    frame = tk.Frame(root)
    frame.pack(pady=20)

    listbox = tk.Listbox(frame, width=50)
    listbox.pack()

    view_tasks(todo_list, listbox)

    btn_add = tk.Button(root, text="Ajouter une tâche", command=lambda: add_task(todo_list, listbox))
    btn_add.pack(fill=tk.X)

    btn_view = tk.Button(root, text="Voir toutes les tâches", command=lambda: view_tasks(todo_list, listbox))
    btn_view.pack(fill=tk.X)

    btn_update = tk.Button(root, text="Modifier une tâche", command=lambda: update_task(todo_list, listbox))
    btn_update.pack(fill=tk.X)

    btn_delete = tk.Button(root, text="Supprimer une tâche", command=lambda: delete_task(todo_list, listbox))
    btn_delete.pack(fill=tk.X)

    btn_save = tk.Button(root, text="Sauvegarder les tâches", command=lambda: save_tasks(todo_list))
    btn_save.pack(fill=tk.X)

    btn_quit = tk.Button(root, text="Quitter", command=lambda: (save_tasks(todo_list), root.destroy()))
    btn_quit.pack(fill=tk.X)

    root.mainloop()

if __name__ == "__main__":
    main()

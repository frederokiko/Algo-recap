import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk
from PIL import Image, ImageTk
import json
import os

# Chemin du fichier de sauvegarde
FILENAME = "todo_list.txt"

# Taille des icônes
ICON_SIZE = (32, 32)

def add_task(todo_list, tree):
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
    tree.insert("", tk.END, values=(task['id'], task['date'], task['name'], task['description']))
    messagebox.showinfo("Info", f"Tâche ajoutée avec l'ID {new_id}.")

def view_tasks(todo_list, tree):
    for i in tree.get_children():
        tree.delete(i)
    if not todo_list:
        tree.insert("", tk.END, values=("Aucune tâche trouvée.", "", "", ""))
    else:
        for task in todo_list:
            tree.insert("", tk.END, values=(task['id'], task['date'], task['name'], task['description']))

def update_task(todo_list, tree):
    task_id = simpledialog.askinteger("Input", "Entrez l'ID de la tâche à modifier:")
    for task in todo_list:
        if task['id'] == task_id:
            task['date'] = simpledialog.askstring("Input", f"Entrez la nouvelle date de rendez-vous pour l'ID {task_id} (actuelle: {task['date']}):")
            task['name'] = simpledialog.askstring("Input", f"Entrez le nouveau nom pour l'ID {task_id} (actuel: {task['name']}):")
            task['description'] = simpledialog.askstring("Input", f"Entrez la nouvelle description pour l'ID {task_id} (actuelle: {task['description']}):")
            messagebox.showinfo("Info", f"Tâche mise à jour pour l'ID {task_id}.")
            view_tasks(todo_list, tree)
            return
    messagebox.showerror("Error", f"Aucune tâche trouvée avec l'ID {task_id}.")

def delete_task(todo_list, tree):
    task_id = simpledialog.askinteger("Input", "Entrez l'ID de la tâche à supprimer:")
    for i, task in enumerate(todo_list):
        if task['id'] == task_id:
            del todo_list[i]
            messagebox.showinfo("Info", f"Tâche supprimée avec l'ID {task_id}.")
            view_tasks(todo_list, tree)
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
    frame.pack(pady=20, fill=tk.BOTH, expand=True)

    tree = ttk.Treeview(frame, columns=("ID", "Date", "Nom", "Description"), show='headings')
    tree.heading("ID", text="ID")
    tree.heading("Date", text="Date")
    tree.heading("Nom", text="Nom")
    tree.heading("Description", text="Description")

    tree.column("ID", anchor=tk.CENTER, width=50)
    tree.column("Date", anchor=tk.CENTER, width=100)
    tree.column("Nom", anchor=tk.CENTER, width=150)
    tree.column("Description", anchor=tk.CENTER, width=300)

    tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    view_tasks(todo_list, tree)

    button_frame = tk.Frame(root)
    button_frame.pack(fill=tk.X, pady=10)

    icons = {}
    for action in ["add", "view", "update", "delete", "save", "quit"]:
        image = Image.open(f"{action}.png").resize(ICON_SIZE, Image.Resampling.LANCZOS)
        icons[action] = ImageTk.PhotoImage(image)

    btn_add = tk.Button(button_frame, text=" Ajouter une tâche", image=icons["add"], compound=tk.LEFT, command=lambda: add_task(todo_list, tree))
    btn_add.pack(fill=tk.X, pady=5)

    # btn_view = tk.Button(button_frame, text=" Voir toutes les tâches", image=icons["view"], compound=tk.LEFT, command=lambda: view_tasks(todo_list, tree))
    # btn_view.pack(fill=tk.X, pady=5)

    btn_update = tk.Button(button_frame, text=" Modifier une tâche", image=icons["update"], compound=tk.LEFT, command=lambda: update_task(todo_list, tree))
    btn_update.pack(fill=tk.X, pady=5)

    btn_delete = tk.Button(button_frame, text=" Supprimer une tâche", image=icons["delete"], compound=tk.LEFT, command=lambda: delete_task(todo_list, tree))
    btn_delete.pack(fill=tk.X, pady=5)

    # btn_save = tk.Button(button_frame, text=" Sauvegarder les tâches", image=icons["save"], compound=tk.LEFT, command=lambda: save_tasks(todo_list))
    # btn_save.pack(fill=tk.X, pady=5)

    btn_quit = tk.Button(button_frame, text=" Quitter", image=icons["quit"], compound=tk.LEFT, command=lambda: (save_tasks(todo_list), root.destroy()))
    btn_quit.pack(fill=tk.X, pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()


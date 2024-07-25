from contact_model import *

class Interface:
    """
        Classe Interface qui permet de gérer l'affichage et la partie UI
    """
    def __init__(self, manager):
        self.manager = manager
    
    def show_menu(self):
        menu = {
            1 : 'Ajouter un contact',
            2 : 'Afficher les contact',
            'Q' : 'Quitter'
        }
        
        print('¤¤¤ Carnet d\'adresse ¤¤¤\n')
        
        for key, value in menu.items():
            print(key, value, sep=' ')
        
        choice = input('\nFaites un choix > ')

        return choice

    def show_contacts_list(self):
        print('\n|° Liste des contacts °|\n')

        for key, value in self.manager.get_list().items():
            print(key, value['firstname'], value['lastname'], sep=' ')
        print('Q : Retour')
        
        choice = input('\nChoisissez un contact > ')
        return choice

    def show_contact(self, contact):
        contact = self.manager.get(contact)

        if not contact:
            return None

        print('\n|° Fiche °|\n')
        
        print(contact)
        
        print('\n--------\n1 : Modifier')
        print('2 : Supprimer')
        print('Q : Retour\n--------')

        choice = input('\nQue voulez-vous faire ? > ')
        return choice 

    def create(self):
        print('\n|° Creation Fiche °|\n')

        firstname = input("Prénom : ")
        lastname = input("Nom : ")
        telephone = input("Téléphone : ")
        email = input("Mail : ")

        person = Person(firstname, lastname, telephone, email)
        self.manager.create(person)

    def update(self, contact_id):
        contact = self.manager.get(contact_id)

        if not contact:
            return

        print('\n|° Modification Fiche °|\n')

        firstname = input(f"Prénom ({contact.firstname}) : ") or contact.firstname
        lastname = input(f"Nom ({contact.lastname}) : ") or contact.lastname
        telephone = input(f"Téléphone ({contact.telephone}) : ") or contact.telephone
        email = input(f"Email ({contact.email}) : ") or contact.email

        contact.update(firstname, lastname, telephone, email)
        self.manager.update(contact_id, contact)
    
    def delete(self, contact_id):
        self.manager.delete(contact_id)
        print(f"Contact {contact_id} supprimé")
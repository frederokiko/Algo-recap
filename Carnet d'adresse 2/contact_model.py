class Person:
    """
        Classe contenant l'entité personne avec ses infos
    """

    def __init__(self, firstname, lastname, telephone, email):
        self.lastname = lastname
        self.firstname = firstname
        self.telephone = telephone
        self.email = email
    
    def __str__(self) -> str:
        return f"Prénom : {self.firstname}\nNom : {self.lastname}\nTéléphone : {self.telephone}\nMail : {self.email}"
    
    def update(self, firstname=None, lastname=None, telephone=None, email=None):
        if firstname:
            self.firstname = firstname
        if lastname:
            self.lastname = lastname
        if telephone:
            self.telephone = telephone
        if email:
            self.email = email
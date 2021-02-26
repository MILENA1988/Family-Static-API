
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [
            {
                "id": self._generateId(),
                "first_name": "Michael",
                "last_name": last_name
            }
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, first_name, age, lucky_numbers):

        new_member={
             "id": self._generateId(),
                "first_name": first_name,
                "last_name": self.last_name,
                "age": age,
                "lucky_numbers": lucky_numbers,
            
        }
        
        self._members.append(new_member)
        return self._members
        pass

    def delete_member(self, id): 
        status=False
        for i,item in enumerate(self._members,start=0):  #  pasa dos parametros a todos los miembros
            if item["id"] == id:  #del id que se le esta pasando es igual al id que tengo en esa posición,
                self._members.pop(i) #con el pop, me elimina esa posición 
                status=True  #si es v o f, si es v lo sacas
        return status
     

    def get_member(self, id):  #self llamarse asi mismo
        for i in self._members:
            if i["id"] ==int(id): #castear expliqueme !!!!!!!
                return i
        
                

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members

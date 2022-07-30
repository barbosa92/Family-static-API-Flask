
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
        self._members = [{
            "id": self.generateId(),
            "first_name": "Jhon",
            "last_name": str(last_name),
            "age": int(33),
            "lucky_numbers": [7, 13, 22]
        },
        {
            "id": self.generateId(),
            "first_name": "Jane",
            "last_name": str(last_name),
            "age": int(35),
            "lucky_numbers": [10, 14]
        },
        {
            "id": self.generateId(),
            "first_name": "Jimmy",
            "last_name": str(last_name),
            "age": int(5),
            "lucky_numbers": [1]
        }
       
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def generateId(self):
        return randint(0, 100)

    def add_member(self, member):
        ## you have to implement this method
        ## append the member to the list of _members
        members = self._members
        
        members.append(member)
        return "Miembro añadido"

    def delete_member(self, id):
        ## you have to implement this method
        ## append the member to the list of _members
        members = self._members
        for obj in members:
            if obj['id'] == id:
                print(obj)
                index = members.index(obj)
                print(index)
                members.remove(obj)
                print(members)
                return "Member removed"

    def update_member(self, id, member):
        ## you have to implement this method
        ## loop the list and replace the member with the given id
        # print("Entra en update_member")
        # print(id)
        # print(member)
        members = self._members
        for obj in members:
            if obj['id'] == id:
                # print("Encuentra un id")
                # print(obj)
                # print(obj['first_name'])
                # print(member['first_name'])
                for key, value in member.items():
                    # print("Entra en el bucle")
                    # print(key)
                    # print(value)

                    if key == "first_name" and value != None:
                        obj['first_name'] = member['first_name']

                    elif key == "age" and value != None:
                        obj['age'] = member['age']
                        
                    elif key == "lucky_numbers" and value != None:
                        obj['lucky_numbers'] = member['lucky_numbers']
                        return "Modified"
                        
                    else:
                        return "No se ha modificado ningún campo"
                
            else:
                return "No se ha encontrado ningún miembro con ese id"

    def get_member(self, id):
        ## you have to implement this method
        ## loop all the members and return the one with the given id
        members = self._members
        for obj in members:
            if obj['id'] == id:
                position = members.index(obj)
                member = members[position]
                # print(member)
                return member

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members

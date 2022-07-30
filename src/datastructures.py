
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
        return randint(0, 10)

    def add_member(self, member):
        ## you have to implement this method
        ## append the member to the list of _members
        members = self._members
        
        members.append(member)
        return "Miembro añadido"

    def delete_member(self, id):
        ## you have to implement this method
        ## append the member to the list of _members
        pass

    def update_member(self, id, member):
        ## you have to implement this method
        ## loop the list and replace the member with the given id
        pass

    def get_member(self, id):
        ## you have to implement this method
        ## loop all the members and return the one with the given id
        members = self._members
        for obj in members:
            if obj['id'] == id:
                position = members.index(obj)
                member = members[position]
                print(member)
                return member

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members

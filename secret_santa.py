import random

class Secret_Santa:
    def __init__(self, people=""):
        if isinstance(people, str):
            self.people = self._string_to_list(people)
        elif isinstance(people, list):
            # Normalize and strip names in case they have spaces
            self.people = [name.strip() for name in people if str(name).strip()]
        else:
            raise TypeError("People must be a string or a list of names")
        
        self.__pairs = {}
        self.validate_names(self.people)

    def __add__(self, new_value):
        combined = self.people + self._string_to_list(new_value)
        self.validate_names(combined)
        return Secret_Santa(combined)
    
    def __iadd__(self, new_value):
        if isinstance(new_value, str):
            self.people += self._string_to_list(new_value)
        elif isinstance(new_value, list):
            # Normalize and strip names in case they have spaces
            self.people += [name.strip() for name in new_value if str(name).strip()]
        else:
            raise TypeError("People must be a string or a list of names")
        
        return self.validate_names(self.people)
    
    def __str__(self):
        return self.generate_formatted_list(self.people)
    
    def append(self, new_value):
        combined = self.people + self._string_to_list(new_value)
        self.validate_names(combined)
        self.people = combined
    
    def _string_to_list(self, people):
        return [name.strip() for name in people.split(",") if name.strip()]

    def validate_names(self, combined):
        if len(combined) != len(set(combined)):
            raise DuplicateNameException("Duplicate names were detected")
        return True

    def set_pair(self, giver, recipient):
        if giver == recipient:
            raise ValueError("Giver and recipient must be different")
        if giver not in self.people or recipient not in self.people:
            raise ValueError("Both names must be in the unpaired pool")
        if giver in self.__pairs:
            raise ValueError(f"{giver} is already paired")
        if recipient in self.__pairs.values():
            raise ValueError(f"{recipient} is already assigned as a recipient")
        
        self.__pairs[giver] = recipient
        self.people.remove(giver)
        self.people.remove(recipient)

    def delete_pair(self, giver):
        recipient = self.__pairs[giver]
        
        self.people.append(giver)
        self.people.append(recipient)
        self.__pairs.pop(giver)

    def view_pairs(self):
        return self.__pairs

    def create_secret_santa_list(self, from_people):
        if len(from_people) < 2:
            raise InsufficientNamesException("Need at least 2 participants")
        
        to_people = from_people[:]
        n = len(to_people)
        
        for i in range(n-1, 0, -1):            
            j = random.randrange(i)
            to_people[i], to_people[j] = to_people[j], to_people[i]
        for g, r in self.__pairs.items():
            from_people.append(g)
            to_people.append(r)
        return list(zip(from_people, to_people))
    
    def generate_formatted_string(self, giver, receiver) -> str:
        return f"{giver} 👉 {receiver}\n"

    def generate_formatted_list(self, from_people):
        secret_santa_list = self.create_secret_santa_list(from_people)
        formatted_list = ""
        for giver, receiver in secret_santa_list:
            formatted_list += self.generate_formatted_string(giver, receiver)
        
        return formatted_list.strip()
    
class DuplicateNameException(Exception):
    """Raised when a list contains duplicate name values"""
    pass

class InsufficientNamesException(Exception):
    """Raised when a list contains fewer than two valid names"""
    pass
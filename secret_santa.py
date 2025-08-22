import random

class Secret_Santa:
    def __init__(self, people=""):
        self.people = self._string_to_list(people)

    def __add__(self, new_value):
        combined = self.people + self._string_to_list(new_value)
        self.validate_names(combined)
        return self.people + self._string_to_list(new_value)
    
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

    def create_secret_santa_list(self, from_people):
        if len(from_people) < 2:
            raise InsufficientNamesException("Need at least 2 participants")
        
        to_people = from_people[:]

        while True:
            random.shuffle(to_people)
            pairs = list(zip(from_people, to_people))
            if all(a != b for a, b in pairs):
                return pairs

    def generate_formatted_list(self, from_people):
        secret_santa_list = self.create_secret_santa_list(from_people)
        formatted_list = ""
        for giver, receiver in secret_santa_list:
            formatted_list += f"{giver} 👉 {receiver}\n"
        
        return formatted_list.strip()
    
class DuplicateNameException(Exception):
    """Raised when a list contains duplicate name values"""
    pass

class InsufficientNamesException(Exception):
    """Raised when a list contains fewer than two valid names"""
    pass
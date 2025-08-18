import os
import random

def main():
    people = []
    
    while True:
        if len(people) > 0:
            print("Secret Santas: " + ", ".join(people))
        
        person = input("Enter name: ").strip()

        if person == "":
            secret_santa_list = create_secret_santa_list(people)
            print(generate_formatted_list(secret_santa_list))
            break
        
        if validate_name(person, people):
            people.append(person)
            clear_text()
        else:
            print(f"{person} is already in the Secret Santa list!")

def validate_name(new_name, people):
    if new_name in people:
        return False
    return True

def create_secret_santa_list(from_people):
    secret_santa_list = {}
    exclude_list = []

    for person in from_people:
        selected_index = random_exclude(0, len(from_people) - 1, exclude_list)
        exclude_list.append(selected_index)
        secret_santa_list.update({person: from_people[selected_index]})
        
    return secret_santa_list

def random_exclude(start, end, exclude):
    choices = [i for i in range(start, end + 1) if i not in exclude]
    if not choices:
        raise ValueError("No valid numbers to choose from.")
    return random.choice(choices)

def generate_formatted_list(secret_santa_list):
    formatted_list = ""
    for giver, reciever in secret_santa_list.items():
        formatted_list += f"{giver} 👉 {reciever}\n"
    
    return formatted_list.strip()


def clear_text():
    os.system('cls' if os.name=='nt' else 'clear')

if __name__ == "__main__":
    main()


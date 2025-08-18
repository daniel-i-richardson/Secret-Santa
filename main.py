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

def test_main():
    people = ["Jim", "Brenda", "Katie", "Nathan", "Hannah", "Zachary"]

    for i in range(10):
        ss_list = create_secret_santa_list(people)
        print(generate_formatted_list(ss_list))
        print("\n\n")

def validate_name(new_name, people):
    if new_name in people:
        return False
    return True

def create_secret_santa_list(from_people):
    if len(from_people) < 2:
        raise ValueError("Need at least 2 participants")
    
    to_people = from_people[:]

    while True:
        random.shuffle(to_people)
        secret_santa_list = zip(from_people, to_people)
        if all(a != b for a, b in secret_santa_list):
            return dict(secret_santa_list)
        else:
            random.shuffle(to_people)

def generate_formatted_list(secret_santa_list):
    formatted_list = ""
    for giver, reciever in secret_santa_list.items():
        formatted_list += f"{giver} 👉 {reciever}\n"
    
    return formatted_list.strip()


def clear_text():
    os.system('cls' if os.name=='nt' else 'clear')

if __name__ == "__main__":
    main()


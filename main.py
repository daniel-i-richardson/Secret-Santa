import os
import random

def main():
    people = []
    
    while True:
        if len(people) > 0:
            print("Secret Santas: " + ", ".join(people))
        
        person = input("Enter name: ").strip()

        if person == "":
            recipients = create_secret_santa_list(people)
            print(generate_formatted_list(people, recipients))
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
    to_people = []
    exclude_list = []

    for person in from_people:
        selected_index = random_exclude(0, len(from_people) - 1, exclude_list)
        to_people.append(from_people[selected_index])
        exclude_list.append(selected_index)

    return to_people

def generate_formatted_list(from_people, to_people):
    if len(from_people) is not len(to_people):
        print("ERROR: List lengths do not match")
        return

    formatted_list = ""
    for giver, reciever in zip(from_people, to_people):
        formatted_list += f"{giver} 👉 {reciever}\n"
    
    return formatted_list.strip()


def clear_text():
    os.system('cls' if os.name=='nt' else 'clear')


def random_exclude(start, end, exclude):
    choices = [i for i in range(start, end + 1) if i not in exclude]
    if not choices:
        raise ValueError("No valid numbers to choose from.")
    return random.choice(choices)

if __name__ == "__main__":
    main()

class Test:
    def test_randomization():
        name_list = [Jim, Brenda, Katie, Matt, Daniel, Susanna]
        
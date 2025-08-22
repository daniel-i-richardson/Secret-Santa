import os
from secret_santa import Secret_Santa, DuplicateNameException, InsufficientNamesException

def main():
    ss = Secret_Santa()
    
    while True:
        person = ""
        if len(ss.people) > 0:
            print("Secret Santas: " + ", ".join(ss.people))

        try:
            person = input("Enter name: ").strip()
            ss.append(person)

            clear_text()
        except DuplicateNameException:
            print("You're attempting to add a name that already exists in the Secret Santa list.")
        
        if person == "":
            try:
                print(ss)
                break
            except InsufficientNamesException:
                print("Your Secret Santa list must contain two or more participants")

        
        


def test_main():
    people = ["Jim", "Brenda", "Katie", "Nathan", "Hannah", "Zachary"]

    for i in range(10):
        ss_list = create_secret_santa_list(people)
        print(generate_formatted_list(ss_list))
        print("\n\n")


def clear_text():
    os.system('cls' if os.name=='nt' else 'clear')

if __name__ == "__main__":
    main()


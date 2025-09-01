import os
from secret_santa import Secret_Santa, DuplicateNameException, InsufficientNamesException

def main():
    ss = Secret_Santa()
    
    while True:
        user_input = ""
        print("Menu:\n1: View paired names\n2: Add name pair\n3: Delete name pair")
        if len(ss.people) > 0:
            print("Secret Santas: " + ", ".join(ss.people))
        
        user_input = input("Enter name: ").strip()
        match user_input:
            case "1":
                add_pair()
            case "2":
                delete_pair()
            case "2":
                view_pair()
            case "":
                try:
                    print(ss)
                    break
                except InsufficientNamesException:
                    print("Your Secret Santa list must contain two or more participants")
            case _:
                try:                    
                    ss.append(user_input)
                    clear_text()
                except DuplicateNameException:
                    print("You're attempting to add a name that already exists in the Secret Santa list.")
            

        
def add_pair():
    #Code Here

def view_pair():
    #Code Here

def delete_pair():
    #Code Here


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


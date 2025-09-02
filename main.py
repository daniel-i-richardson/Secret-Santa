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
                view_pairs(ss)
            case "2":
                add_pair(ss)
                clear_text()
            case "3":
                delete_pair(ss)
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
            

        
def add_pair(ss: Secret_Santa):
    while True:
        giver = input("Enter giver: ").strip()
        recipient = input("Enter recipient: ").strip()

        if giver not in ss.people and recipient not in ss.people:
            print("Giver/Receiver names are not valid. Please try again.")
        else:
            ss.set_pair(giver, recipient)
            break

def view_pairs(ss: Secret_Santa):
    print("Giver/Recipient Pairs:\n")
    pair_list = ss.view_pairs()
    for giver, recipient in pair_list.items():
        print(ss.generate_formatted_string(giver, recipient))

def delete_pair(ss: Secret_Santa):
    giver = input("Enter giver: ").strip()
    ss.delete_pair(giver)

def clear_text():
    os.system('cls' if os.name=='nt' else 'clear')

if __name__ == "__main__":
    main()


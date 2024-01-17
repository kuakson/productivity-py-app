from modules import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is ", now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        chore = user_action[4:]

        chore_list = functions.get_chore_list()

        chore_list.append(chore + "\n")

        functions.write_chore_list(chore_list)

    elif user_action.startswith('show'):
        chore_list = functions.get_chore_list()

        # LIST COMPREHENSION
        # new_chore_list = [item.strip('\n') for item in chore_list]

        for index, item in enumerate(chore_list):
            item = item.strip('\n')
            print(f"{index + 1}. {item.capitalize()}")

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number -= 1

            chore_list = functions.get_chore_list()

            new_chore = input("Write new chore: ")
            chore_list[number] = new_chore + '\n'

            functions.write_chore_list(chore_list)

        except ValueError:
            print("Wrong command")
            continue

    elif user_action.startswith('complete'):
        try:
            completed_chore = int(user_action[9:])

            chore_list = functions.get_chore_list()

            index = completed_chore - 1
            chore_to_remove = chore_list[index].strip('\n')
            chore_list.pop(index)

            functions.write_chore_list(chore_list)

            message = f"Chore {chore_to_remove} was removed from the list"
            print(message)
        except ValueError:
            print("Wrong command")
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print("Wrong action")

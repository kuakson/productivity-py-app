def get_chore_list(filepath="chore_list.txt"):
    with open(filepath, 'r') as file_local:
        chore_list_local = file_local.readlines()
    return chore_list_local


def write_chore_list(chore_list_arg, filepath="chore_list.txt"):
    with open(filepath, 'w') as file_local:
        file_local.writelines(chore_list_arg)


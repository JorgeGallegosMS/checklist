checklist = list()

# CREATE
def create(item):
    checklist.append(item)

# READ
def read(index):
    return checklist[index]

# UPDATE
def update(index, item):
    checklist[index] = item

# DESTROY
def destroy(index):
    return checklist.pop(index)

def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}\n".format(index, list_item))
        index += 1

def mark_completed(index):
    item = checklist[index]
    if item[0] != "√":
        checked = "√" + checklist[index]
        update(index, checked)
        return item
    else:
        item.pop(0)
        return item

def select(function_code):
    # Create item
    if function_code.upper() == 'C':
        input_item = user_input("Input item: ")
        create(input_item)

    # Read item
    elif function_code.upper() == 'R':
        item_index = int(user_input("Index number? "))

        if item_index not in range(len(checklist)):
            print("Error: Invalid index\n")
        else:
            print(read(item_index))
            print("\n")

    # Print all items
    elif function_code.upper() == "P":
        list_all_items()

    elif function_code.upper() == "U":
        list_all_items()
        item_index = int(user_input("Which index would you like to update? "))
        if item_index not in range(len(checklist)):
            print("Erorr: {} is not a valid index\n".format(item_index))
            return True
        new_item = user_input("New item: ")
        update(item_index, new_item)
        list_all_items()

    elif function_code.upper() == "D":
        list_all_items()
        item_index = int(user_input("What index would you like to delete?"))

        if item_index not in range(len(checklist)):
            print("Error: Invalid index\n")
        else:
            removed = destroy(item_index)
            print("{} has been removed from the list\n".format(removed))
            list_all_items()

    elif function_code.upper() == "M":
        mark_completed()

    elif function_code.upper() == "Q":
        return False

    else:
        print("Error: Unknown Option\n")

    return True

def user_input(prompt):
    user_input = input(prompt)
    return user_input

def test():
    select("C")
    list_all_items()
    select("R")
    list_all_items()

#test()

running = True

while running:
    selection = user_input("Press C to add to list, R to Read from list, M to mark/unmark an item, U to update an item in the list, D to delete an item, P to display the entire list and Q to quit\n")
    running = select(selection)

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
    if index not in range(len(checklist)):
        print("Error: Item number {} does not exist\n".format(index))
    else:
        # check item if unchecked
        if item[0] != "√":
            checked = "√" + checklist[index]
            update(index, checked)
            print("{} was checked\n".format(item))
            return item
        # uncheck checked item
        else:
            item = item[1:]
            update(index, item)
            print("{} was unchecked\n".format(item))
            return item

def select(function_code):
    # Create item
    if function_code.upper() == 'C':
        input_item = user_input("New item: ")
        create(input_item)
        list_all_items()

    # Read item
    elif function_code.upper() == 'R':
        item_index = int(user_input("Item number? "))

        if item_index not in range(len(checklist)):
            print("Error: Item number {} does not exist\n".format(index))
        else:
            print(read(item_index))
            print("\n")

    # Print all items
    elif function_code.upper() == "P":
        if len(checklist) > 0:
            list_all_items()
        else:
            print("No items in the list\n")

    elif function_code.upper() == "U":
        list_all_items()
        item_index = int(user_input("Which item number would you like to update? "))
        if item_index not in range(len(checklist)):
            print("Error: Item number {} does not exist\n".format(index))
            return True
        new_item = user_input("New item: ")
        update(item_index, new_item)
        list_all_items()

    # Delete an item
    elif function_code.upper() == "D":
        list_all_items()
        item_index = int(user_input("What item number would you like to delete?"))

        if item_index not in range(len(checklist)):
            print("Error: Item number {} does not exist\n".format(index))
        else:
            removed = destroy(item_index)
            print("{} has been removed from the list\n".format(removed))
            list_all_items()

    # Mark an item as complete
    elif function_code.upper() == "M":
        index = int(input("What item number would you like to mark/unmark?"))
        mark_completed(index)
        list_all_items()

    elif function_code.upper() == "Q":
        return False

    else:
        print("Error: Unknown Option\n")

    return True

def user_input(prompt):
    user_input = input(prompt)
    return user_input

def test():
    select("c")
    list_all_items()
    select("c")
    list_all_items()
    select("m")
    list_all_items()

# test()

running = True

while running:
    selection = user_input("Press C to add to list, R to Read from list, M to mark/unmark an item, U to update an item in the list, D to delete an item, P to display the entire list and Q to quit\n")
    running = select(selection)

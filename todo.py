import datetime
import time
from typing import TextIO
import os

# add a header to other_info and always display the header when you display the lists?
# arrange the info when you display the lists with split at comma and join with another character? (see above)

print("\n\t\tHi,", os.getlogin(), "! Let's begin!\n")


def save_category(text: str) -> TextIO:     # not sure what TextIO is...
    with open("categories.txt", "r+") as file1:
        temp_list = []
        for line_cat in file1.read().splitlines():  # made with temporary list because I had issues with partial words
            temp_list.append(line_cat)
        if text in temp_list:
            print(f"\nCategory <{text.upper()}> is already saved on file!\n")
            pass
        else:
            file1.write(f"{text}\n")
    return file1


def delete_q() -> TextIO:
    with open("categories.txt", "r+") as file2:
        data = file2.readlines()
        file2.seek(0)    # sets the cursor at the top of the file
        for i in data:
            if i.strip('\n') != "q":    # rewrites the file without that one "q"
                file2.write(i)
        file2.truncate()     # deletes the rest of the file after the last "q"
    return file2


def adding_to_category(task: str) -> str:
    while search_in_categories_list(task) is False:
        task = input(" \n |>>> ")
    print(f'\n Task added to "{task.upper()}" category!')
    return task


def save_other_info(task: str, person: str, category: str,
                    date: datetime = (datetime.datetime.today() + datetime.timedelta(days=1))) -> dict:
    data = {"task": task, "date": date, "person": person, "category": category}
    with open("other_info.txt", "a+") as file4:
        file4.write(task+","+person+","+category+","+str(date)+"\n")
    return data


def display_categories_from_file():
    with open("categories.txt", "r") as file3:
        for position, line8 in enumerate(file3.readlines(), start=1):
            print(f"{position} - {line8.strip().upper()}")
            time.sleep(0.5)


def search_in_categories_list(text: str) -> bool:
    with open("categories.txt", "r+") as file1:
        temp_list = []
        for line_cat in file1.read().splitlines():  # made with temporary list because I had issues with partial words
            temp_list.append(line_cat.lower())
        if text.lower() in temp_list:
            print(f"\nCategory <{text.upper()}> found!")
            categories_search_result = True
        else:
            print(f"Category <{text.upper()}> does not exist. Please try again!")
            categories_search_result = False
    return categories_search_result


def delete_line(line_number: int) -> list:
    with open("other_info.txt", "r+") as file_for_deletion:
        lines = file_for_deletion.readlines()
        file_for_deletion.close()
        del lines[line_number]
        print(f"\n\t\tLine [{line_number}] has been deleted!")
        updated_file_after_deletion = open("other_info.txt", "w+")
        for line5 in lines:
            updated_file_after_deletion.write(line5)

        updated_file_after_deletion.close()
    return lines


def amend_field(line_number: int, field_to_be_amended: int) -> TextIO:
    with open("other_info.txt", "r+") as file_for_amending:
        main_list_amending = []
        lines = file_for_amending.readlines()
        for line8 in lines:
            line8 = list(line8.split(","))
            main_list_amending.append(line8)
        file_for_amending.close()

        new_value = input("\nWhat is the new information (please type): \n |>>> ")
        main_list_amending[line_number][field_to_be_amended] = new_value.upper()

        updated_file_after_amending = open("other_info.txt", "w+")
        for line6 in main_list_amending:
            line6 = str(",".join(line6))
            updated_file_after_amending.write(str(line6))

        updated_file_after_amending.close()

    return updated_file_after_amending


def show_sort_filter_menu() -> dict:
    menu_options = {1: "print all data", 2: "sort by task (ascending)", 3: "sort by task (descending)",
                    4: "sort by date (ascending)", 5: "sort by date (descending)",
                    6: "sort by person (ascending)", 7: "sort by person (descending)",
                    8: "sort by category (ascending)", 9: "sort by category (descending)",
                    10: "filter by task", 11: "filter by date", 12: "filter by person", 13: "filter by category"}
    for m_key, v in menu_options.items():
        print("-" * 43)
        if m_key < 10 and len(v) % 2 == 0:
            print(
                f'({m_key}) {"*" * (int(18 - (len(v) / 2)))} {v.upper().strip()} {"*" * (int(18 - (len(v) / 2) + 1))}')
        elif m_key < 10 and len(v) % 2 != 0:
            print(f'({m_key}) {"*" * (int(18 - (len(v)/2)+1))} {v.upper().strip()} {"*" * (int(18 - (len(v)/2)+1))}')
        else:
            print(f'({m_key}) {"*" * (int(18 - (len(v) / 2)))} {v.upper().strip()} {"*" * (int(18 - (len(v) / 2)))}')
    return menu_options


def sort_data(sorter: int, asc_or_desc: bool) -> list:
    with open("other_info.txt", "r+") as display_data_file:
        main_list = []
        e = display_data_file.readlines()
        for line7 in e:
            line7 = list(line7.split(","))
            main_list.append(line7)

        sorted_list = sorted(main_list, key=lambda row: row[sorter], reverse=asc_or_desc)
        for line2 in sorted_list:
            print(line2)
        return sorted_list


def filter_data(filter_by: str, accurate: str) -> list:
    with open("other_info.txt", "r+") as filter_file:
        main_list_filter = []
        b = filter_file.readlines()
        if accurate.lower() == "y":
            for line3 in b:
                line3 = list(line3.split(","))  # for accurate searches
                main_list_filter.append(line3)
        else:
            for line3 in b:
                main_list_filter.append(line3)

        for line2 in main_list_filter:
            if filter_by in line2:
                print(line2)
    return main_list_filter


def data_display(operation_type: int) -> int:
    if operation_type == 1:
        with open("other_info.txt", "r") as file:
            for line4 in file.readlines():
                print(line4.strip())
    elif operation_type == 2:
        sort_data(0, False)
    elif operation_type == 3:
        sort_data(0, True)
    elif operation_type == 4:
        sort_data(1, False)
    elif operation_type == 5:
        sort_data(1, True)
    elif operation_type == 6:
        sort_data(2, False)
    elif operation_type == 7:
        sort_data(2, True)
    elif operation_type == 8:
        sort_data(3, False)
    elif operation_type == 9:
        sort_data(3, True)
    elif operation_type == 10:
        filter_data(filter_word, accurate_check)  # these aren't really needed since I search in all sub-lists
    elif operation_type == 11:
        filter_data(filter_word, accurate_check)  # can be pass (if I change line 230)
    elif operation_type == 12:
        filter_data(filter_word, accurate_check)  # can be pass (if I change line 230)
    elif operation_type == 13:
        filter_data(filter_word, accurate_check)  # can be pass (if I change line 230)
    else:
        print("Invalid selection. Please try again!")
        pass
    return operation_type


categories_list = []
# categories = str(input('Please type your "to do" categories (Press Q to stop): \n |>>> '))
# categories_list.append(categories.title().strip())
# save_category(categories)

while True:
    categories = str(input('Please type your "TO DO" categories (Press Q to move to the next step): \n |>>> '))
    if categories.title().strip() in categories_list:
        print(f'\n\tCategory <{categories.upper()}> already exists. Please try another!\n')
    elif categories.strip() == "":
        print("A category cannot be empty or space. Please type a category or press Q to exit.")
    else:
        categories_list.append(categories.title().strip())
        save_category(categories)
    if categories.lower() == "q":
        categories_list.pop()
        delete_q()
        break


print('\nPress "R" to see your recent categories or "A" to see all categories (saved on file):')
time.sleep(1)
wait_for_user = input(" \n |>>> ")
if wait_for_user.lower() == "a":
    display_categories_from_file()
elif wait_for_user.lower() == "r":
    display_list_and_select = [print(x, f'{"-" * (30 - (len(x)))}-> ', [position]) for position, x in
                               enumerate(categories_list, start=1)]
else:
    print("Categories will not be displayed! Continuing...")
    pass
print("\n")

while True:
    task_text = input("\n\t\t\t\tPlease add your task (Press Q to exit): \n |>>> ")
    with open("other_info.txt", "r+") as file_t:
        check_duplicate_task = []
        lines_t = file_t.readlines()
        for line_t in lines_t:
            check_duplicate_task.append(line_t.split(",")[0])

        first_column = []
        for line_index in range(len(lines_t)):
            first_column.append(check_duplicate_task[line_index])

        # print(first_item_each_line)
    if task_text.lower() == "q":
        print("\nSee you later!")
        break

    if task_text.upper() in first_column:
        print("\nThis task is already in the system. Please try another one!\n")
        continue
    file_t.close()

    try:
        task_date = datetime.datetime(int(input("\nTo complete by: \t\n |>>> Year: ")),
                                      int(input(" |>>> Month: ")),
                                      int(input(" |>>> Day: ")),
                                      int(input("\t |>>> Hour: ")),
                                      int(input("\t |>>> Minute: ")))
    except ValueError:
        print("\nIncorrect date. Please try again!")
        continue

    assigned_to = input("\nWho will be responsible for this task (type name)? \n |>>> ")
    print("\nWhat category would you like to place this task into (type the category name)?\n")
    display_categories_from_file()
    time.sleep(0.5)
    task_category = input(" \n |>>> ")  # If I don't declare it here, I get an error message
    task_category = adding_to_category(task_category)   # forces task_category to update...
    # adding_to_category(task_category)   # and the updated value is used here and added to the file on drive
    save_other_info(task_text.upper(), assigned_to.upper(), task_category.upper(), task_date)   # sorting issues 1, A, a


while True:
    ask_if_view_sort_data = input('\nDo you wish to visualise/SORT the data on file ("Y" for Yes or '
                                  'any key to exit)?: \n |>>> ')
    if ask_if_view_sort_data.lower() == "y":
        show_sort_filter_menu()
        user_selection_for_operation = int(input("\nPlease select a number from the menu: \n |>>> "))
        data_display(user_selection_for_operation)
    else:
        break

while True:
    ask_if_view_filter_data = input('\nDo you wish to visualise/FILTER the data on file ("Y" for Yes or '
                                    'any key to exit)?\n |>>> ')
    if ask_if_view_filter_data.lower() == "y":
        show_sort_filter_menu()
        filter_type = input("\nSelect a filter from the menu (number from list): \n |>>> ")
        filter_word = input("\nFilter by (please type word): \n |>>> ")
        accurate_check = input('\nPress "Y" for a 100% match or any other key for an approximate match: \n |>>> ')
        data_display(int(filter_type))  # or call filter_data function from here
    else:
        break


while True:
    ask_if_edit = input('\nDo you wish to EDIT a task ("Y" for Yes or any key to exit)?\n |>>> ')
    if ask_if_edit.lower() == "y":
        with open("other_info.txt", "r+") as edit_file:
            c = edit_file.readlines()
            longest_list = []
            for line in c:
                a = len(line)
                longest_list.append(a)
                line = list(line.split(","))
                continue
            m = max(longest_list) + 10
            print("\nThe list of items is:\n")
            print(f"LINE [x]" + " " * (int(m / 5) - 4), "TASK" + " " * (int(m / 5) - 4),
                  "PERSON" + " " * (int(m / 5) - 6), "CATEGORY"+ " " * (int(m / 5) - 8), "DATE" + " " * (int(m / 5) - 4))
            print("-" * m)
            display_edit_list = [print(f"Line [{position}] : {x}", end="") for position, x in enumerate(c, start=0)]

        type_of_edit = input('\nPress "A" to amend a task or "D" to delete it!\n |>>> ')
        if type_of_edit.lower() == "a":
            what_to_amend = int(input('Which line would you like to Amend?\n |>>> '))
            column_items = {"0": "Amend Task", "1": "Amend Person", "2": "Amend Category", "3": "Amend Date"}
            for key, value in column_items.items():
                print(f"{key} - {value}")
            column_to_amend = int(input("What would you like to amend (type number from the above list)?\n |>>> "))
            amend_field(what_to_amend, column_to_amend)
        elif type_of_edit.lower() == "d":
            what_to_delete = int(input('Which line to permanently Delete (first line has index 0)?\n |>>> '))
            delete_line(what_to_delete)
        else:
            print("You will go back to the previous menu.")
            time.sleep(1)
    else:
        print("Goodbye!")
        break

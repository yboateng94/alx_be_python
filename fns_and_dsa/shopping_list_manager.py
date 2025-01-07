# shopping list manager.py

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def add_item(Shopping_List):
    item = input("Enter the item to add: ").strip()
    Shopping_List.append(item)
    print(f" '{item}' has been added to the List.")

def remove_item(Shopping_List):
    item = input("Enter the item to remove: ").strip()
    if item in Shopping_List:
        Shopping_List.remove(item)
        print(f" '{item}' has been removed from the List.")
    else:
        print(f"Error: '{item}' not found in the List")


def view_the_list(Shopping_List):
    if Shopping_List:
        print("\nCurrent Shopping List:")
        for idx, item in enumerate(Shopping_List, start=1):
            print(f"{idx}. {item}")
    else:
        print("\nThe shopping list is empty.")

def main():
    Shopping_List = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_item(Shopping_List)
        elif choice == '2':
            remove_item(Shopping_List)
        elif choice == '3':
            view_the_list(Shopping_List)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Error: Invalid choice. Please choose a valid option.")
if __name__ == "__main__":
    main()


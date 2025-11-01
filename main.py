"""
File Name: main.py
Project Name: Linked List Demo
Author: Mehmet Mert Asma
Date Created: 10/29/2025
"""
import LinkedList as ll
def main():

    # Initialize empty ll
    head = None

    print("Linked List Demo")

    # Element insertion at thr end
    print("inserting elements at the end of the linked list")
    head = ll.insert_at_end(head, 25)
    head = ll.insert_at_end(head, 50)
    head = ll.insert_at_end(head, 75)

    # Element insertion at the beginning
    print("inserting elements at the beginning of the linked list")
    head = ll.insert_at_end(head, 100)
    head = ll.insert_at_end(head, 200)
    ll.display(head)


        # Get the length of the ll
    length = ll.get_length(head)
    print("Length of the linked list:", length)

    # Search for an element in the ll
    search_value = 50
    position = ll.search(head, search_value)
    if position != -1:
        print(f"Element {search_value} found at position {position}")
    else:
        print(f"Element {search_value} not found in the list")

    # Search for element that does not exist
    # (think abt using conditionial logic to handle this case)
    missing_value = 999
    position = ll.search(head, missing_value)
    if position == -1:
        print(f"Element {missing_value} does not exist in the list")

    # Delete an element in the ll
    delete_value = 75
    print(f"Deleting element {delete_value} from the linked list...")
    head = ll.delete_node(head, delete_value)
    ll.display(head)

    # Get the final length of the ll (think line 19)
    final_length = ll.get_length(head)
    print("Final length of the linked list:", final_length)

    if __name__ == "__main__":
        main()
from linked_list import LinkedList


def get_middle_node(head):
    slow = head  # Initialize slow pointer to head
    fast = head  # Initialize fast pointer to head

    # Move fast pointer two steps and slow pointer one step at a time
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # When fast pointer reaches the end, slow pointer will be at the middle
    return slow

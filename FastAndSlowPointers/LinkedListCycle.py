from linked_list import LinkedList

def detect_cycle(head):
    if not head:
        return False

    slow = head  # The slow pointer starts at the head
    fast = head  # The fast pointer also starts at the head

    while fast and fast.next:
        slow = slow.next  # Move the slow pointer by one step
        fast = fast.next.next  # Move the fast pointer by two steps

        if slow == fast:  # If the slow pointer and fast pointer meet, a cycle exists
            return True

    return False  # The fast pointer reached the end, so there is no cycle

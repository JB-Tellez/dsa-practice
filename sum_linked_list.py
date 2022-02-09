def sum_linked_list(node):
    if not node:
        return 0
        
    return node.value + sum_linked_list(node.next) if node else 0

def min_stack(stack):
    
    mine = stack.pop()

    if not stack:
        return mine

    further = min_stack(stack)

    return mine if mine < further else further


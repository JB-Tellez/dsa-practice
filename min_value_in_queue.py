def min_value(q):
    lowest = q.dequeue()
    while q:
        candidate = q.dequeue()
        if candidate < lowest:
            lowest = candidate

    return lowest

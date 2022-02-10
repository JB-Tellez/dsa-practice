from codefellows.dsa.binary_tree import BinarySearchTree


class Frame:
    LEFT = 0
    ROOT = 1
    RIGHT = 2
    DONE = 4

    def __init__(self, node):
        self.node = node
        self.action = Frame.LEFT

    def __repr__(self):
        return f"{self.node.value}:{self.action}"


class FrameStack:
    def __init__(self):
        self.storage = []

    def peek(self):
        return self.storage[-1]

    def pop(self):
        return self.storage.pop()

    def push(self, value):
        self.storage.append(Frame(value))

    def __len__(self):
        return len(self.storage)


def sort_tree(tree):

    values = []
    frame_stack = FrameStack()
    frame_stack.push(tree.root)

    while frame_stack:
        frame = frame_stack.peek()

        if frame.action == Frame.LEFT and frame.node.left:
            frame_stack.push(frame.node.left)

        elif frame.action == Frame.ROOT:
            values.append(frame.node.value)

        elif frame.action == Frame.RIGHT and frame.node.right:
            frame_stack.push(frame.node.right)

        elif frame.action == Frame.DONE:
            frame_stack.pop()
            continue

        frame.action += 1

    return values

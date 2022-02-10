from codefellows.dsa.binary_tree import BinarySearchTree
from sort_bst import sort_tree


def test_sort():

    unordered = [10, 5, 15, 3, 7, 12, 17]
    tree = BinarySearchTree(values=unordered)

    actual = sort_tree(tree)
    expected = sorted(unordered)

    assert actual == expected

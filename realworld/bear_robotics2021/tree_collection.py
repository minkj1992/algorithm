# https://coderbyte.com/information/Tree%20Constructor
from collections import defaultdict
from typing import List, Tuple, Dict


def is_binary_tree(arr: List[str]) -> bool:
    """
    1. #child > 2
    2. child's parent > 1
    3. multiple tree
    """
    p2c: dict = defaultdict(list)  # parent : [c1,c2..]
    c2p = {}  # child:parent

    for str_tuple in arr:
        child, parent = parse(str_tuple)

        if len(p2c[parent]) == 2:
            return False
        p2c[parent].append(child)

        if child in c2p:
            return False
        c2p[child] = parent

    return is_single_tree(p2c, c2p)


def parse(str_tuple: str) -> Tuple[int, int]:
    str_pair = str_tuple.split(",")
    child = int(str_pair[0][1:])
    parent = int(str_pair[1][:-1])
    return child, parent


def is_single_tree(p2c, c2p) -> bool:
    root = None
    for parent in p2c:
        if root not in c2p:
            if root:
                return False
            root = parent
    return True


# keep this function call here
answer = "true" if is_binary_tree(input()) else "false"
print(answer)

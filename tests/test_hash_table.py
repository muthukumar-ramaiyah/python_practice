import pytest

from hash_table import hash_function, add, contains, my_list

def test_hash_table_operations():
    assert hash_function('Bob') == (ord('B') + ord('o') + ord('b')) % 10
    assert hash_function('Alice') == (ord('A') + ord('l') + ord('i') + ord('c') + ord('e')) % 10
    add('Bob')
    add('Alice')
    add('Charlie')
    assert contains('Bob') == True
    assert contains('Alice') == True
    assert contains('Charlie') == True
    assert contains('David') == False
                                        
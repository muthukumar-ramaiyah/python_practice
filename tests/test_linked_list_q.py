# %%
import pytest
import os
import sys

# print(__file__)
# print(os.path.dirname(__file__))
# print(os.path.join(os.path.dirname(__file__), '../src'))
# sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))
# %%
from linked_list_q import Q

def test_q_operations():
    myQ = Q()
    assert myQ.is_empty() == True
    assert myQ.q_size() == 0

    myQ.append('A')
    assert myQ.first() == 'A'
    assert myQ.last() == 'A'
    assert myQ.is_empty() == False
    assert myQ.q_size() == 1

    myQ.append('B')
    assert myQ.first() == 'A'
    assert myQ.last() == 'B'
    assert myQ.q_size() == 2

    myQ.append('C')
    assert myQ.first() == 'A'
    assert myQ.last() == 'C'
    assert myQ.q_size() == 3

    assert myQ.remove() == 'A'
    assert myQ.first() == 'B'
    assert myQ.last() == 'C'
    assert myQ.q_size() == 2

    assert myQ.remove() == 'B'
    assert myQ.first() == 'C'
    assert myQ.last() == 'C'
    assert myQ.q_size() == 1

    assert myQ.remove() == 'C'
    assert myQ.is_empty() == True
    assert myQ.q_size() == 0

    with pytest.raises(Exception) as excinfo:
        myQ.remove()
    assert str(excinfo.value) == "Q is empty"

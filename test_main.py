import pytest

import main 

def test_index():
    assert main.index() == 'Hello, world!'
    

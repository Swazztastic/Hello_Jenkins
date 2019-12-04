import pytest
from hello_world import *

def test_hello():
    result = hello()
    assert result == "Hello"
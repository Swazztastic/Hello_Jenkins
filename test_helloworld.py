import pytest
from hello_world import *

#Hope this does some change to Jenkins
#More changes

def test_hello():
    result = hello()
    assert result == "Hello"

import pytest
from PasswordIsSecure import *

def test_Veryweak():
    assert VeryWeak('a12') == False
    assert VeryWeak('1234')
    assert VeryWeak('45jdf4r2') == False
    assert VeryWeak('123456a') == False
    assert VeryWeak('123456789') == False

def test_Weak():
    assert Weak('1234h7a')
    assert Weak('1234567') == False
    assert Weak('hol374ha') == False
    

def test_Strong():
    pass

def test_VeryStrong():
    pass

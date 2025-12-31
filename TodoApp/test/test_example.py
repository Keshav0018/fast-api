import pytest



def test_equal_or_not_equal():
    assert 3== 3


def test_is_instance():
    assert isinstance('this is a ', str)

def test_boolean():
    value =True
    assert value is True
    assert 7 > 3
    num_list = [1,2,3,4,5]
    any_list = [False,False,False,False]
    assert 1 in  num_list



class Student:
    def __init__(self,first_name:str,last_name:str):
        self.first_name = first_name
        self.last_name = last_name


@pytest.fixture
def default_student():
    return Student('ss','ss')

def test_person_intial(default_student):
    assert default_student.first_name == 'ss',"first name should be 'ss'"
    assert default_student.last_name == 'ss',"last name should be 'ss'"

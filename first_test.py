import pytest;

def test_addition():
    assert 2 + 3 == 5
    print("Pass")

def test_stringCompare():
    assert "GK" == "GK"
    assert "CAR" in "CARPENTER"
    
def test_assert_text():
    name = ['Girish', 'Harish',"Tom"]
    assert "Girish" in name
    print(test_assert_text,"Pass")
test_assert_text()

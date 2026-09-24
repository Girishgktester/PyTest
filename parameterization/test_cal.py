import pytest



from cal import add , subStarct , multiply


# def test_addition():
    
#     assert add(2,2) == 4
#     print("add is Pass")
# def test_Sub():
    
#     assert subStarct(5,4) ==1
#     print("subStarct is Pass")
    
    
@pytest.mark.parametrize("a,b, expected", [
    (2,5,7),
    (10,5,15),
    (1,1,2)
])
def test_add(a, b , expected):
    assert add(a,b) == expected
    print(f"test add results: {a},{b} and result is {expected}")
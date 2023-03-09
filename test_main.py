def func(x):
    return x + 1


def test_answer():
    # arrange
    result = 0
    # act
    result = func(3)
    # assert
    assert result == 5, f"El número esperado es 5, pero su función devuelve: {result}"

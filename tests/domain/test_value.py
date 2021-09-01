from calculator.domain import value


def test_value_calc():
    val = value.Value(10)
    assert val.calc() == 10

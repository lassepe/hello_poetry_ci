from hello_poetry_ci import foo
import pytest


@pytest.mark.parametrize("x", [1, 2, 3])
def test_foo(x):
    assert foo(x) == x

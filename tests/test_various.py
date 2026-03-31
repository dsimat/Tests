import pytest


# Tests for parameterization
@pytest.mark.parametrize("x", [1, 2, 3])
def test_example(x):
    assert x > 0


@pytest.mark.parametrize(
    "a, b, result",
    [
        (1, 2, 3),
        (3, 4, 7),
    ],
)
def test_add(a, b, result):
    """Test addition of two numbers"""
    assert a + b == result


# Test for fixtures
@pytest.fixture
def sample_list():
    return [1, 2, 3]


def test_length(sample_list):
    assert len(sample_list) == 3


def test_append(sample_list):
    sample_list.append(4)
    assert sample_list == [1, 2, 3, 4]


# Test for parameterized fixtures
@pytest.fixture(params=[1, 2, 3])
def number(request):
    return request.param


def test_number(number):
    assert number > 0


# Test for file operations
def test_file(tmp_path):
    """Test file writing and reading"""
    file = tmp_path / "hello.txt"
    file.write_text("hi!")
    assert file.read_text() == "hi!"


# Test for exception handling
def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        print(1 / 0)

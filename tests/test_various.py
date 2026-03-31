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


# Test for exception handling
def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        print(1 / 0)


# Fixture with setup and teardown for file handling
@pytest.fixture
def temp_file(tmp_path):
    file = tmp_path / "data.txt"
    file.write_text("hello")

    yield file

    # tear down runs after test finishes
    file.unlink()


def test_temp_file(temp_file):
    assert temp_file.read_text() == "hello"

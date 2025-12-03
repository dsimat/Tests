import pytest


@pytest.mark.parametrize(
    "a,b,result",
    [
        (1, 2, 3),
        (3, 4, 7),
    ],
)
def test_add(a, b, result):
    assert a + b == result


def test_file(tmp_path):
    file = tmp_path / "hello.txt"
    file.write_text("hi!")
    assert file.read_text() == "hi!"

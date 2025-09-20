from tasks import version, add


def test_version_and_add():
    assert isinstance(version(), str) and len(version()) > 0
    assert add(2, 3) == 5



from tasks import run_main_guard, double


def test_double():
    assert double(21) == 42


def test_run_main_guard_imported():
    # When imported by pytest, __name__ != '__main__'
    assert run_main_guard() == "imported"

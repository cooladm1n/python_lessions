from tasks import first_n_fibs, timer


def test_first_n_fibs():
    assert first_n_fibs(10) == [0,1,1,2,3,5,8,13,21,34]


def test_timer_does_not_crash(capsys):
    with timer():
        x = sum(range(1000))
    out = capsys.readouterr().out
    assert "took" in out

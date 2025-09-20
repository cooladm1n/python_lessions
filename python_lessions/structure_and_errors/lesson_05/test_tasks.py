import logging
from tasks import get_logger, log_start_stop, log_exception


def test_get_logger():
    logger = get_logger("x")
    assert isinstance(logger, logging.Logger)


def test_decorators(caplog):
    logger = get_logger("y")

    @log_start_stop(logger)
    def f(a, b):
        return a + b

    @log_exception(logger)
    def g():
        raise RuntimeError("boom")

    with caplog.at_level(logging.INFO):
        assert f(2, 3) == 5
        try:
            g()
        except RuntimeError:
            pass
    # verify logs were produced
    assert any("f" in rec.message for rec in caplog.records)
    assert any("boom" in rec.message for rec in caplog.records)



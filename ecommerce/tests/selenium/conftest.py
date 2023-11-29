import pytest

def pytest_addoption(parser):
    parser.addoption("--show", action="store", default="pfs", help="Argument customizes the output of tests. Values are p, f, s, for passed, failed, and skipped.\n \
                     Ex. '--show=fs' will output failed and skipped tests only.")

@pytest.fixture(scope="session")
def test_log(request):
    log = []

    yield log

    args = request.config.getoption("--show")
    if "p" in args:
        pass
    if "f" in args:
        pass
    if "s" in args:
        pass
    print(log)
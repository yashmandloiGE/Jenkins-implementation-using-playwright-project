def pytest_sessionstart(session):
    print("\n[HOOK] Pytest session started")


def pytest_runtest_setup(item):
    print(f"\n[HOOK] Starting test: {item.name}")


def pytest_runtest_teardown(item, nextitem):
    print(f"\n[HOOK] Cleaning up test: {item.name}")


def pytest_runtest_logreport(report):

    if report.when == "call":
        print(
            f"\n[PLUGIN REPORT] "
            f"{report.nodeid}: {report.outcome.upper()}"
        )


def pytest_sessionfinish(session, exitstatus):
    print("\n[HOOK] Pytest session finished")
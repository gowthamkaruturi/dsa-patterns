"""Tests run against problems/ by default. TARGET=solutions pytest  -> check the reference answers."""
import importlib, os
import pytest

TARGET = os.environ.get("TARGET", "problems")


def load(name):
    return importlib.import_module(f"{TARGET}.{name}")


def pytest_collection_modifyitems(items):
    for item in items:  # tag tests by week so you can run: pytest -m week1
        item.add_marker(getattr(pytest.mark, item.fspath.purebasename.split("_")[1]))


def pytest_configure(config):
    for w in ("week1", "week2", "week3", "week4"):
        config.addinivalue_line("markers", f"{w}: {w} problems")

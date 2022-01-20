"""Test file for dataacquisition"""
from dataacquisition import __version__


def test_version():
    """Checking version"""
    assert __version__ == "0.1.0" #nosec

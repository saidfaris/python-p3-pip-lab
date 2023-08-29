from versions import (
    python_version,
    requests_version,
    pytest_version
)


def test_python_version():
    version_info = python_version()
    assert version_info.major == 3
    assert version_info.minor == 8
    assert version_info.micro == 11  # Corrected assertion


def test_requests_version():
    assert requests_version() == "2.27.1"


    version = pytest_version()
    assert version in ["7.1.3", "6.2.5"]  # Check if version is in the list

import pytest


@pytest.mark.parametrize(
    "user,config_path",
    [
        ("root", "/etc/wsl.conf"),
    ],
)
def test_config(host, user, config_path):
    config = host.file(config_path)

    assert config.exists
    assert config.is_file
    assert config.size > 0
    assert config.user == user
    assert config.contains("default = user")

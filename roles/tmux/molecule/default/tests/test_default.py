import pytest


@pytest.mark.parametrize("user", ["root", "ansible"])
def test_smoke(host, user):
    cmd = host.run(
        f"su - {user} -c %s",
        """/;
        tmux -V
        """,
    )

    assert cmd.rc == 0


@pytest.mark.parametrize(
    "user,config_path",
    [
        ("ansible", "/home/ansible/.config/tmux/conf.d/user_bind.conf"),
        ("ansible", "/home/ansible/.config/tmux/conf.d/user_status_bar.conf"),
        ("ansible", "/home/ansible/.config/tmux/user_config.conf"),
        ("ansible", "/home/ansible/.config/tmux/tmux.conf"),
    ],
)
def test_config(host, user, config_path):
    config = host.file(config_path)

    assert config.exists
    assert config.is_file
    assert config.size > 0
    assert config.user == user

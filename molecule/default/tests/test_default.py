import pytest


@pytest.mark.parametrize("user", ["root", "serjleks"])
def test_user(host, user):
    host_user = host.user("serjleks")

    assert host_user.exists


@pytest.mark.parametrize(
    "package_name",
    [
        "bat",
        "broot",
        "btop",
        "docker",
        "eza",
        "fish",
        "fzf",
        "git",
        "htop",
        "lazydocker",
        "mc",
        "nano",
        "ncdu",
        "nvim",
        "tmux",
        "tmuxinator",
    ],
)
def test_package_is_installed(host, package_name):
    cmd = host.run(
        "su - serjleks -c %s",
        f"""/;
        which {package_name}
        """,
    )

    assert cmd.rc == 0

import pytest


@pytest.mark.parametrize("user", ["root", "ansible"])
def test_smoke(host, user):
    cmd = host.run(
        f"su - {user} -c %s",
        """
        mise --help
        """,
    )

    assert cmd.rc == 0


@pytest.mark.parametrize(
    "os_name,os_codename,package_name,package_version",
    [
        ("debian", "trixie", "mise", "2026.3.15"),
        ("debian", "bookworm", "mise", "2026.3.15"),
    ],
)
def test_package_is_installed(host, os_name, os_codename, package_name, package_version):
    host_os = host.system_info.distribution
    host_os_codename = host.system_info.codename

    if host_os == os_name and os_codename == host_os_codename:
        cmd = host.run("mise --version")

        assert cmd.rc == 0
        assert package_version in cmd.stdout


@pytest.mark.parametrize("user", ["root", "ansible"])
def test_bash_configuration(host, user):
    user_home = host.user(user).home
    bashrc = host.file(f"{user_home}/.bashrc")

    assert bashrc.exists
    assert bashrc.contains('eval "$(mise activate bash)"')
    assert bashrc.contains('eval "$(mise activate bash --shims)"')


@pytest.mark.parametrize("user", ["root", "ansible"])
def test_fish_configuration(host, user):
    if not host.file("/usr/bin/fish").exists:
        pytest.skip("Fish is not installed")

    user_home = host.user(user).home
    config_fish = host.file(f"{user_home}/.config/fish/config.fish")

    assert config_fish.exists
    assert config_fish.contains("mise activate fish | source")
    assert config_fish.contains("mise activate fish --shims | source")

    completions = host.file(f"{user_home}/.config/fish/completions/mise.fish")
    assert completions.exists
    assert completions.size > 0


@pytest.mark.parametrize("user", ["root", "ansible"])
def test_mise_doctor(host, user):
    cmd = host.run(
        f"su - {user} -c \"bash -i -c %s\"",
        """
        mise doctor
        """.strip(),
    )

    assert cmd.rc == 0

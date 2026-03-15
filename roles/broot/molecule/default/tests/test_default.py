import pytest


@pytest.mark.parametrize("user", ["root", "ansible"])
def test_smoke(host, user):
    cmd = host.run(
        f"su - {user} -c %s",
        """/;
        broot --help
        """,
    )

    assert cmd.rc == 0


@pytest.mark.parametrize(
    "os_name,os_codename,package_name,package_version",
    [
        ("debian", "trixie", "broot", "1.55.0"),
        ("debian", "bookworm", "broot", "1.55.0"),
    ],
)
def test_package_is_installed(host, os_name, os_codename, package_name, package_version):
    host_os = host.system_info.distribution
    host_os_codename = host.system_info.codename

    if host_os == os_name and os_codename == host_os_codename:
        cmd = host.run_test("broot --version")

        assert cmd.rc == 0
        assert cmd.stdout.startswith(f"broot {package_version}\n")


@pytest.mark.parametrize(
    "user,config_path",
    [
        ("ansible", "/home/ansible/.config/broot/conf.hjson"),
    ],
)
def test_config(host, user, config_path):
    config = host.file(config_path)

    assert config.exists
    assert config.is_file
    assert config.size > 0
    assert config.user == user
    assert config.contains('default_flags: "-hipg"')
    assert config.contains("file: skins/dark-void.hjson")


@pytest.mark.parametrize(
    "user,config_path",
    [
        ("ansible", "/home/ansible/.config/broot/verbs.hjson"),
        ("ansible", "/home/ansible/.config/broot/skins/dark-void.hjson"),
    ],
)
def test_configs(host, user, config_path):
    config = host.file(config_path)

    assert config.exists
    assert config.is_file
    assert config.size > 0
    assert config.user == user


@pytest.mark.parametrize(
    "user,launcher_path",
    [
        ("ansible", "/home/ansible/.config/broot/launcher/bash/br"),
    ],
)
def test_bash_shell_function_installed(host, user, launcher_path):
    launcher = host.file(launcher_path)

    assert launcher.exists
    assert launcher.is_file
    assert launcher.size > 0
    assert launcher.user == user

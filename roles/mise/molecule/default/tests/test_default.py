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
def test_mise_bash_configuration(host, user):
    user_home = host.user(user).home
    bashrc = host.file(f"{user_home}/.bashrc")

    assert bashrc.exists
    assert bashrc.contains('eval "$(mise activate bash)"')
    assert bashrc.contains('eval "$(mise activate bash --shims)"')


@pytest.mark.parametrize("user", ["root", "ansible"])
def test_mise_fish_configuration(host, user):
    if not host.file("/usr/bin/fish").exists:
        pytest.skip("Fish is not installed")

    user_home = host.user(user).home
    mise_fish = host.file(f"{user_home}/.config/fish/conf.d/mise.fish")

    assert mise_fish.exists
    assert mise_fish.contains("mise activate fish | source")
    assert mise_fish.contains("mise activate fish --shims | source")


@pytest.mark.parametrize(
    "os_name,os_codename,user,package_name,package_version",
    [
        ("debian", "trixie", "root", "mise", "2026.3.15"),
        ("debian", "bookworm", "root", "mise", "2026.3.15"),
        ("debian", "trixie", "ansible", "mise", "2026.3.15"),
        ("debian", "bookworm", "ansible", "mise", "2026.3.15"),
    ],
)
def test_mise_doctor(host, os_name, os_codename, user, package_name, package_version):
    host_os = host.system_info.distribution
    host_os_codename = host.system_info.codename

    if host_os == os_name and os_codename == host_os_codename:
        cmd = host.run(
            f'su - {user} -c "bash -i -c %s"',
            """
            mise doctor
            """.strip(),
        )

        assert cmd.rc == 0
        assert package_version in cmd.stdout
        assert "activated: yes" in cmd.stdout
        assert "shims_on_path: yes" in cmd.stdout

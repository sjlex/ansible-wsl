import pytest


@pytest.mark.parametrize("user", ["root", "ansible"])
def test_docker_smoke(host, user):
    cmd = host.run(f"su - {user} -c 'docker --version'")

    assert cmd.rc == 0


@pytest.mark.parametrize("package_name", ["docker-ce", "docker-ce-cli", "containerd.io"])
def test_packages_are_installed(host, package_name):
    pkg = host.package(package_name)

    assert pkg.is_installed


def test_docker_group_exists(host):
    assert host.group("docker").exists


@pytest.mark.parametrize("user_name", ["ansible"])
def test_user_in_docker_group(host, user_name):
    if host.user(user_name).exists:
        user = host.user(user_name)

        assert "docker" in user.groups

import pytest


@pytest.mark.parametrize("user", ["root", "ansible"])
def test_smoke(host, user):
    cmd = host.run(
        f"su - {user} -c %s",
        """/;
        fish --command 'id -un'
        """,
    )

    assert cmd.rc == 0
    assert cmd.stdout.startswith(user)


@pytest.mark.parametrize(
    "os_name,os_codename,package_name,package_version",
    [
        ("debian", "trixie", "fish", "4.5.0"),
        ("debian", "bookworm", "fish", "4.5.0"),
    ],
)
def test_package_is_installed(host, os_name, os_codename, package_name, package_version):
    host_os = host.system_info.distribution
    host_os_codename = host.system_info.codename

    if host_os == os_name and os_codename == host_os_codename:
        cmd = host.run_test("fish --version")

        assert cmd.rc == 0
        assert cmd.stdout.startswith(f"fish, version {package_version}\n")


@pytest.mark.parametrize(
    "user,config_path",
    [
        ("ansible", "/home/ansible/.config/fish/config.fish"),
        ("ansible", "/home/ansible/.config/fish/env.fish"),
        ("ansible", "/home/ansible/.config/fish/init.fish"),
        ("ansible", "/home/ansible/.config/fish/keybindings.fish"),
        ("ansible", "/home/ansible/.config/fish/aliases/user_cd.fish"),
        ("ansible", "/home/ansible/.config/fish/aliases/user_eza.fish"),
        ("ansible", "/home/ansible/.config/fish/conf.d/user_fzf.fish"),
        ("ansible", "/home/ansible/.config/fish/functions/user_fzf_select_z.fish"),
        ("ansible", "/home/ansible/.config/fish/functions/user_list_current_token.fish"),
        ("ansible", "/home/ansible/.config/fish/functions/fish_prompt.fish"),
        ("ansible", "/home/ansible/.config/fish/functions/_plain_prompt.fish"),
        ("ansible", "/home/ansible/.config/fish/conf.d/plain_prompt.fish"),
        ("ansible", "/home/ansible/.config/fish/conf.d/plain_prompt_config.fish"),
    ],
)
def test_config(host, user, config_path):
    config = host.file(config_path)

    assert config.exists
    assert config.is_file
    assert config.size > 0
    assert config.user == user

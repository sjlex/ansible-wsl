import pytest


@pytest.mark.parametrize(
    "user,context_name,endpoint",
    [
        ("ansible", "remote", "tcp://localhost:2375"),
        ("ansible", "remote-foo", "tcp://foo:1234"),
        ("root", "remote", "tcp://localhost:2375"),
        ("root", "remote-foo", "tcp://foo:1234"),
    ],
)
def test_context(host, user, context_name, endpoint):
    cmd_docker_ls = host.run(
        f"sudo su - {user} -c %s",
        f"""
        docker context ls
        """,
    )

    assert cmd_docker_ls.succeeded
    assert cmd_docker_ls.stdout.strip() != ""
    assert context_name in cmd_docker_ls.stdout

    cmd_docker_inspect = host.run(
        f"sudo su - {user} -c %s",
        f"""
        docker context inspect {context_name}
        """,
    )

    assert cmd_docker_inspect.succeeded
    assert cmd_docker_inspect.stdout.strip() != ""
    assert context_name in cmd_docker_inspect.stdout
    assert endpoint in cmd_docker_inspect.stdout

    cmd_docker_default = host.run(
        f"sudo su - {user} -c %s",
        f"""
        docker context show
        """,
    )
    assert cmd_docker_default.succeeded
    assert cmd_docker_default.stdout.strip() == "remote"

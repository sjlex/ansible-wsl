<h3 id="ansible-playbooks-wsl" align="center">
  <br>
    <img src="assets/logo.png" alt="Ansible Playbooks for WSL Logo" width="160">
  <br>
  Ansible Playbooks for WSL
  <br>
</h3>

##

<div align="center">
  <p>Ansible playbooks for provisioning WSL-1 and WSL-2.</p>
</div>

<p align="center">
  <a href="https://github.com/sjlex/ansible-wsl/releases/latest"><img alt="Version" src="https://img.shields.io/github/v/release/sjlex/ansible-wsl?labelColor=black&color=black"></a>&nbsp;
  <a href="https://github.com/sjlex/ansible-wsl/blob/main/LICENSE"><img alt="GitHub License" src="https://img.shields.io/github/license/sjlex/ansible-wsl?labelColor=black&color=black"></a>&nbsp;
</p>

## Table of contents

- [Ansible Collection](#ansible-playbooks-wsl)
  - [Table of contents](#table-of-contents)
  - [Getting started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
      - [Install WSL](#install-wsl)
      - [Post-Install](#post-install)
    - [Bootstrap](#bootstrap)
  - [Run Playbooks](#run-playbooks)
  - [Development](#development)
    - [Dev-Container](#dev-container)
      - [Build](#build-the-docker-image)
      - [Run](#run-the-docker-container)
    - [Install dependencies](#install-dependencies)
    - [Testing](#testing)
      - [Roles](#roles)
        - [Run all tests](#run-tests-for-all-roles)
        - [Run tests for a specific role](#run-tests-for-a-specific-role)
        - [Run tests manually](#run-tests-manually)
        - [Login](#login)
      - [Playbooks](#playbooks)
        - [Run integration tests](#run-integration-tests)
        - [Run integration tests for a specific scenario](#run-integration-tests-for-a-specific-scenario)
        - [Run integration tests manually](#run-integration-tests-manually)
        - [Login](#login)
    - [Linting](#linting)
    - [Clear](#clear)
  - [License](#license)
  - [Third-Party Assets](#third-party-assets)

## Getting started

### Prerequisites

Supported Operating Systems:

| Platform | Versions                   |
| -------- |----------------------------|
| Debian   | Bookworm - 12, Trixie - 13 |

### Installation

#### Install WSL

- WSL-1:

  ```shell
  wsl --set-default-version 1
  wsl --import debian-wsl1 C:\wsl\debian-wsl1 install.tar.gz
  ```

- WSL-2:

  ```shell
  wsl --set-default-version 2
  wsl --import debian-wsl2 C:\wsl\debian-wsl2 install.tar.gz
  ```

#### Post-Install

```shell
wsl --set-default-version 2
```

```shell
wsl --set-default debian-wsl2
```

### Bootstrap

- Launch WSL distribution and login (root):

  ```shell
  wsl -d debian-wsl1 -u root
  ```

  ```shell
  wsl -d debian-wsl2 -u root
  ```

- Install the required dependencies:

  ```shell
  apt install -y python3 python3-poetry python-is-python3 pyenv
  ```

  ```shell
  pyenv install
  ```

  ```shell
  ./bin/task dependencies:install
  ```

## Run Playbooks

- WSL-1:

  ```shell
  ./bin/task run:local:wsl1
  ```

- WSL-2:

  ```shell
  ./bin/task run:local:wsl2
  ```

## Finalization

### Set user password

```shell
passwd <username>
```

### Clear

- Cache and Python environment cleanup:

```shell
task clear
```

## Development

### Dev-Container

#### Build the Docker image:

```shell
./bin/task docker:build
```

#### Run the Docker container:

```shell
./bin/task docker:dev:run
```

### Install dependencies:

```shell
task dependencies:dev:install
```

### Testing

#### Roles

##### Run tests for all roles:

```shell
task test:role:all
```

##### Run tests for a specific role:

```shell
task test:role -- fish
```

or:

```shell
cd roles/fish
```

```shell
molecule test --all
```

##### Run tests manually:

```shell
cd roles/fish
```

```shell
molecule create &&
molecule converge &&
molecule verify &&
molecule idempotence &&
molecule destroy
```

##### Login

```shell
molecule list
```

```shell
molecule login --host wsl_role-fish_debian13_
```

#### Playbooks

##### Run integration tests:

```shell
task test:integration:all
```

##### Run integration tests for a specific scenario:

- Run Molecule Default scenario (docker):

  ```shell
  task test:integration:default
  ```

- Run Molecule VM scenario (vagrant + libvirt + qemu):

  ```shell
  task test:integration:main-vm
  ```

##### Run integration tests manually:

- Run Molecule Default scenario (docker):

  ```shell
  molecule create -s default &&
  molecule converge -s default &&
  molecule verify -s default &&
  molecule idempotence -s default &&
  molecule destroy -s default
  ```

- Run Molecule VM scenario (vagrant + libvirt + qemu):

  ```shell
  molecule create -s main-vm &&
  molecule converge -s main-vm &&
  molecule verify -s main-vm &&
  molecule idempotence -s main-vm &&
  molecule destroy -s main-vm
  ```

##### Login

```shell
molecule list
```

```shell
molecule login -s default --host playbook-main-debian13-
```

or:

```shell
molecule login -s main-vm --host playbook-main-debian13-
```

- Switch to user:

```shell
sudo su - <user>
```

### Linting

```shell
task lint
```

```shell
task lint:fix
```

### Clear

- Cache and Python environment cleanup:

```shell
task clear
```

## License

[MIT License](LICENSE)

## Third-Party Assets

This project may include or reference third-party assets under their own licenses. Any such assets are used in accordance with their licensing terms.

- [JetBrains Mono](https://www.jetbrains.com/lp/mono/)
  - Source: [JetBrains Mono](https://fonts.google.com/specimen/JetBrains+Mono)
  - License: [SIL Open Font License 1.1](https://fonts.google.com/specimen/JetBrains+Mono/license)

# ansible-my-wsl

> Ansible playbooks for provisioning WSL-1 and WSL-2.

## Supported Operating Systems

| Platform | Versions                   |
| -------- |----------------------------|
| Debian   | Bookworm - 12, Trixie - 13 |


## Install WSL-distribution

### WSL-1:

```shell
wsl --set-default-version 1
wsl --import debian-wsl1 C:\wsl\debian-wsl1 install.tar.gz
```

### WSL-2:

```shell
wsl --set-default-version 2
wsl --import debian-wsl2 C:\wsl\debian-wsl2 install.tar.gz
```

### Post-Install:

```shell
wsl --set-default-version 2
wsl --set-default debian-wsl2
```

## Preparing WSL environment

### 1. Run WSL-distribution:

```shell
wsl -d debian-wsl1 -u root
wsl -d debian-wsl2 -u root
```

### 2. Upgrade linux distribution (optional)

### 3. Install the required dependencies:

- Install python, pyenv and poetry:

```shell
apt install -y python3 python3-poetry python-is-python3 pyenv
```

- Use a specific Python version for this project:

```shell
pyenv install
```

- Install dependencies:

```shell
./bin/task dependencies:install
```

## Playbooks

### 1. Run playbooks:

```shell
./bin/task run:local:wsl1
./bin/task run:local:wsl2
```

### 2. Change user password:

```shell
passwd <username>
```

### 3. Clear cache and python env

```shell
./bin/task dependencies:clear
```

## Development and Testing

### 1. Build Docker image and run dev-container:

```shell
./bin/task docker:build
./bin/task docker:dev:run
```

### 2. Install dev dependencies

```shell
task dependencies:dev:install
```

### 3. Development

#### 3.1 Roles

```shell
cd roles/fish
```

Run molecule test:

```shell
molecule test --all
```

or

```shell
molecule create &&
molecule converge &&
molecule idempotence &&
molecule verify &&
molecule destroy
```

#### 3.1.1 Login:

```shell
molecule login --host wsl_role-[name]_debian13_
molecule login --host wsl_role-fish_debian12_
```

#### 3.2 Playbooks

- Molecule default scenario (docker):

  ```shell
  molecule create -s default &&
  molecule converge -s default &&
  molecule verify -s default &&
  molecule destroy -s default
  ```

  ```shell
  molecule login -s default --host playbook-main-debian13-
  molecule login -s default --host playbook-main-debian12-
  ```

  ```shell
  sudo su - <user>
  ```

- Molecule VM scenario (vagrant + libvirt + qemu):

  ```shell
  molecule create -s main-vm &&
  molecule converge -s main-vm &&
  molecule verify -s main-vm &&
  molecule destroy -s main-vm
  ```

  ```shell
  molecule login -s main-vm --host playbook-main-debian13-
  molecule login -s main-vm --host playbook-main-debian12-
  ```

  ```shell
  sudo su - <user>
  ```

### 4. Testing

#### 4.1 Roles

```shell
task test:role:all
```

or (specific role):

```shell
task test:role -- fish
```

#### 4.2 Playbooks

```shell
task test:integration:all
```

or (specific scenario):

```shell
task test:integration:default
task test:integration:main-vm
```

### 5. Linting

```shell
task lint
task lint:fix
```

## License

[MIT](LICENSE)

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

### Post-install:

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

- Install python and poetry:

```shell
apt install -y python3 python3-poetry
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

or

```shell
ANSIBLE_CONFIG=ansible.cfg ./bin/task run:local:wsl1
```

### 2. Change user password:

```shell
passwd <username>
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
molecule test
```

or

```shell
molecule create &&
molecule converge &&
molecule idempotence &&
molecule verify &&
molecule destroy
```

#### 3.2 Playbooks

- Molecule default scenario (docker):

  ```shell
  molecule create -s default &&
  molecule converge -s default &&
  molecule verify -s default &&
  molecule destroy -s default
  ```

- Molecule VM scenario (vagrant + libvirt + qemu):

  ```shell
  molecule create -s main-vm &&
  molecule converge -s main-vm &&
  molecule verify -s main-vm &&
  molecule destroy -s main-vm
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

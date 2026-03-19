docker
=========

An Ansible role to configure docker.

Requirements
------------

None

Role Variables
--------------

`docker_context_default`: Docker default context

`docker_context`: Docker context

    docker_context:
      - name: "remote"
        endpoint: "tcp://localhost:2375"

Dependencies
------------

    - sjlex.collection.docker

Example Playbook
----------------

    - hosts: servers
      roles:
        - role: sjlex.docker
          vars:
            docker_context_default: "my-context"
            docker_context:
              - name: "remote"
                endpoint: "tcp://localhost:2375"
              - name: "my-context"
                endpoint: "unix:///var/run/docker.sock"

License
-------

MIT

Author Information
------------------

Sergei Aleksandrov <sergei.a.aleks@gmail.com>

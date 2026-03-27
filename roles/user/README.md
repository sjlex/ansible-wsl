user
=========

An Ansible role to user configure.

Requirements
------------

None

Role Variables
--------------

`user_name`: User name

`user_uid`: User UID (default: 1000)

`user_groups`: User groups (default: sudo)

`user_shell`: Default shell (default: /bin/bash)

Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: user, user_name: "user", user_shell: "/usr/bin/fish" }

License
-------

MIT

Author Information
------------------

Sergei Aleksandrov <sergei.a.aleks@gmail.com>

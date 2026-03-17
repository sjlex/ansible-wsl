wsl
=========

An Ansible role to configure wsl.

Requirements
------------

None

Role Variables
--------------

`wsl_user_name`: WSL user name

Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: sjlex.wsl, wsl_user_name: "user" }

License
-------

MIT

Author Information
------------------

Sergei Aleksandrov <sergei.a.aleks@gmail.com>

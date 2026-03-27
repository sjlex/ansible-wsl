system
=========

An Ansible role to configure system.

Requirements
------------

None

Role Variables
--------------

`system_update_repository`: Update the apt repository

`system_upgrade`: Upgrades of all packages

Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: system, system_upgrade: true }

License
-------

MIT

Author Information
------------------

Sergei Aleksandrov <sergei.a.aleks@gmail.com>

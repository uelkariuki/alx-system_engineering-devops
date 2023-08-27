#!/usr/bin/env bash
# puppet manifest to make changes to our configuration file.
# Your SSH client configuration must be configured to use the private key ~/.ssh/school
# Your SSH client configuration must be configured to refuse to authenticate using a password

exec { 'ssh_config':
  path => '/bin',
  command  => 'echo "PasswordAuthentification no" >> /etc/ssh/ssh_config ; echo "IdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config',
}

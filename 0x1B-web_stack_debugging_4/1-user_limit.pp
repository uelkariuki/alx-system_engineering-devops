# Enable login with the holberton user and open a file without any error message

exec { 'change-hard-file-limit-os-configuration-for-holberton-user':
  command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

exec { 'change-soft-file-limit-os-configuration-for-holberton-user':
  command => 'sed -i "/holberton soft/s/4/40000/" /etc/security/limits.conf',  path    => '/usr/local/bin/:/bin/'
}

# Increasing the ULIMIT of default file from 15 to 4096 to handle more requests and fix the failing requests


exec { 'fix-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'

} - >

# restart nginx
exec { 'restart-nginx':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}

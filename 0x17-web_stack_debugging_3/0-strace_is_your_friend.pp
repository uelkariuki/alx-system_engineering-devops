# Automate fix of Apache returning a 500 error
file { '/var/www/html/index.html':
  ensure => 'present'
}

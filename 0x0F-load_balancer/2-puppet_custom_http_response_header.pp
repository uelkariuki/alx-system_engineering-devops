# Just as in task #0, we’d like you to automate the task of creating a custom HTTP header response, but with Puppet.
# The name of the custom HTTP header must be X-Served-By
# The value of the custom HTTP header must be the hostname of the server Nginx is running on
# Write 2-puppet_custom_http_response_header.pp so that it configures a brand new Ubuntu machine to the requirements asked in this task
#

exec { 'apt-update':
  command => '/usr/bin/apt-get -y update',
  path    =>  ['/usr/bin', '/bin']
}


# install nginx
package { 'nginx':
  ensure => installed,
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

# add X-Served-By custom header
file_line { 'add header':
  ensure => present,
  path =>  '/etc/nginx/sites-available/default',
  line => "    add_header X-Served-By ${hostname};",
  after => 'index index.html;',
}
service { 'nginx':
  ensure => running,
  enable => true,
}

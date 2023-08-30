# Puppet manifest containing commands to automatically configure an Ubuntu machine to respect above requirements
# Nginx should be listening on port 80
# When querying Nginx at its root / with a GET request (requesting a page) using curl, it must return a page that contains the string Hello World!
# The redirection must be a “301 Moved Permanently”

# Installing the Nginx package
package { 'nginx':
  ensure => installed;
}

# Defining the Nginx server configuration using a here document

file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => @("END")

# Nginx server configuration
server {
  listen 80;
  server_name localhost;

  location / {
    return 200 'Hello World!';
  }
  location /redirect_me {
    return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
  }
}
END
}

# starting and enabling the Nginx service
service { 'nginx':
  ensure     => running,
  enable     => true,
  hasrestart => true,
  hasstatus  => true,
  require    => Package['nginx'],
  notify     => File['/etc/nginx/sites-available/default'],
}

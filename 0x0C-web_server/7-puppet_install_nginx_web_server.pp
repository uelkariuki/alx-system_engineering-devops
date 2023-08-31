# Puppet manifest containing commands to automatically configure an Ubuntu machine to respect above requirements
# Nginx should be listening on port 80
# When querying Nginx at its root / with a GET request (requesting a page) using curl, it must return a page that contains the string Hello World!
# The redirection must be a “301 Moved Permanently”

# Installing the Nginx package
package { 'nginx':
  ensure => installed;
}

# Defining the Nginx server configuration using a here document

file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
  require => Package['nginx'],
}

# Nginx server configuration

file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => @("END"),
}

 server {
    listen 80;
    listen [::]:80 default_server;
    root /etc/nginx/html;
    index index.html;

    location /redirect_me {
         return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }
    error_page 404 /404.html;
    location /404 {
        root /etc/nginx/html;
        internal;
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

# Just as in task #0, we’d like you to automate the task of creating a custom HTTP header response, but with Puppet.
# The name of the custom HTTP header must be X-Served-By
# The value of the custom HTTP header must be the hostname of the server Nginx is running on
# Write 2-puppet_custom_http_response_header.pp so that it configures a brand new Ubuntu machine to the requirements asked in this task

class { 'nginx': }

nginx::resource::server {'/var/www/html/index.html':
listen_port => 80,
www_root    => '/var/www/html/index.html',
headers     => {
  'X-Served-By' => $::hostname,
  },
}

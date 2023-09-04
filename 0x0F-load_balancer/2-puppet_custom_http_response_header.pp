# Just as in task #0, we’d like you to automate the task of creating a custom HTTP header response, but with Puppet.
# The name of the custom HTTP header must be X-Served-By
# The value of the custom HTTP header must be the hostname of the server Nginx is running on
# Write 2-puppet_custom_http_response_header.pp so that it configures a brand new Ubuntu machine to the requirements asked in this task
# -i option is to add in place to make changes to the input file directly instead of printing result to stdout
# /a option is to append line that adds a custom HTTP header after the line listen 80 default_server
# /listen .. the / helps know which pattern or line that is being looked for
exec { 'command':
  command  => 'apt -y update; apt -y install nginx;
  sudo sed -i  "/listen 80 default_server; /a add_header X-Served-By $hostname;" /etc/nginx/sites-available/default;
  service nginx restart',
  provider => shell,

}

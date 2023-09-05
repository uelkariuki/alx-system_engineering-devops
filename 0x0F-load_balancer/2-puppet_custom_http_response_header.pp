# Write 2-puppet_custom_http_response_header.pp so that it configures a brand new Ubuntu machine to the requirements asked in this task
#
exec { 'command':
  command => 'apt-get -y update;
  apt-get -y install nginx;
# -i option is to add in place to make changes to the input file directly instead of printing result to stdout
# /a option is to append line that adds a custom HTTP header after the line listen 80 default_server
# /listen .. the / helps know which pattern or line that is being looked for
  sudo sed -i "/listen 80 default_server;/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default;
  service nginx restart',
  provider => shell,

}

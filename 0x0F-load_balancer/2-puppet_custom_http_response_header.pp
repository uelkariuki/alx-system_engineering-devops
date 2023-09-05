# Just as in task #0, we’d like you to automate the task of creating a custom HTTP header response, but with Puppet.
# The name of the custom HTTP header must be X-Served-By
# The value of the custom HTTP header must be the hostname of the server Nginx is running on
# Write 2-puppet_custom_http_response_header.pp so that it configures a brand new Ubuntu machine to the requirements asked in this task
# -i option is to add in place to make changes to the input file directly instead of printing result to stdout
# /a option is to append line that adds a custom HTTP header after the line listen 80 default_server
# /listen .. the / helps know which pattern or line that is being looked for

exec { 'add_header':
  command => 'echo "    add_header X-Served-By $(hostname);" | sudo tee /tmp/add_header.txt > /dev/null;
        sudo sed -i "/listen 80 default_server/r /tmp/add_header.txt" /etc/nginx/sites-available/default;
        sudo rm /tmp/add_header.txt;
        sudo service nginx restart',
  provider => shell,
}

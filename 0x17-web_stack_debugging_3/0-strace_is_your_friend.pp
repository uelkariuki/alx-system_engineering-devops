# Automate fix of Apache returning a 500 error by fixing wrong .phpp extension to .php

exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'

}

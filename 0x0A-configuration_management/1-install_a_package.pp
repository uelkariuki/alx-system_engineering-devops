# Using Puppet, install flask from pip3.

$package_name = 'flask'

package { $package_name:
  ensure   => '2.1.0',
  provider => 'pip3'

}


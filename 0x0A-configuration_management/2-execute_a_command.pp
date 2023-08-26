# Using Puppet, create a manifest that kills a process named killmenow.

$manifest_file = '2-execute_a_command'

exec { $manifest_file :
  command => 'pkill -15 killmenow',
  path    => ['/usr/bin', '/bin'], # increase chances of execution

}

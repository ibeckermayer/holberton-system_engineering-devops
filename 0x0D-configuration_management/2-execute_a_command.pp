# kill
exec { 'kill':
  path    => [ '/usr/local/sbin',
  '/usr/local/bin', '/usr/sbin', '/usr/bin', '/sbin', '/bin' ],
  command => 'pkill killmenow'
}

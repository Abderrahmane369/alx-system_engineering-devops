# task 3
exec { 'killmenow':
  command => '/usr/bin/pkill -9 killmenow',
  onlyif  => '/usr/bin/pgrep -f killmenow',
}

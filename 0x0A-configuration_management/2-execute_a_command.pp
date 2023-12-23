# task 3
exec { 'killmenow':
  command  => 'pkill -f killmenow',
  onlyif   => 'pgrep -f killmenow',
  provider => 'shell',
}

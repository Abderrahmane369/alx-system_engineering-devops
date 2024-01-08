file_line { 'haproxy_custom_header':
  path => '/etc/haproxy/haproxy.cfg'
  line => 'add_header X-Served-By $host;'
}

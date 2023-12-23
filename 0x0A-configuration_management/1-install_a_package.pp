# task 2

package { 'flask':
  ensure   => installed,
  provider => pip3,
}

package { 'werkzeug':
ensure   => installed,
provider => pip3,
}

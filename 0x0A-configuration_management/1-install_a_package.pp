#Automated installatio n of flask and puppet
exec { 'install_puppet-lint':
  command => '/usr/bin/apt-get -y install puppet-lint=2.5.0',
  unless  => 'dpkg -s puppet-lint | grep -q "Version: 2.5.0"',
}

exec { 'install_flask':
  command => '/usr/bin/apt-get -y install python3-flask=2.1.0',
  unless  => 'dpkg -s python3-flask | grep -q "Version: 2.1.0"',
}


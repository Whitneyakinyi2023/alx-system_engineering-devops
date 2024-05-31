# Automated installation of  puppet-lint -v 2.5.0

exec { 'puppet-lint':
  command => '/usr/bin/apt-get -y install puppet-lint -v 2.5.0',
}
python::pip { 'Flask':
ensure => $flask_version,
}
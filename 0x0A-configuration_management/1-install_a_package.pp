# Automated installation of  puppet-lint -v 2.5.0

# Define a class to manage Flask installation
class { 'flask':
  # Ensure Flask is installed with pip3
  package { 'Flask':
    ensure => present,
    provider => 'pip3',
    require => undef,  # Remove any unnecessary dependencies
  }
  
  # Specify the exact version (2.1.0)
  $flask_version = '2.1.0'
  # Install Flask with the specific version
  python::pip { 'Flask':
    ensure => $flask_version,
  }
}

#Automated installatio n of flask and puppet
# Check the operatings system with a fact
$os_family = $facts['osfamily']

# Define a class for installing Flask
class ::flask {

  # Use package resource with appropriate name
  package { 'python3-flask':
    ensure => installed,
  }
}

# Define a class for installing Puppet (assuming yum for RedHat)
if $os_family == 'RedHat' {
  class ::puppet {
    package { 'puppet':
      ensure => installed,
    }
  }
} else {
  # Use apt for Debian-based systems
  class ::puppet {
    package { 'puppet-agent':
      ensure => installed,
    }
  }
}



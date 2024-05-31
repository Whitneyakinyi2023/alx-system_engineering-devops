# Automated installation of  puppet-lint -v 2.5.0
package {'flask':
    provider => 'pip3',
    ensure   => '2.1.0',
    }exec { 'puppet-lint':
command => '/usr/bin/apt-get -y install puppet-lint -v 2.5.0',
}

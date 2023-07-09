# Install Nginx if not already installed
package { 'nginx':
  ensure => installed,
}

# Create necessary directories
file { '/data/':
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

file { '/data/web_static/':
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

file { '/data/web_static/releases/':
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

file { '/data/web_static/shared/':
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

file { '/data/web_static/releases/test/':
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

# Create a fake HTML file for testing
file { '/data/web_static/releases/test/index.html':
  ensure  => file,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  content => 'This is a test',
}

# Create a symbolic link
file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test/',
  force  => true,
}

# Update Nginx configuration
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "# Puppet-managed file\n\nserver {\n\tlisten 80 default_server;\n\tlisten [::]:80 default_server;\n\n\troot /var/www/html;\n\tindex index.html index.htm index.nginx-debian.html;\n\n\tserver_name _;\n\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n}",
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Restart Nginx
service { 'nginx':
  ensure => running,
  enable => true,
  require => File['/etc/nginx/sites-available/default'],
}

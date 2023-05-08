# Sets up web servers

class setup_web_static {
  package { 'nginx':
    ensure => 'installed',
  }

  service { 'nginx':
    ensure => 'running',
    enable => true,
  }

  file { '/data/':
    ensure => 'directory',
    owner  => 'ubuntu',
    group  => 'ubuntu',
  }

  file { '/data/web_static/':
    ensure => 'directory',
    owner  => 'ubuntu',
    group  => 'ubuntu',
  }

  file { '/data/web_static/releases/':
    ensure => 'directory',
    owner  => 'ubuntu',
    group  => 'ubuntu',
  }

  file { '/data/web_static/shared/':
    ensure => 'directory',
    owner  => 'ubuntu',
    group  => 'ubuntu',
  }

  file { '/data/web_static/releases/test/':
    ensure => 'directory',
    owner  => 'ubuntu',
    group  => 'ubuntu',
  }

  file { '/data/web_static/releases/test/index.html':
    ensure => 'file',
    owner  => 'ubuntu',
    group  => 'ubuntu',
    mode   => '0644',
    content => 'Holberton School',
  }

  file { '/data/web_static/current':
    ensure => 'link',
    target => '/data/web_static/releases/test',
  }

  file { '/etc/nginx/sites-available/default':
    ensure  => 'file',
    owner   => 'root',
    group   => 'root',
    mode    => '0644',
    content => template('setup_web_static/default.erb'),
    notify  => Service['nginx'],
  }

  file { '/etc/nginx/sites-enabled/default':
    ensure  => 'link',
    target  => '/etc/nginx/sites-available/default',
    require => File['/etc/nginx/sites-available/default'],
  }
}

#!/usr/bin/python3
# Module with Fabric script that creates and distributes an archive to a server.

from fabric.api import *
import os.path
import datetime

env.user = 'ubuntu'
env.hosts = ['107.22.143.207', '100.25.200.19']
# Path to SSH private key file
env.key_filename = '/Users/serahnderi/ssh/school/id_rsa.pub'
env.warn_only = True  # Continue execution if some commands fail


def do_pack():
    """Generates a .tgrz archive"""
    local("mkdir -p versions")
    t = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    archive = local("tar -czvf versions/web_static_{}\
.tgz web_static".format(t))
    if archive.succeeded:
        return ("versions/web_static_{}.tgz".format(t))
    else:
        return None


def do_deploy(archive_path):
    """Fabric script that distributes an archive to server"""
    if os.path.exists(archive_path):
        new_path = archive_path.replace('versions/', '')
        file_name = new_path[:-4]
        arc_folder = "/data/web_static/releases/{}".format(new_path)
        put(archive_path, '/tmp/')
        run('mkdir -p /data/web_static/releases/{}'.format(file_name))
        run('tar -xzf /tmp/{} -C {}'.format(new_path, arc_folder[:-4]))
        run('rm /tmp/{}'.format(new_path))
        run('mv {}/web_static/* {}/'.format(arc_folder[:-4], arc_folder[:-4]))
        run('rm -rf {}/web_static'.format(arc_folder[:-4]))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(arc_folder[:-4]))
        return True
    else:
        return False


def deploy():
    """Creates and distributes and archive to a server"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)

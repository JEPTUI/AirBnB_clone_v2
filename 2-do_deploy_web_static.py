#!/usr/bin/python3
# creates and distributes an archive to your web servers

from fabric.api import env, run, put
import os.path
env.hosts = ["100.25.182.185", "54.237.33.235"]


def do_deploy(archive_path):
    """
    creates and distributes an archive to your web servers
    """
    if os.path.isfile(archive_path) is False:
        return False
    try:
        filename = archive_path.split("/")[-1]
        name = filename.split(".")[0]
        path_no_ext = "/data/web_static/releases/{}/".format(name)
        symlink = "/data/web_static/current"
        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(path_no_ext))
        run("tar -xzf /tmp/{} -C {}".format(filename, path_no_ext))
        run("rm /tmp/{}".format(filename))
        run("mv {}web_static/* {}".format(path_no_ext, path_no_ext))
        run("rm -rf {}web_static".format(path_no_ext))
        run("rm -rf {}".format(symlink))
        run("ln -s {} {}".format(path_no_ext, symlink))
        return True
    except Exception as e:
        return False

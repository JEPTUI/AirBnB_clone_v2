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
        put(archive_path, "/tmp/")
        filename = archive_path.split("/")[-1]
        folder_name = "/data/web_static/releases/{}".format(
                filename.split(".")[0])
        run("mkdir -p {}".format(folder_name))
        run("tar -xzf /tmp/{} -C {}".format(filename, folder_name))
        run("rm /tmp/{}".format(filename))
        run("mv {}web_static/* {}".format(filename, folder_name))
        run("rm -rf {}web_static".format(folder_name))

        run("rm -rf /data/web_static/current")

        run("ln -s {} /data/web_static/current".format(folder_name))
        return True
    except Exception as e:
        return False

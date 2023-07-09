#!/usr/bin/python3
# creates and distributes an archive to your web servers
import os.path
from datetime import datetime
from fabric.api import local, env, put, run
from time import strftime
env.hosts = ["100.25.182.185", "54.237.33.235"]


def do_pack():
    """
    generates a .tgz archive from the contents of the web_static
    """
    timenow = datetime.now().strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        filename = "versions/web_static_{}.tgz".format(timenow)
        local("tar -cvzf {} web_static/".format(filename))
        return filename
    except Exception as e:
        return None
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
def deploy():
    """
    creates and distributes an archive to your web servers
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)

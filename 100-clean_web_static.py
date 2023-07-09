#!/usr/bin/python3
# creates and distributes an archive to your web servers
import os.path
from datetime import datetime
from fabric.api import local, env, put, run, cd
from time import strftime

env.user = 'ubuntu'
env.hosts = ["100.25.182.185", "54.237.33.235"]


def do_clean(number=0):
    """
    Deletes out-of-date archives
    """
    number = int(number)
    if number < 1:
        number = 1
    number += 1
    with cd('versions'):
        # Delete unnecessary archives from the versions folder
        run("ls -t | tail -n +{} | xargs rm -rf --".format(number))

    with cd('/data/web_static/releases'):
        # Delete unnecessary archives from the /data/web_static/releases
        run("ls -t | tail -n +{} | xargs rm -rf --".format(number))


def deploy():
    """
    creates and distributes an archive to your web servers
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)

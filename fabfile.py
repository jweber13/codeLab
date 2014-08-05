from fabric import api
from fabric.api import *
from fabric.operations import *
from boto import ec2

import os, sys, glob
from datetime import date

AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY", "")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY", "")
DATABASE_URL = os.getenv("STAGING_DATABASE_URL", "")

BUCKET = "codelabjw"
STAGING_IP = "54.186.155.42"

def get_ec2_connection():
    return ec2.connect_to_region(REGION,
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY)

def create_snapshot():
    conn = get_ec2_connection()
    instance_id = conn.get_all_addresses([IP,])[0].instance_id
    name = 'fig_codelab.{0}'.format(date.today().strftime("%d.%m.%y"))
    return conn.create_image(instance_id, name, no_reboot=True)

def staging():
    api.env.hosts = [IP,]
    api.env.user = "ubuntu"
    api.env.branch = "master"

def ssh_into():
	local("ssh -i ~/.ssh/ec2codelabjw.pem ubuntu@54.186.155.42")

def update():
    api.require("hosts", provided_by=[staging])

    with api.settings(warn_only=True):
        api.sudo('service fig_codelab stop')

    with api.cd('~/NextTier-Web'):
        api.run('git pull origin master')
        with shell_env(DATABASE_URL=DATABASE_URL):
            #with api.prefix('source ./venv/bin/activate'):
                api.run('pip install -r requirements.txt')
                api.run('cd ./next-tier && python manage.py migrate')
                api.run('deactivate')

    api.sudo('service fig_codelab start')

def sample():
	print("status check")
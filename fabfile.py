from fabric import api
from fabric.api import *
from fabric.operations import *

import os, sys, glob
from datetime import date

STAGING_IP = "54.186.155.42"

def setup():
	local("ssh -i ~/.ssh/ec2codelabjw.pem ubuntu@54.186.155.42")

def update():
	run("cd codeLab")
	run("git pull")
	
def sample():
	print("status check")

def run_upstart():
	run("suder service restart fig_codelab")

def migrate():
	run("python manage.py syncdb --migrate")

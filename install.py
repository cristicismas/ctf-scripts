#!/usr/bin/env python3

import os
import sys

scripts_path = os.environ['PWD'] + "/scripts"

if os.path.exists(scripts_path):
    print("The scripts folder already exists.")
    exit(1)
else:
    os.mkdir(scripts_path)

repos = tuple(open("repos.txt", 'r'))

os.chdir(scripts_path)

for repo in repos:
    os.system("git clone " + repo)

print("Repos cloned in " + scripts_path)

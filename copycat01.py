#!/usr/bin/env python3

import shutil

import os

os.chdir("/home/student/mycode/")

shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.tx.copy")

shutil.copytree("5g_research/", "5g_reearch_backup/")



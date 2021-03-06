#!/usr/bin/env python3

import tarfile
import subprocess

# download tar.gz file
subprocess.call(['curl', '-o', 'adult.tar.gz', 'http://dsi.ut-capitole.fr/blacklists/download/adult.tar.gz'])

# extract the contents of the downloaded file
with tarfile.open('adult.tar.gz') as my_tar:
    my_tar.extractall()

# add domain from each line in the specified file to pihole blacklist
with open('adult/domains', 'r') as adult_list:
    for line in adult_list.readlines():
        subprocess.call(['pihole', '-b', line.strip()])
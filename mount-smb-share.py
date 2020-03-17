#!/usr/bin/env python3

import sys, os
import conf

config = conf.read_config()

username = config.Windows.Username
password = config.Windows.Password
share = config.Windows.Share
local_mnt = config.Local.MountPath

os.system(f"sudo mount -t cifs -o username={username},password={password} {share} {local_mnt}")

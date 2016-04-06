#!/usr/bin/env python

import os.path

if os.path.isfile('/etc/dhcpcd_backup.conf'):
	print "True"
else:
	print "False"
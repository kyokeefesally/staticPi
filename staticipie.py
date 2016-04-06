#!/usr/bin/env python

from __future__ import print_function
import os
import time

try:
	from configparser import ConfigParser
except ImportError:
	from ConfigParser import ConfigParser  # ver. < 3.0

def getdata():
	# instantiate
	config = ConfigParser()

	# parse existing file
	config.read('/boot/staticipie.txt')

	config_file = open ('/boot/staticipie.txt')

	config_data = config_file.read()

	#print("checking staticipie.txt to make sure config file is complete")

	# check to see if config file has all keys present
	if 'interface=' in config_data and 'ip_address=' in config_data and 'routers=' in config_data and 'domain_name_servers=' in config_data:
		
		#print("staticipie.txt config file has all keys present")
		# set config variables
		interface = config.get('staticIPie', 'interface')
		ip_address = config.get('staticIPie', 'ip_address')
		routers = config.get('staticIPie', 'routers')
		domain_name_servers = config.get('staticIPie', 'domain_name_servers')

		#print("checking key values are present")
		if interface <> "" and ip_address <> "" and routers <> "" and domain_name_servers <> "":

			#print("all key values present")
			# format static IP text that will be added to dhcpcd.conf file
			static_ip_config = ("# Custom static IP address for eth0\n"
						"interface " + interface + "\n"
						"static ip_address=" + ip_address + "\n"
						"static routers=" + routers + "\n"
						"static domain_name_servers=" + domain_name_servers
						)

			#print("creating new dhcpcd.conf temp file")
			# open clean/default dhcpcd.conf file w/o any static IP config txt
			txt_file = open("/home/pi/staticIPie/etc/dhcpcd_raw.conf")

			# read clean config file and store as variable
			source_content = txt_file.read()

			# open temp file to overwrite with clean config txt
			temp = open ("/home/pi/staticIPie/etc/dhcpcd_temp.conf", 'w')
			
			# write clean config data to overwrite existing dhcpcd_temp.conf file
			temp.write(source_content)	
			# close temp file so can re-open to append
			temp.close()

			# open temp file to append new static IP txt
			temp = open ("/home/pi/staticIPie/etc/dhcpcd_temp.conf", 'a')
			temp.write(static_ip_config)

			# open 
			temp = open ("/home/pi/staticIPie/etc/dhcpcd_temp.conf")

			temp_config = temp.read()
			#print("temp file complete")

			###################################
			#  make backup of current config  #
			###################################

			#print("backing up /etc/dhcpcd.conf to /etc/dhcpcd_backup.conf")
			# open current config
			dhcpcd = open ("/etc/dhcpcd.conf")
			# copy current config
			current_config = dhcpcd.read()
			# make backup config
			backup_config = open ("/etc/dhcpcd_backup.conf", 'w')
			# write current config to backup
			backup_config.write(current_config)
			#print("backup complete")

			##############################################
			#  create new config - copy temp to current  #
			##############################################

			#print("creating new dhcpcd.conf config file")
			# open current config to rewrite new config
			new_config = open ("/etc/dhcpcd.conf", 'w')

			# overwrite current config w/temp config
			new_config.write(temp_config)

			#print("new dhcpcd.conf config file complete\n")
			#print("new static IP info:")
			#print(static_ip_config)

			#print("restarting eth0 interface")
			time.sleep(5)
			os.system("sudo ifdown eth0")
			time.sleep(10)
			os.system("sudo ifup eth0")
			time.sleep(10)
			os.system("sudo /etc/init.d/networking restart")
			#os.system("sudo systemctl daemon-reload")


			#print(temp_config)

		else:
			#print("staticipie.txt config file is missing a key value")
			exit()

	else:
		#print("staticipie.txt config file is missing a required key")
		exit()


getdata()
#writeconf()

#!/usr/bin/env python

from __future__ import print_function

#collecting the filename we are about to copy the content
#sourcefile = raw_input("/home/pi/staticIPie/etc/dhcpcd_raw.conf")
#here we are opening the file we specified earlier
txt_file = open("/home/pi/staticIPie/etc/dhcpcd_raw.conf")
#here we are reading the content from the source file and storing the content
source_content = txt_file.read()
#providing name for the file to be created
#destinationfile = raw_input("/home/pi/staticIPie/etc/dhcpcd_temp.conf")
#here we are opening the newly created file in write mode
target = open ("/home/pi/staticIPie/etc/dhcpcd_temp.conf", 'w') ## a will append, w will over-write 
#here we are writing the source file content to destination file
#target.write(source_content)
var = "kyle"
new_array = ("# Custom static IP address for eth0\n"
			"interface " + var + "\n"
			"static ip_address=" + var + "\n"
			"static routers=" + var + "\n"
			"static domain_name_servers=" + var
			)
print(new_array)
#target.write(new_array)
#providing information that the task is completed
#print("we have added those text to the file")
#target.close()
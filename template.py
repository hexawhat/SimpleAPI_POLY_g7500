import telnetlib

host = "192.168.0.8"
port = 24 
username = "UserNameGoesHere"
password = "passwordGoesHEre"
commandToRun = "mute near get" # https://www.poly.com/content/dam/www/products/support/video/video-os/archive/g7500-cl-api-3-8-0.pdf
tn = telnetlib.Telnet(host, port)
tn.write(password.encode('ascii')+b'\n')
tn.write(commandToRun.encode('ascii')+b'\n')
variable = tn.listener()
print(variable)

#tn.interact() # uncomment this line to inteact with telnet client app 

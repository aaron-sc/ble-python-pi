import os, time, bluetooth

# Set up all of our variables
photo_quality = "480x320"
filename = "testing.jpg"
photo_folder = "~/usbphotos/"
file_to_send = photo_folder + filename
mac_address="50:50:A4:2D:BB:F5"
photo_command="fswebcam -r " + photo_quality + " --no-banner ~/usbphotos/" + filename
transfer_command = "obexftp --nopath --noconn --uuid none --bluetooth " + mac_address + " --channel 12 -p " + file_to_send


server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
port = 1
server_sock.bind(("",port))
server_sock.listen(1)
client_sock,address = server_sock.accept()
print("Accepted connection from " + str(address))


def sendMessageTo(targetBluetoothMacAddress):
  port = 1
  sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
  sock.connect((targetBluetoothMacAddress, port))
  sock.send("hello!!")
  sock.close()

def lookUpNearbyBluetoothDevices():
  nearby_devices = bluetooth.discover_devices()
  for bdaddr in nearby_devices:
    print(str(bluetooth.lookup_name( bdaddr )) + " [" + str(bdaddr) + "]")

def send_file():
    global photo_command, transfer_command
    os.system(photo_command)
    time.sleep(0.5)
    os.system(transfer_command)

"""
def connect(mac_address):
    bd_addr = mac_address
    port = 1
    sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((bd_addr, port))
    sock.send("test")
    sock.close()
"""

while 1:
    #server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )

    #port = 1
    #server_sock.bind(("",port))
    #server_sock.listen(1)

    #client_sock,address = server_sock.accept()
    # print("Accepted connection from " + str(address))

    data = client_sock.recv(1024).decode("utf-8")
    if(data == "look"):
        send_file()

    #receiveMessages("look", send_file)

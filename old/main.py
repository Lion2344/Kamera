#import internet
#import machine
#import server
#import read_write
import lights


for l in ['OnBoard', 'Red', 'Yellow', 'Green']:
    lights.ToggleLight(l)


#led = DigitalInOut(board.LED)
#internet.ScanWifiNetwork()
#machine.reset()

#lights.ToggleRed()
#ip = internet.ConnectToWifi()

#connection = internet.open_socket(ip=ip, port=80)
#server.serve(connection)

#internet.DisconnectFromWlan()

#read_write.SDTest()

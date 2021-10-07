import telnetlib
import time
import re

def getData(ip,username,password):
    tn_ip = ip
    tn_port = "5153"
    tn_username = username
    tn_password = password
    try:
        tn = telnetlib.Telnet(tn_ip, tn_port, 15)
    except:
        print ("Unable to connect to Telnet server: ")
        return

    z = tn.read_until(b'Login:', 10)
    if z == b'':
        return
    tn.write(tn_username.encode('utf-8'))
    tn.write(b'\r')
    tn.read_until(b"Password: ",10)
    if z == b'':
        return
    tn.write(tn_password.encode('utf-8'))
    tn.write(b'\r')
    tn.read_until(b">",10)
    time.sleep(2)
    tn.write(b"interface wireless print")
    tn.write(b'\r')
    time.sleep(2)
    
    a=tn.read_very_eager().decode("utf-8")
    tn.write(b"system routerboard print")
    tn.write(b'\r')
    time.sleep(1)
    b=tn.read_very_eager().decode("utf-8")
    ssid = re.findall(r'.*ssid.*"(.*)"', a)
    cpeNumber = re.findall(r'.*serial-number:\s+(\w+)',b)
    return ssid[0],cpeNumber[0]

    #
    #b = tn.read_until(tn_username.encode("utf-8"))
    # print(a)
    # print(b)

    # print(tn.read_very_eager())


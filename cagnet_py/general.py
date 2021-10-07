import mysqlConnector
import telnetConnector

mydb = mysqlConnector.connect()

data = mysqlConnector.getData(mydb)

for x in data:
    try:
        ssid,cpe = telnetConnector.getData(x["framedipaddress"],x["cihaz_kad"],x["cihaz_sifre"])
        print(str(x["id"])+":"+ssid+"-"+cpe)
        mysqlConnector.insertData(mydb, x["id"], ssid, cpe)
        
    except:
        print(str(x["id"])+" olmadı")
    

mydb.close()
 

print("end")

exit()
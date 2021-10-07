import mysql.connector

def connect():
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="cagnet"
  )

  return mydb

def getData(mydb):

  mycursor = mydb.cursor(dictionary=True)

  mycursor.execute("SELECT tbliss_uyeler.id,tbliss_uyeler.k_adi,tbliss_uyeler.cihaz_kad,tbliss_uyeler.cihaz_sifre,radacct.framedipaddress FROM tbliss_uyeler LEFT JOIN tbliss_tarifeler ON tbliss_tarifeler.id = tbliss_uyeler.tarife LEFT JOIN tbliss_kullanicilar ON tbliss_kullanicilar.id = tbliss_uyeler.s_id JOIN radacct ON radacct.username = tbliss_uyeler.k_adi AND radacct.acctstoptime IS null WHERE tbliss_uyeler.durum = 1 AND tbliss_uyeler.s_id NOT IN (10035,10044,10046,10048,10050,10051,10052,10053,10057,10059,10062,10071,10072,10073) AND tbliss_uyeler.tarih > '2021-06-01' ORDER BY tbliss_uyeler.id")

  myresult = mycursor.fetchall()

  return myresult

def insertData(mydb, id, ssid, cpe):

  print("")
  mycursor = mydb.cursor()

  sql = "INSERT INTO z_mactable (k_id, ssid, cpe) VALUES (%s, %s, %s)"
  val = (id, ssid, cpe)
  mycursor.execute(sql, val)

  mydb.commit()

def insertDataFailData(mydb, id):


  mycursor = mydb.cursor()

  sql = "INSERT INTO z_mactableFail (kid) VALUES (%d)"
  val = (id)
  mycursor.execute(sql, val)

  mydb.commit()  
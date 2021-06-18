# Laravel Assignment

## Database
- Kullanılacak olan db teknolojisi MYSQL.
- Tabloları'i migrations ve seederleri kullanarak aşağıdaki tablolardaki kolonları ve içerikleri oluşturun. Laravelin gerektirdiği timestamp değerlerini de ekleyiniz. İlgili tablolar soft delete olacak şekilde ayarlanmalıdır.

customers
|id|name|email|gsm_no|department_id
|---|---|---|---|---|
|1|John Doe|john@doe.com|905331234567|1
|2|Mary Lee|mary@lee.com|905331234568|2

departments
|id|name
|---|---
|1|Muhasebe
|2|Pazarlama

Not: customers ve departments arasında foreign key kullanılması gerekmektedir.

## Müşteri(customers) ekranları
- Müşteri listeleme ekranı oluşturulması. Burada tablodaki anlamlı alanlar kullanılmalıdır. Bu ekranda bir buttonla müşteri oluşturma ekranına gidilmelidir.
- Müşteri oluşturma ekranı oluşturulması. Bu ekranda tabloya yazılacak şekilde bir form oluşturulması ve backendin ona göre geliştirilmesi gerekmektedir. Oluşturma sırasında gelen alanlar doğrulanmalıdır(validation).

## Zamanlanmış İşler (Scheduled Jobs)
- Customers tablosundaki departmanı Muhasebe olan kişilere her sabah 8de mail çıkacak şekilde bir job yazılması.
- Customers tablosundaki departmanı Pazarlama olan kişilere her akşam saat 12de mail çıkacak şekilde bir job yazılması.

print ("Hello")
print ("Nama: Diska Kurnia Azzahra Putra")
print ("NIM: 312210369")
print ("Kelas: TI.22.A.4")

print ("//Masukan input")
print ("Program menghitung luas dan keliling lingkaran")
print ("----------------------------------------------")

r = float(input('Masukan nilai jari-jari : '))

phi = 3.14
Diameter = 2*r

luas = phi*r*r
keliling = phi*Diameter
print('\nLuasnya =', str("%.2f" % luas))
print('kelilingnya =', str("%.2f" % keliling))
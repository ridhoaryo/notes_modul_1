# print('Jum'at')
# print("Jum'at")

# assignment = memasukkan value ke dalam variable

nama = 'Ridho' # String
umur = 28 # int
tinggi = 173.5 # float
married = True # boolean
gadget = ['hp', 'laptop', 24, 'tv', 'smartwatch', True] # list #mutable
family = {'wife': 'Fita', 'son': 'Khalid'} # dictionary
numbers = {1,2,3,4,5} # set
anatomi = ('mata', 'telinga', 'hidung') # tuple #immutable

# print(nama)
# print(umur)
# print(tinggi)

# update umur dan tinggi
# umur = 29
# tinggi = 175.5

# print(umur)
# print(tinggi)

# # untuk mengetahui data type sebuah value => 'type'
# print(type(nama))
# print(type(umur))
# print(type(tinggi))
# print(type(married))
# print(type(gadget))
# print(type(family))
# print(type(numbers))
# print(type(anatomi))

# nama = 28
# umur = 'Ridho'

# print(type(nama))
# print(type(umur))

# print(nama)
# print(umur)

# hp = input('Input your phone number: ')
# print(hp)


# alamat = input('Input your address: ') # String
# print(alamat)

# angka = 12
# print(type(angka))

# print(input('Terserah: '))

# myname1 = 'My name ' # spasinya di sini
# name1 = 'Andi'
# print(myname1 + name1)

# myname2 = 'My name'
# name2 = ' Andi' # spasinya di sini
# print(myname2 + name2)

# myname3 = 'My name'
# name3 = 'Lintang'
# print(myname3 + ' ' + name3) # spasinya di sini

# myname4 = 'My name'
# name4 = 'Ridho'
# print(myname4, name4, 'Halo apa kabar') # spasinya diwakilkan koma

# print(name3)
# print(name3)
# print(name3)
# print(name3)
# print(name3)

# print(name3 * 5)
# print((name3+' ')*5)
#     (Lintang )*5

# print(4+5) # penjumlahan
# print(4-1) # pengurangan
# print(4*5) # perkalian

# print(20/5) # pembagian (float)
# print(20//5) # pembagian (int)

# print(5/2)
# print(5//2)

# print(7.8/2)
# print(7.8//2)

# print(5 % 4) # reminder / sisa pembagian

# print(5 ** 2) # hasil pangkat

# # +- < */ < ** < ()
# print(1+2*8-9)
# print((1+2)*8-9)
# print((1+3)*7**2)

# nama = 'Ridho'
# umur = 28
# str_umur = str(umur)

# print(umur)
# print(str_umur)

# print(type(umur))
# print(type(str_umur))

# # output => Ridho umurnya 28
# print(nama + ' umurnya ' + str(umur))
# print(True + False)
# print(nama, 'umurnya', umur)

# angka = int(input('Masukkan angka: ')) # input by default menghasilkan String
# print(type(angka))
# print(angka+10)

# print(type(int('23')))
# print(float('23'))
# print(type(str(24)))
# print(type(str(24)))

# nama = 'Andi'
# umur = 23

# output => 5 tahun lagi, umur Andi adalah 28
# print('5 tahun lagi, umur', nama, 'adalah', umur+5) # cara 1
# print('5 tahun lagi, umur ' + nama + ' adalah ' + str(umur+5)) # cara 2
# print('5 tahun lagi, umur {} adalah {}'.format(umur+5, nama)) # cara 3
# print(f'5 tahun lagi, umur {nama} adalah {umur+5}') # cara 4
# print('5 tahun lagi, umur %s adalah %d' % (nama, umur+5)) # cara 5
# formatted string

# umur = 28
# umur = umur + 5
# umur += 5
# umur *= 2 # ==> umur = umur * 2
# umur -= 5 # ==> umur = umur - 5
# umur /= 2 #   ==> umur = umur / 2
# print(umur)

# swap
# x = 2
# y = 1
# z = 0
# print('x:', x, 'y:', y)

# temp = x
# x = y
# y = temp
# print('x:', x, 'y:', y)

# x, y = y, x
# print('x:', x, 'y:', y)

# x, y, z = y, z, x
# print(x,y,z)

# a, b, c = 1, 2, 3
# print(a, b, c)
# print(a)
# print(b)

# import math
# # from math import pi, fabs, pow, sqrt, floor, ceil

# # # from dipakai kalau kita hanya butuh beberapa function saja / kita tidak hafal dengan function2 dalam
# # # library tersebut
# i = 125.6748

# print(math.pi)
# print(math.fabs(-i))
# print(math.pow(i, 3))
# print(math.sqrt(i))
# print(math.floor(i))
# print(math.ceil(i))

# print(round(i))



## STRING & LIST
#    01234567891011
x = 'Halo Dunia Lain. Apa Kabar?'
# print(len(x)) #27
# index_max = len - 1
# print(x.index('a'))
# print(x.index('Dunia'))
# print(x.index(' '))
# print(x.index('a'))
# print(x.index('A'))
# print(x.index('?'))
# y = x.split(',') # split(' ')
# print(y)
# print(x.lower())
# print(x.upper())
# print(x.capitalize())
# print(x.replace('Halo', 'Hai')) # hasil akhir tidak langsung di save ke x. sehingga perlu dimasukkan ke variable lain
# z = x.replace('Halo', 'Hai')
# print(x)
# print(z)
# print(x.count('a'))
# print(x.count('Halo'))

# STRING indexing & slicing
#    01234567891011121314
#         -5-4-3-2-1
# a = 'saya makan nasi'
# print(a) # saya makan nasi
# print(a[5]) # m => # indexing
# print(a[5:10]) # makan => slicing
# print(a[14]) # i
# print(a[-1]) # i
# print(a[-15]) # s
# print(a[11:]) # nasi
# print(a[5:]) # makan nasi
# print(a[-4:]) # nasi
# # #             step
# print(a[-1:-5:-1]) # isan
# print(a[11:15:2]) # ns
# print(a[::-1]) #isan nakam ayas
# print(a) # saya makan nasi
# print(a[:4]) # saya
# print(a[14]) # indexing= ngga boleh lebih dari index maksimalnya
# print(a[:125]) # slicing


'''
1 tahun = 360
jumlah hari = 150
output = 150 hari sama dengan 0 tahun, 5 bulan, 0 minggu, 0 hari

jumlah hari = 360
output = 360 hari sama dengan 1 tahun, 0 bulan, 0 minggu, 0 hari    

jumlah hari = 287
output = 287 hari sama dengan 0 tahun, 9 bulan, 2 minggu, 3 hari
'''

import math
jumlah_hari = int(input('Masukkan hari: '))
tahun = math.floor(jumlah_hari/360)
bulan = math.floor((jumlah_hari%360)/30)
minggu = math.floor(((jumlah_hari%360)%30)/7)
hari = math.floor(((jumlah_hari%360)%30)%7)

print(f"{jumlah_hari} hari sama dengan, {tahun} tahun, {bulan} bulan, {minggu} minggu, {hari} hari")



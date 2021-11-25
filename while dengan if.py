
jumlah_buku = 10
print("ibu menyuruh membaca dan memahami semua buku")

total_jumlah_baca_buku = 0
print(f"total jumlah baca buku{total_jumlah_baca_buku}")

buku_yang_udah_dibaca_dan_dipahami = 0
print(f'buku yang udah dibaca dan dipahami {buku_yang_udah_dibaca_dan_dipahami}')

while total_jumlah_baca_buku < jumlah_buku * 2 :
    total_jumlah_baca_buku = total_jumlah_baca_buku + 1
    if buku_yang_udah_dibaca_dan_dipahami == 9:
        print(f"buku ke {buku_yang_udah_dibaca_dan_dipahami+1} belum paham")
    else:
        buku_yang_udah_dibaca_dan_dipahami = buku_yang_udah_dibaca_dan_dipahami + 1

if buku_yang_udah_dibaca_dan_dipahami == jumlah_buku :
    print('"bu buku dah di baca sama di pahami semuanya')
else:
    print(f"buku yang bisa di pahami {buku_yang_udah_dibaca_dan_dipahami} buku doang")




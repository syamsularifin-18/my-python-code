print("list daftar semua buku")
daftar_buku = ["alqura'n", "iqro", "sansu", "seikatsu"]
print(daftar_buku)

print("\nproses semua dengan for in")
for buku in daftar_buku:
    print(buku)

print("\ntampilkan buku ke 1 dan 3")
print(daftar_buku[0])
print(daftar_buku[2])

print("\ntampilkan mengunakan len")
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\npenambahan buku dengan append")
daftar_buku.append("kanji")
print(daftar_buku)

print("\nproses semua dengan for in")
for buku in daftar_buku:
    print(buku)

print("\ntampilkan buku ke 1 dan 5")
print(daftar_buku[0])
print(daftar_buku[4])

print("\ntampilkan mengunakan len")
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])
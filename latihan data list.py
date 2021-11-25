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

print("cara mengganti list")
daftar_buku = ["alqura'n", "iqro", "sansu", "seikatsu","kanji"]
daftar_buku[2] = "komik"
print(daftar_buku)

print("\ncara menghapus list")
daftar_buku.pop(3)
print(daftar_buku)

print("\ncara menghapus list dari belakang")
daftar_buku.pop(-2)
print(daftar_buku)

daftar_buku = ["alqura'n", "iqro", "sansu", "seikatsu","kanji"]
print("\n cra menghapus list dari belakang hanya 1 buku")
daftar_buku.pop(-2)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

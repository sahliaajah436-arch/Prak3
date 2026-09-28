import math

luas_lingkaran = lambda jari_jari: math.pi * jari_jari ** 2

jari_jari = float(input("Masukkan jari-jari lingkaran: "))

if jari_jari < 0:
    print("Jari-jari tidak boleh negatif!")
else:
    luas = luas_lingkaran(jari_jari)
    print(f"Jari-jari : {jari_jari}")
    print(f"Luas      : {luas:.2f}")

print("\nContoh:")
for r in [5, 7, 10]:
    print(f"Jari-jari {r} -> Luas {luas_lingkaran(r):.2f}")
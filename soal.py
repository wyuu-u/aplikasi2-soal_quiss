print("Selamat datang di kuis ini!")

mulai = input("Apakah kamu ingin memulai? [y/n]")

if mulai.lower() != "y":
    quit()

print("Oke! ayo mulai :)")
score = 0

jawaban = input("Apa kepanjangan dari CPU? ")
if jawaban.lower() == "central processing unit":
    print('Benar!')
    score += 1
else:
    print("Salah!")

jawaban = input("Apa kepanjanga dari GPU? ")
if jawaban.lower() == "graphics processing unit":
    print('Benar!')
    score += 1
else:
    print("Salah!")

jawaban = input("apa kepanjangan dari RAM? ")
if jawaban.lower() == "random access memory":
    print('Benar!')
    score += 1
else:
    print("Salah!")

jawaban = input("Apa keapanjangan dari PSU? ")
if jawaban.lower() == "power supply":
    print('Benar!')
    score += 1
else:
    print("Salah!")

print(" Anda berhasil menjawab " + str(score) + " Pertanyaan benar!")
print(" Anda benar " + str((score / 4 ) * 100) + "%.")
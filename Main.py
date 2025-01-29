import time
import datetime
from babel.dates import format_date
import sys
import shutil
import os

def hapus_layar():
    # penghapus layar
    if os.name == "nt":  # Windows
        os.system("cls")
    else:  # macOS dan Linux
        os.system("clear")

def logo():
    # fungsi logo
    lebar_terminal = shutil.get_terminal_size().columns
    spasi = " " * ((lebar_terminal - 30) // 2)
    print("\n" + spasi + """
       =========================
      |				|
      |		BOOT AI		|
      |				|
       ==========================
   
""")
    print(spasi + " Selamat datang di Chatbot AI ")
    print(spasi + "-------------------------------")

def loading_proses(teks, waktu=10):
    # fungsi loading
    print(teks)
    for i in range(waktu+1):
        proses = i * 10
        sys.stdout.write("\r >>.Proses: [{}{}] {}%".format("#" * (proses // 10), "-" * (10 - proses // 10), proses))
        sys.stdout.flush()
        time.sleep(1)
    print("\n")
    
def salam_waktu():
    jam_sekarang = datetime.datetime.now().hour
    if 1 <= jam_sekarang <= 9:
        return "Selamat pagi!"
    elif 10 <= jam_sekarang <= 12:
        return "Selamat siang!"
    elif 13 <= jam_sekarang <= 15:
        return "Selamat siang!"
    elif 16 <= jam_sekarang <= 18:
        return "Selamat sore!"
    else:
        return "Selamat malam!"
        
def tanggal_hariini():
	# menampilkan tanggal sekarang
	hari_ini=datetime.datetime.now()
	return format_date(hari_ini,format='full',locale='id_ID')

def buat_data_file():
    # Membuat file jika belum ada
    file_name = "data.txt"
    try:
        with open(file_name, "x") as file:
            pass
        print(f"File {file_name} berhasil dibuat.")
    except FileExistsError:
        print("Data file siap di muat !")
        
def edit_data_file(pertanyaan,jawaban):
    # fungsi Menambah isi file
    file_name = "data.txt"
    with open(file_name, "a") as file:
        file.write(f"{pertanyaan}:{jawaban}\n")
        print("data di simpan !")

def cari_jawaban(pertanyaan):
    try:
        with open("data.txt", "r") as file:
            for line in file:
                line = line.strip()
                if ":" in line:
                    p, j = line.split(":")
                    if p.lower() == pertanyaan.lower():
                        return j.strip()
    except FileNotFoundError:
        print("File data.txt tidak ditemukan.")
    except Exception as e:
        print(f"Kesalahan: {e}")
    return None
   
def main ():
	loading_proses(" >>.mennyalakan program !",)
	nama = input(" siyapa nama anda? ")
	buat_data_file()
	loading_proses(">>.Memuat data: ")
	print("MULAI:")
	time.sleep(2)
	hapus_layar()
	logo()
	print(salam_waktu(),nama)
	print("ada yang bisa saya bantu ?")
	while True:
		pertanyaan = input(nama+': ').lower()
		if pertanyaan == "hari apa ini":
			print(tanggal_hariini())
		elif pertanyaan == "selesai":
			exit()
		else :
			jawaban=cari_jawaban(pertanyaan)
			if jawaban :
				print ('chatboot:',jawaban)
			else:
				print('maaf saya tidak tahu jawaban nya tolong ajari saya:')
				jawaban_baru=input("masukan jawaban nya: ")
				if jawaban_baru:
					edit_data_file(pertanyaan,jawaban_baru)
				else:
					print("jawaban tidak boleh kosong")
								
if __name__ == "__main__":
		main()
		

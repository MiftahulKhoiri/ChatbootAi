import time
import datetime
from babel.dates import format_date
import sys
import shutil
import os
import random
import subprocess

modul_yang_dibutuhkan = ["time","datetime","babel","sys","shutil","os","random","subprocess"]

def hapus_layar():
    # penghapus layar
    if os.name == "nt":  # Windows
        os.system("cls")
    else:  # macOS dan Linux
        os.system("clear")

def cek_install_modul():
    for modul in modul_yang_dibutuhkan:
        try:
            __import__(modul)
            print(f" >>.Modul {modul} sudah terinstal.")
            time.sleep(2)
        except ImportError:
            print(f" >>.Modul {modul} belum terinstal. Menginstal...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", modul])
            print(f" >>.Modul {modul} berhasil diinstal.")
    print(" >>.Semua modul telah diinstal.")

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
        print(" >>.Data file sudah siap")     

def hitung_data():
    # menghitug data yang di simpan 
    file_name = "data.txt"
    try:
        with open(file_name, "r") as file:
            data = file.readlines()
            jumlah_data = len(data)
            print(f" >>.Jumlah data yang disimpan di data bas: {jumlah_data}")
    except FileNotFoundError:
        print(f"File {file_name} tidak ditemukan.")
    except Exception as e:
        print(f"Kesalahan: {e}")

def edit_data_file(pertanyaan, jawaban):
    # fungsi Menambah isi file
    file_name = "data.txt"
    try:
        with open(file_name, "a") as file:
            file.write(f"{pertanyaan}:{jawaban}\n")
        print("data di simpan !")
    except FileNotFoundError:
        print(f"File {file_name} tidak ditemukan.")
    except PermissionError:
        print(f"Anda tidak memiliki izin untuk menulis file {file_name}.")
    except Exception as e:
        print(f"Kesalahan: {e}")

def cari_jawaban(pertanyaan):
    try:
        with open("data.txt", "r") as file:
            jawaban_list = []
            for line in file:
                line = line.strip()
                if ":" in line:
                    p, j = line.split(":")
                    if p.lower() == pertanyaan.lower():
                        jawaban_list = [x.strip() for x in j.split(" | ")]
            if jawaban_list:
                return random.choice(jawaban_list)
            else:
                return "Maaf, saya tidak tahu jawaban untuk pertanyaan tersebut."
    except FileNotFoundError:
        print("File data.txt tidak ditemukan.")
        return None
    except Exception as e:
        print(f"Kesalahan: {e}")
        return None
   
def main ():
	loading_proses(" >>.men nyalakan program !",)
	print(">>.memuat modull yang di butuhkan")
	cek_install_modul()
	buat_data_file()
	hitung_data()
	nama = input(" >>.Masukkan nama anda? ")
	loading_proses(" >>.Memuat data: ")
	print(" >>.semua data sudah siayap:")
	time.sleep(2)
	hapus_layar()
	logo()
	print(salam_waktu(),nama)
	print(" ada yang bisa saya bantu ?")
	while True:
		pertanyaan = input(nama+': ').lower()
		if pertanyaan == "hari apa ini":
			print(tanggal_hariini())
		elif pertanyaan == "exit":
			print (f"chatboot: terimakasih {nama}",cari_jawaban("exit"))
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
		

# AUTHOR : LORDHOZOO
# TEAM : SYSTEM UMBRELLA DRAK999 FOR TEAM HEX PLOIT
# JANGAN RECORD LAMMER YA TANPA IZIN NYA 
# SEKALI LAGI ADA RECORD LAMMER AMPAS GADA SKILL 
import requests
import os
import time
from datetime import datetime
import sys

# Fungsi untuk membersihkan layar
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Fungsi untuk menampilkan banner Hozoo
def show_banner():
    banner = """
\033[91m
╔════════════════════════════════════════════════════════════════╗
║ \033[93m▒█░█░█ █▀▀█ █▀▀█ ░█▀▀█ █▀▀█ █▀▀▄  █▀▀▀ █▀▀ █▀▀█ █▀▀▄ █▀▀█ \033[91m║
║ \033[93m▒█▀▀▄ █▄▄█ █▄▄▀ ▒█▄▄█ █▄▄█ █░░█  █░▀█ █▀▀ █▄▄█ █░░█ █▄▄█ \033[91m║
║ \033[93m▒█░▒█ ▀░░▀ ▀░▀▀ ▒█░▒█ ▀░░▀ ▀▀▀░  ▀▀▀▀ ▀▀▀ ▀░░▀ ▀▀▀░ ▀░░▀ \033[91m║
║                                                        ║
║ \033[97m► TERMUX ONLINE - JARINGAN STABIL                   \033[91m║
║ \033[97m► OFFLINE - JARINGAN GADA - HABIS KUOTA            \033[91m║
║ \033[97m► LORD HOZOO TEAM - ULTIMATE TOOL                  \033[91m║
╚════════════════════════════════════════════════════════════════╝
\033[0m
"""
    print(banner)

# Fungsi untuk menampilkan waktu dan cuaca
def show_time_weather():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%A, %d %B %Y")
    
    print(f"\033[94m┌────────────────────────────────────────────────────────┐")
    print(f"│ \033[92m🕐 WAKTU   : {current_time}                          \033[94m│")
    print(f"│ \033[92m📅 HARI    : {current_date}          \033[94m│")
    print(f"│ \033[92m☁️  CUACA  : Cerah Berawan - 28°C                    \033[94m│")
    print(f"└────────────────────────────────────────────────────────┘\033[0m")

# Fungsi login
def login():
    clear_screen()
    show_banner()
    
    print("\033[91m┌────────────────────────────────────────────────────────┐")
    print("\033[91m│                    \033[97mLOGIN SYSTEM\033[91m                      │")
    print("\033[91m└────────────────────────────────────────────────────────┘\033[0m")
    
    username = input("\033[93m[*] USERNAME: \033[97m")
    password = input("\033[93m[*] PASSWORD: \033[97m")
    
    if username == "LORDHOZOO" and password == "123456":
        print("\033[92m[✓] Login berhasil! Mengakses sistem...\033[0m")
        time.sleep(2)
        return True
    else:
        print("\033[91m[✗] Login gagal! Username atau password salah.\033[0m")
        print("\033[91m[*] Jika lupa password, hubungi: xdg-open 'https://wa.me/6285602222719'\033[0m")
        time.sleep(3)
        return False

# Fungsi navigasi
def show_navigation():
    print("\033[91m┌────────────────────────────────────────────────────────┐")
    print("\033[91m│ \033[97mNAVIGASI: [1] KIRIM LAPORAN │ [2] INFO │ [3] KELUAR \033[91m│")
    print("\033[91m└────────────────────────────────────────────────────────┘\033[0m")

# Fungsi utama
def main():
    if not login():
        return
    
    while True:
        clear_screen()
        show_banner()
        show_time_weather()
        show_navigation()
        
        choice = input("\033[93m[*] PILIH MENU [1-3]: \033[97m")
        
        if choice == "1":
            send_report()
        elif choice == "2":
            show_info()
        elif choice == "3":
            print("\033[92m[✓] Terima kasih telah menggunakan tools LORD HOZOO!\033[0m")
            break
        else:
            print("\033[91m[✗] Pilihan tidak valid!\033[0m")
            time.sleep(2)

def send_report():
    clear_screen()
    show_banner()
    
    print("\033[91m┌────────────────────────────────────────────────────────┐")
    print("\033[91m│                   \033[97mKIRIM LAPORAN\033[91m                      │")
    print("\033[91m└────────────────────────────────────────────────────────┘\033[0m")
    
    # MASUKIN NOMOR TARGET
    target_number = input("\033[93m[*] MASUKIN NOMOR TARGET: \033[97m")
    
    if not target_number:
        target_number = "+6285602222719"  # Default number
    
    # Endpoint kontak WhatsApp
    url = "https://www.whatsapp.com/contact/?subject=messenger"

    # Data yang ingin dikirim (payload)
    payload = {
        "phone_number": target_number,
        "email": "hozoonethunter@gmail.com",
        "confirm_email": "hozoonethunter@gmail.com",
        "platform": "Android",
        "message": f"""Masalah Akun WhatsApp Terblokir

Kepada Tim WhatsApp yang terhormat,

Saya menerima pesan yang mengatakan "Akun ini tidak dapat lagi menggunakan WhatsApp." Saya yakin ini mungkin kesalahan. Saya selalu berusaha mengikuti aturan WhatsApp, dan jika saya tanpa sengaja melakukan kesalahan, saya mohon maaf yang sebesar-besarnya.

Mohon tinjau kembali kasus saya dan beri saya kesempatan lagi. Akun ini sangat penting untuk penggunaan sehari-hari saya.

Terima kasih atas dukungan Anda.

Hormat saya,  
hozoo  
Nomor Telepon: {target_number}"""
    }

    # Header mirip browser
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    print("\033[93m[*] Mengirim laporan...\033[0m")
    
    try:
        # Kirim POST request
        response = requests.post(url, data=payload, headers=headers)

        # Cek hasil
        if response.status_code == 200:
            print("\033[92m[✓] Laporan berhasil dikirim ke nomor:", target_number, "\033[0m")
        else:
            print(f"\033[91m[✗] Gagal: {response.status_code}\033[0m")
            
    except Exception as e:
        print(f"\033[91m[✗] Error: {str(e)}\033[0m")
    
    input("\033[93m[*] Tekan Enter untuk kembali...\033[0m")

def show_info():
    clear_screen()
    show_banner()
    
    print("\033[91m┌────────────────────────────────────────────────────────┐")
    print("\033[91m│                      \033[97mINFORMASI\033[91m                       │")
    print("\033[91m└────────────────────────────────────────────────────────┘\033[0m")
    
    info = """
\033[97m╔════════════════════════════════════════════════════════════════╗
║ \033[92m                   LORD HOZOO TEAM TOOLS                    \033[97m║
╠════════════════════════════════════════════════════════════════╣
║ \033[93m► Developer   : LORD HOZOO                                 \033[97m║
║ \033[93m► Version     : 2.0 Premium                               \033[97m║
║ \033[93m► Contact     : +62 856-0222-2719                         \033[97m║
║ \033[93m► Email       : hozoonethunter@gmail.com                  \033[97m║
║ \033[93m► Features    : WhatsApp Report System                    \033[97m║
║ \033[93m► Status      : Termux Online - Jaringan Stabil           \033[97m║
╚════════════════════════════════════════════════════════════════╝\033[0m
"""
    print(info)
    input("\033[93m[*] Tekan Enter untuk kembali...\033[0m")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\033[91m[!] Program dihentikan oleh user\033[0m")
    except Exception as e:
        print(f"\033[91m[!] Error: {str(e)}\033[0m")

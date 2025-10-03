# lammer apain buka script gw lammer jangan record susah payah gw bikin 
import requests
import os
import time
from datetime import datetime
import sys
import socket

# Fungsi untuk membersihkan layar
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Fungsi untuk mengecek koneksi internet
def check_internet():
    """
    Mengecek status koneksi internet dengan beberapa metode
    Mengembalikan: "ONLINE", "OFFLINE", atau "HABIS KUOTA"
    """
    try:
        # Method 1: Socket connection to Google DNS
        socket.setdefaulttimeout(3)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(("8.8.8.8", 53))
        return "ONLINE"
    except socket.error:
        pass
    
    try:
        # Method 2: HTTP request to reliable site
        response = requests.get("http://216.58.192.142", timeout=5)  # Google IP
        if response.status_code == 200:
            return "ONLINE"
    except (requests.ConnectionError, requests.Timeout):
        pass
    except Exception:
        return "HABIS KUOTA"
    
    return "OFFLINE"

# Fungsi untuk menampilkan banner Hozoo
def show_banner():
    banner = """
\033[91m
╔════════════════════════════════════════════════════════════════╗
║ \033[93m▒█░█░█ █▀▀█ █▀▀█ ░█▀▀█ █▀▀█ █▀▀▄  █▀▀▀ █▀▀ █▀▀█ █▀▀▄ █▀▀█ \033[91m║
║ \033[93m▒█▀▀▄ █▄▄█ █▄▄▀ ▒█▄▄█ █▄▄█ █░░█  █░▀█ █▀▀ █▄▄█ █░░█ █▄▄█ \033[91m║
║ \033[93m▒█░▒█ ▀░░▀ ▀░▀▀ ▒█░▒█ ▀░░▀ ▀▀▀░  ▀▀▀▀ ▀▀▀ ▀░░▀ ▀▀▀░ ▀░░▀ \033[91m║
║                                                        ║
║ \033[97m► LORD HOZOO TEAM - ULTIMATE TOOL                  \033[91m║
╚════════════════════════════════════════════════════════════════╝
\033[0m
"""
    print(banner)

# Fungsi untuk menampilkan waktu dan status jaringan
def show_time_network():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%A, %d %B %Y")
    
    # Cek status internet
    internet_status = check_internet()
    
    # Tentukan warna dan ikon berdasarkan status
    if internet_status == "ONLINE":
        status_color = "\033[92m"  # Hijau
        status_icon = "🟢"
        status_text = "TERMUX ONLINE - JARINGAN STABIL"
    elif internet_status == "HABIS KUOTA":
        status_color = "\033[93m"  # Kuning
        status_icon = "🟡"
        status_text = "ADA SINYAL TAPI HABIS KUOTA"
    else:
        status_color = "\033[91m"  # Merah
        status_icon = "🔴"
        status_text = "OFFLINE - JARINGAN GADA - HABIS KUOTA"
    
    print(f"\033[94m┌────────────────────────────────────────────────────────┐")
    print(f"│ \033[92m🕐 WAKTU   : {current_time}                          \033[94m│")
    print(f"│ \033[92m📅 HARI    : {current_date}          \033[94m│")
    print(f"│ \033[92m☁️  CUACA  : Cerah Berawan - 28°C                    \033[94m│")
    print(f"│ {status_icon} {status_color}{status_text:<43}\033[94m│")
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
        show_time_network()
        show_navigation()
        
        choice = input("\033[93m[*] PILIH MENU [1-3]: \033[97m")
        
        if choice == "1":
            # Cek internet sebelum kirim laporan
            internet_status = check_internet()
            if internet_status != "ONLINE":
                print(f"\033[91m[✗] Gagal! Status jaringan: {internet_status}\033[0m")
                print("\033[91m[*] Periksa koneksi internet atau kuota Anda\033[0m")
                input("\033[93m[*] Tekan Enter untuk kembali...\033[0m")
                continue
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
    
    # Cek internet lagi sebelum proses
    internet_status = check_internet()
    if internet_status != "ONLINE":
        print(f"\033[91m[✗] Tidak dapat melanjutkan. Status: {internet_status}\033[0m")
        input("\033[93m[*] Tekan Enter untuk kembali...\033[0m")
        return
    
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

    # Header mirip browser :cite[1]:cite[4]:cite[6]
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "id-ID,id;q=0.9,en;q=0.8",
        "Connection": "keep-alive"
    }

    print("\033[93m[*] Mengecek koneksi...\033[0m")
    print("\033[92m[✓] Jaringan stabil, mengirim laporan...\033[0m")
    
    try:
        # Kirim POST request :cite[4]
        response = requests.post(url, data=payload, headers=headers, timeout=30)

        # Cek hasil
        if response.status_code == 200:
            print("\033[92m[✓] Laporan berhasil dikirim ke nomor:", target_number, "\033[0m")
        else:
            print(f"\033[91m[✗] Gagal: {response.status_code}\033[0m")
            print(f"\033[93m[*] Response: {response.text[:200]}\033[0m")
            
    except requests.exceptions.Timeout:
        print("\033[91m[✗] Timeout: Koneksi terlalu lama\033[0m")
        print("\033[91m[*] Mungkin jaringan lambat atau habis kuota\033[0m")
    except requests.exceptions.ConnectionError:
        print("\033[91m[✗] Connection Error: Tidak dapat terhubung ke server\033[0m")
        print("\033[91m[*] Periksa koneksi internet Anda\033[0m")
    except Exception as e:
        print(f"\033[91m[✗] Error: {str(e)}\033[0m")
    
    input("\033[93m[*] Tekan Enter untuk kembali...\033[0m")

def show_info():
    clear_screen()
    show_banner()
    
    print("\033[91m┌────────────────────────────────────────────────────────┐")
    print("\033[91m│                      \033[97mINFORMASI\033[91m                       │")
    print("\033[91m└────────────────────────────────────────────────────────┘\033[0m")
    
    # Cek status internet untuk info
    internet_status = check_internet()
    
    info = f"""
\033[97m╔════════════════════════════════════════════════════════════════╗
║ \033[92m                   LORD HOZOO TEAM TOOLS                    \033[97m║
╠════════════════════════════════════════════════════════════════╣
║ \033[93m► Developer   : LORD HOZOO                                 \033[97m║
║ \033[93m► Version     : 2.1 Premium                               \033[97m║
║ \033[93m► Contact     : +62 856-0222-2719                         \033[97m║
║ \033[93m► Email       : hozoonethunter@gmail.com                  \033[97m║
║ \033[93m► Features    : WhatsApp Report System                    \033[97m║
║ \033[93m► Status      : {internet_status:<30} \033[97m║
║ \033[93m► Deteksi     : Online/Offline/Habis Kuota                \033[97m║
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

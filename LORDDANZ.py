import requests
import os
import time
from datetime import datetime
import sys
import socket
from fake_useragent import UserAgent
import subprocess

# Fungsi untuk membersihkan layar
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Fungsi untuk install dependencies
def install_dependencies():
    """Menginstall semua dependencies yang diperlukan"""
    print("\033[93m[*] Memeriksa dan menginstall dependencies...\033[0m")
    
    packages = [
        "python",
        "python-pip", 
        "python-numpy",
        "ffmpeg",
        "tinyproxy"
    ]
    
    pip_packages = [
        "requests",
        "fake-useragent", 
        "rich",
        "pycryptodome",
        "pygame",
        "weathercom"
    ]
    
    for pkg in packages:
        try:
            print(f"\033[93m[*] Menginstall {pkg}...\033[0m")
            subprocess.run(f"pkg install {pkg} -y", shell=True, check=True)
            print(f"\033[92m[✓] {pkg} berhasil diinstall\033[0m")
        except subprocess.CalledProcessError:
            print(f"\033[91m[✗] Gagal menginstall {pkg}\033[0m")
    
    for pip_pkg in pip_packages:
        try:
            print(f"\033[93m[*] Menginstall {pip_pkg} via pip...\033[0m")
            subprocess.run(f"pip install {pip_pkg}", shell=True, check=True)
            print(f"\033[92m[✓] {pip_pkg} berhasil diinstall\033[0m")
        except subprocess.CalledProcessError:
            print(f"\033[91m[✗] Gagal menginstall {pip_pkg}\033[0m")
    
    print("\033[92m[✓] Semua dependencies selesai diinstall\033[0m")
    time.sleep(2)

# Fungsi untuk mendapatkan proxy gratis dari web
def get_free_proxies():
    """Mendapatkan list proxy gratis dari berbagai sumber"""
    print("\033[93m[*] Mendapatkan proxy gratis dari web...\033[0m")
    
    proxy_sources = [
        "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all",
        "https://proxylist.geonode.com/api/proxy-list?limit=50&page=1&sort_by=lastChecked&sort_type=desc",
        "https://www.proxy-list.download/api/v1/get?type=http"
    ]
    
    proxies = []
    for source in proxy_sources:
        try:
            ua = UserAgent()
            headers = {'User-Agent': ua.random}
            response = requests.get(source, headers=headers, timeout=10)
            if response.status_code == 200:
                # Parse proxy list dari berbagai format
                lines = response.text.strip().split('\n')
                for line in lines:
                    line = line.strip()
                    if ':' in line and not line.startswith('#'):
                        if len(line.split(':')) == 2:
                            proxies.append(f"http://{line}")
                print(f"\033[92m[✓] Berhasil mendapatkan {len(proxies)} proxy\033[0m")
                break
        except Exception as e:
            print(f"\033[91m[✗] Gagal dari sumber: {e}\033[0m")
            continue
    
    return proxies

# Fungsi untuk mengecek koneksi internet dengan proxy
def check_internet_with_proxy(proxy_list=None):
    """
    Mengecek status koneksi internet dengan beberapa metode
    Mengembalikan: "ONLINE", "OFFLINE", "HABIS KUOTA", atau "PROXY_READY"
    """
    # Cek tanpa proxy dulu
    try:
        socket.setdefaulttimeout(5)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(("8.8.8.8", 53))
        return "ONLINE"
    except socket.error:
        pass
    
    # Jika ada sinyal tapi tidak bisa akses, coba dengan proxy
    if proxy_list:
        for proxy in proxy_list[:5]:  # Coba 5 proxy pertama
            try:
                ua = UserAgent()
                proxies = {
                    'http': proxy,
                    'https': proxy
                }
                headers = {'User-Agent': ua.random}
                response = requests.get(
                    "http://httpbin.org/ip", 
                    proxies=proxies, 
                    headers=headers, 
                    timeout=10
                )
                if response.status_code == 200:
                    print(f"\033[92m[✓] Proxy {proxy} berhasil\033[0m")
                    return "PROXY_READY", proxy
            except Exception:
                continue
    
    # Cek tanpa proxy method 2
    try:
        response = requests.get("http://216.58.192.142", timeout=5)
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
║ \033[97m► LORD HOZOO TEAM - ULTIMATE TOOL + PROXY SYSTEM    \033[91m║
╚════════════════════════════════════════════════════════════════╝
\033[0m
"""
    print(banner)

# Fungsi untuk menampilkan waktu dan status jaringan dengan proxy
def show_time_network():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%A, %d %B %Y")
    
    # Dapatkan proxy list
    proxy_list = get_free_proxies()
    
    # Cek status internet dengan proxy
    internet_result = check_internet_with_proxy(proxy_list)
    
    if isinstance(internet_result, tuple) and internet_result[0] == "PROXY_READY":
        internet_status = "PROXY_READY"
        current_proxy = internet_result[1]
        status_color = "\033[96m"  # Cyan
        status_icon = "🔵"
        status_text = "PROXY ONLINE - JARINGAN BYPASS"
    elif internet_status == "ONLINE":
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
    if internet_status == "PROXY_READY":
        print(f"│ \033[96m🔷 PROXY   : {current_proxy:<34} \033[94m│")
    print(f"└────────────────────────────────────────────────────────┘\033[0m")
    
    return internet_status, proxy_list

# Fungsi untuk mengirim laporan dengan proxy
def send_report_with_proxy(proxy_list):
    clear_screen()
    show_banner()
    
    print("\033[91m┌────────────────────────────────────────────────────────┐")
    print("\033[91m│              \033[97mKIRIM LAPORAN DENGAN PROXY\033[91m              │")
    print("\033[91m└────────────────────────────────────────────────────────┘\033[0m")
    
    # MASUKIN NOMOR TARGET
    target_number = input("\033[93m[*] MASUKIN NOMOR TARGET: \033[97m")
    
    if not target_number:
        target_number = "+6285602222719"  # Default number
    
    # Pilih proxy yang bekerja
    working_proxy = None
    for proxy in proxy_list:
        try:
            ua = UserAgent()
            proxies = {'http': proxy, 'https': proxy}
            headers = {'User-Agent': ua.random}
            
            test_response = requests.get(
                "http://httpbin.org/ip", 
                proxies=proxies, 
                headers=headers, 
                timeout=10
            )
            if test_response.status_code == 200:
                working_proxy = proxy
                print(f"\033[92m[✓] Menggunakan proxy: {proxy}\033[0m")
                break
        except Exception:
            continue
    
    if not working_proxy:
        print("\033[91m[✗] Tidak ada proxy yang bekerja, menggunakan koneksi langsung\033[0m")
        proxies = None
    else:
        proxies = {'http': working_proxy, 'https': working_proxy}
    
    # Data payload
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

    # Header dengan user agent acak
    ua = UserAgent()
    headers = {
        "User-Agent": ua.random,
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "id-ID,id;q=0.9,en;q=0.8",
        "Connection": "keep-alive"
    }

    print("\033[93m[*] Mengirim laporan melalui proxy...\033[0m")
    
    try:
        # Kirim POST request dengan proxy
        if proxies:
            response = requests.post(
                "https://www.whatsapp.com/contact/?subject=messenger",
                data=payload, 
                headers=headers, 
                proxies=proxies,
                timeout=30
            )
        else:
            response = requests.post(
                "https://www.whatsapp.com/contact/?subject=messenger",
                data=payload, 
                headers=headers,
                timeout=30
            )

        # Cek hasil
        if response.status_code == 200:
            print("\033[92m[✓] Laporan berhasil dikirim ke nomor:", target_number, "\033[0m")
            if working_proxy:
                print("\033[96m[✓] Berhasil menggunakan proxy system\033[0m")
        else:
            print(f"\033[91m[✗] Gagal: {response.status_code}\033[0m")
            
    except requests.exceptions.Timeout:
        print("\033[91m[✗] Timeout: Koneksi terlalu lama\033[0m")
    except requests.exceptions.ConnectionError:
        print("\033[91m[✗] Connection Error: Tidak dapat terhubung ke server\033[0m")
    except Exception as e:
        print(f"\033[91m[✗] Error: {str(e)}\033[0m")
    
    input("\033[93m[*] Tekan Enter untuk kembali...\033[0m")

# Fungsi utama yang dimodifikasi
def main():
    # Tawarkan install dependencies di awal
    clear_screen()
    show_banner()
    install_choice = input("\033[93m[*] Install dependencies terlebih dahulu? (y/n): \033[97m")
    if install_choice.lower() == 'y':
        install_dependencies()
    
    if not login():
        return
    
    while True:
        clear_screen()
        show_banner()
        internet_status, proxy_list = show_time_network()
        show_navigation()
        
        choice = input("\033[93m[*] PILIH MENU [1-3]: \033[97m")
        
        if choice == "1":
            # Gunakan fungsi baru dengan proxy
            send_report_with_proxy(proxy_list)
        elif choice == "2":
            show_info()
        elif choice == "3":
            print("\033[92m[✓] Terima kasih telah menggunakan tools LORD HOZOO!\033[0m")
            break
        else:
            print("\033[91m[✗] Pilihan tidak valid!\033[0m")
            time.sleep(2)

# ... (fungsi login, show_navigation, show_info tetap sama seperti sebelumnya)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\033[91m[!] Program dihentikan oleh user\033[0m")
    except Exception as e:
        print(f"\033[91m[!] Error: {str(e)}\033[0m")

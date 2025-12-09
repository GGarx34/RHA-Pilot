# 🚀 RHA-Pilot

**RHA-Pilot** adalah alat otomatisasi berbasis **Python** dan **Selenium** untuk membantu navigasi materi kursus Red Hat Academy (RHA).

---

## 📥 Pilihan Instalasi

Pilih salah satu metode yang sesuai dengan kebutuhan Anda:

### ⚡ Opsi 1: Standalone (.exe) - *Direkomendasikan*
Gunakan opsi ini jika Anda tidak ingin repot menginstal Python.
1.  Download file **`RHA-Pilot.exe`** dari daftar file di atas.
2.  Klik dua kali file **`RHA-Pilot.exe`**.
3.  Aplikasi langsung berjalan!

> *Catatan: Jika Antivirus/Windows Defender memblokir, klik "More Info" -> "Run Anyway". Ini wajar karena aplikasi belum ditandatangani sertifikat digital.*

### 🛠️ Opsi 2: Via Source Code (Developer)
Gunakan opsi ini jika Anda adalah pengembang yang ingin menjalankan via terminal.

#### ⚠️ Persyaratan Sistem (Khusus Opsi 2)
* **OS:** Windows 10/11 (64-bit)
* **Python:** Versi **3.11.x** (Wajib)
    > 🛑 **Penting:** Python 3.12 atau versi lain **tidak didukung** karena kompatibilitas mesin biner `.pyd`.

#### Langkah Instalasi:
Jalankan perintah berikut di terminal Anda (Git Bash / CMD):

**1. Clone & Masuk ke Direktori**
```bash
git clone [https://github.com/GGarx34/RHA-Pilot.git](https://github.com/GGarx34/RHA-Pilot.git)
```
```bash
cd RHA-Pilot
```

2. Install Dependensi
```bash
pip install -r requirements.txt
```

4. Jalankan Aplikasi
```bash
python main.py
```

🎮 Cara Penggunaan

Baik menggunakan .exe maupun python main.py, langkah penggunaannya sama:
```bash

    Kredensial: Masukkan Username & Password Red Hat Academy Anda.

    Target URL: Paste Link halaman kursus yang ingin dijalankan.

    Browser: Pilih Chrome (1), Firefox (2), atau Edge (3).

    Delay: Tentukan jeda waktu (detik) antar halaman.
```

❓ Troubleshooting
```bash
    ImportError / Module not found:

        > Pastikan Anda menggunakan Python 3.11. Cek dengan perintah python --version.

    Browser tertutup sendiri:

        > Update browser Chrome/Firefox/Edge Anda ke versi terbaru.

    Error Function not found:

        > Pastikan file lgmx.pyd (atau rha.pyd) berada di satu folder dengan main.py.

    Windows Protected PC (Blue Screen):

        > Saat menjalankan .exe, klik More Info > Run Anyway.
```
📜 Disclaimer

Educational purpose only. Gunakan alat ini dengan bijak untuk membantu pembelajaran. Pengembang tidak bertanggung jawab atas penyalahgunaan.

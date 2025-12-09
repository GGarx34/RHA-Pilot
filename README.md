# 🚀 RHA-Pilot

**RHA-Pilot** adalah alat otomatisasi berbasis **Python** dan **Selenium** untuk membantu navigasi materi kursus Red Hat Academy (RHA). Menggunakan core engine terkompilasi (`.pyd`) untuk performa maksimal dan keamanan kode.

---

### ⚠️ Persyaratan Sistem (Wajib)
Agar aplikasi berjalan lancar, pastikan sistem Anda memenuhi syarat berikut:
* **OS:** Windows 10/11 (64-bit)
* **Python:** Versi **3.11.x**
    > 🛑 **Penting:** Python 3.12 atau versi lain **tidak didukung** karena kompatibilitas mesin biner.

---

### ⚡ Quick Start

Jalankan perintah berikut di terminal Anda (Git Bash / CMD) secara berurutan:

**1. Clone & Masuk ke Direktori**
```bash
git clone https://github.com/GGarx34/RHA-Pilot.git
```
```bash
cd RHA-Pilot
```

2. Install Dependensi
```bash
pip install -r requirements.txt
```

3. Jalankan Aplikasi
```bash
python main.py
```

## 🎮 Cara Penggunaan

Setelah script berjalan, masukkan data berikut saat diminta:

    Kredensial: 
      > Username & Password Red Hat Academy.

    Target URL:
      > Link halaman kursus yang ingin dijalankan.

    Browser:
      > Pilih Chrome (1), Firefox (2), atau Edge (3).

## ❓ Troubleshooting

    ImportError / Module not found: 
      > Pastikan Anda menggunakan Python 3.11. Cek dengan python --version.

    Browser tertutup sendiri: 
      > Update browser Anda ke versi terbaru.

    Error Function not found:
      > Pastikan file rha.pyd ada di satu folder dengan main.py.

## 📜 Disclaimer

Educational purpose only. Gunakan alat ini dengan bijak untuk membantu pembelajaran. Pengembang tidak bertanggung jawab atas penyalahgunaan.
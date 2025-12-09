import sys
import time
import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

try:
    import lgmx
except ImportError:
    print("[ERROR] File tidak ditemukan!")
    input("Tekan Enter untuk keluar...")
    sys.exit()

if __name__ == "__main__":
    try:
        clear()
        lgmx.run_logic()
    except AttributeError:
        print("[ERROR] Fungsi tidak ditemukan")
    except KeyboardInterrupt:
        print("\n[INFO] Program dihentikan pengguna.")
    except Exception as e:
        print(f"\n[CRITICAL ERROR] Terjadi kesalahan: {e}")
    
    input("\nTekan Enter untuk menutup...")
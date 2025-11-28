#!/data/data/com.termux/files/usr/bin/bash

echo "========================================"
echo "   SETUP TERMUX + AUTO DOWNLOAD SCRIPT  "
echo "========================================"

pkg update -y
pkg upgrade -y
pkg install python -y
pkg install tsu -y
pkg install wget -y

echo "========================================"
echo "⬇️ DOWNLOAD SCRIPT PYTHON"
echo "========================================"

# Pastikan kamu sudah ganti USERNAME dan REPO dengan punyamu sendiri
wget -O /sdcard/Download/moveye.py "https://raw.githubusercontent.com/Whinter733/winter12/refs/heads/main/moveye.py"

chmod +x /sdcard/Download/moveye.py

echo "========================================"
echo "▶️ MENJALANKAN SCRIPT"
echo "========================================"

tsu -c "python /sdcard/Download/moveye.py"

echo "========================================"
echo '✅ SETUP + EKSEKUSI SELESAI'
echo "========================================"

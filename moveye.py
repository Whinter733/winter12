import os
import shutil

file_map = [
    (
        "/sdcard/Download/com.mangcut.rulod/app_webview/Default/Cookies",
        "/data/data/com.mangcut.rulod/app_webview/Default/Cookies"
    ),
    (
        "/sdcard/Download/com.mangcut.ruloe/app_webview/Default/Cookies",
        "/data/data/com.mangcut.ruloe/app_webview/Default/Cookies"
    ),
    (
        "/sdcard/Download/com.mangcut.rulof/app_webview/Default/Cookies",
        "/data/data/com.mangcut.rulof/app_webview/Default/Cookies"
    ),
    (
        "/sdcard/Download/com.mangcut.rulog/app_webview/Default/Cookies",
        "/data/data/com.mangcut.rulog/app_webview/Default/Cookies"
    ),
]

for src, dst in file_map:
    try:
        # ✅ JIKA FILE DOWNLOAD TIDAK ADA → BACKUP DARI DATA
        if not os.path.exists(src):
            if os.path.exists(dst):
                os.makedirs(os.path.dirname(src), exist_ok=True)
                shutil.copy2(dst, src)
                print(f"[🔁 BACKUP] {dst} → {src}")
            else:
                print(f"[❌] Tidak ada file untuk backup: {dst}")
            continue

        # ✅ JIKA FILE DOWNLOAD ADA → PINDAHKAN KE DATA
        os.makedirs(os.path.dirname(dst), exist_ok=True)

        if os.path.exists(dst):
            os.remove(dst)

        shutil.move(src, dst)
        print(f"[✅ PINDAH] {src} → {dst}")

    except Exception as e:
        print(f"[⚠️ ERROR] {src}\n{e}\n")

print("✅ SEMUA PROSES SELESAI.")

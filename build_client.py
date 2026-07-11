import os
import zipfile

def initiate_build():
    print("==================================================")
    print("   GARUDAXYBER.INC - AUTOMATED BUILD SYSTEM       ")
    print("   Project: Roblox_ahh~.apkg                      ")
    print("==================================================")
    
    # 1. Membuat direktori output 'dist' jika belum ada
    output_dir = "dist"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"[*] Membuat folder output: {output_dir}/")
        
    output_file = os.path.join(output_dir, "Roblox_ahh~.apkg")
    
    # 2. Proses bundling dummy/core files ke dalam format .apkg (ZIP-based bundle)
    print("[*] Memulai proses kompilasi komponen package...")
    try:
        with zipfile.ZipFile(output_file, 'w', zipfile.ZIP_DEFLATED) as apkg_bundle:
            # Membuat manifest sederhana di dalam bundle
            manifest_content = (
                "Package-Name: Roblox_ahh~\n"
                "Extension: .apkg\n"
                "Developer: GarudaXyber.inc\n"
                "Security-Status: No-Parental-Control / Optimized\n"
            )
            apkg_bundle.writestr("bundle_manifest.txt", manifest_content)
            print("[+] bundle_manifest.txt berhasil ditanamkan.")
            
        print("==================================================")
        print(f"[SUCCESS] File berhasil di-build: {output_file}")
        print("==================================================")
    except Exception as e:
        print(f"[ERROR] Proses build gagal: {str(e)}")

if __name__ == "__main__":
    initiate_build()
  

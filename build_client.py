import os

def create_installer_structure():
    # Membuat struktur folder Android project
    structure = [
        "app/src/main/java/com/garudaxyber/installer",
        "app/src/main/res/layout",
        "dist"
    ]
    
    for path in structure:
        os.makedirs(path, exist_ok=True)
    
    print("[*] Struktur source code Apkg Installer berhasil dibuat.")
    
    # Menulis AndroidManifest.xml (Wajib ada untuk Installer)
    manifest = """<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.garudaxyber.installer">
    <uses-permission android:name="android.permission.REQUEST_INSTALL_PACKAGES" />
    <application android:label="Apkg Installer">
        <activity android:name=".MainActivity">
            <intent-filter>
                <action android:name="android.intent.action.VIEW" />
                <category android:name="android.intent.category.DEFAULT" />
                <data android:mimeType="application/octet-stream" />
            </intent-filter>
        </activity>
    </application>
</manifest>"""
    
    with open("app/src/main/AndroidManifest.xml", "w") as f:
        f.write(manifest)
    print("[+] AndroidManifest.xml generated.")

if __name__ == "__main__":
    create_installer_structure()
    

# setup.py
import platform
import subprocess

def setup_windows():
    print("Configuración para windows...")
    subprocess.run(["pip", "install", "windows-specific-package"])

def setup_mac():
    print("Configuración para MacOs...")
    # Ejemplo: instalar un paquete específico de macOS
    subprocess.run(["pip", "install", "macos-specific-package"])

def setup_linux():
    print("Configuración para Linux...")
    # Ejemplo: instalar un paquete específico de Linux
    subprocess.run(["pip", "install", "linux-specific-package"])

def main():
    os_type = platform.system()
    print(f"Detectar sistem operativo: {os_type}")

    if os_type == "Windows":
        setup_windows()
    elif os_type == "Darwin":
        setup_mac()
    elif os_type == "Linux":
        setup_linux()
    else:
        print("No es posible reconocer el sistema operativo")

if __name__ == "__main__":
    main()
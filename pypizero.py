import time
import platform
import socket
from datetime import datetime

LOG_FILE = "log.txt"

def get_system_info():
    return {
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "hostname": socket.gethostname(),
        "ip": socket.gethostbyname(socket.gethostname()),
        "system": platform.system(),
        "release": platform.release(),
        "machine": platform.machine()
    }

def write_log(info):
    line = (
        f"[{info['time']}] "
        f"{info['hostname']} | "
        f"{info['ip']} | "
        f"{info['system']} {info['release']} | "
        f"{info['machine']}\n"
    )

    with open(LOG_FILE, "a") as f:
        f.write(line)

    print(line.strip())

def main():
    print("Iniciando monitor en Raspberry Pi...\n")

    while True:
        info = get_system_info()
        write_log(info)
        time.sleep(5)

if __name__ == "__main__":
    main()
import random
import re
import subprocess
import sys
import time
import urllib.request


def get_wifi_interface() -> str:
    """Finds the active Wi-Fi network device name on macOS (usually en0)."""
    try:
        output = subprocess.check_output(
            ["networksetup", "-listallhardwareports"], text=True
        )
        match = re.search(
            r"Hardware Port:\s*Wi-Fi\nDevice:\s*(\w+)", output, re.IGNORECASE
        )
        if match:
            return match.group(1)
    except Exception:
        pass
    return "en0"  # Default fallback for MacBooks


def get_public_ip(timeout=8) -> str:
    """Fetches the current external public IP."""
    services = [
        "https://api.ipify.org",
        "https://icanhazip.com",
        "https://ifconfig.me/ip",
    ]
    for url in services:
        try:
            req = urllib.request.Request(
                url, headers={"User-Agent": "curl/7.68.0"}
            )
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                ip = resp.read().decode("utf-8").strip()
                if ip:
                    return ip
        except Exception:
            continue
    return "Unavailable / Offline"


def cycle_wifi(interface: str, delay_seconds: float):
    """Turns Wi-Fi OFF, sleeps, and turns Wi-Fi ON using macOS native tools."""
    print(f"[-] Disconnecting {interface}...")
    subprocess.run(
        ["networksetup", "-setairportpower", interface, "off"], check=True
    )

    print(f"[*] Waiting {delay_seconds:.1f} seconds...")
    time.sleep(delay_seconds)

    print(f"[+] Reconnecting {interface}...")
    subprocess.run(
        ["networksetup", "-setairportpower", interface, "on"], check=True
    )


def wait_for_connection(max_wait=20) -> str:
    """Polls until internet connectivity returns and returns the new public IP."""
    sys.stdout.write("[*] Waiting for network to re-establish...")
    sys.stdout.flush()

    start_time = time.time()
    while time.time() - start_time < max_wait:
        ip = get_public_ip(timeout=3)
        if ip != "Unavailable / Offline":
            print(f" Connected!")
            return ip
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(1)

    print(" Timed out.")
    return "Unavailable / Offline"


def rotate_ip():
    interface = get_wifi_interface()
    print("=" * 55)
    print(f" macOS Network Interface Detected: {interface}")

    old_ip = get_public_ip()
    print(f" Current Public IP: {old_ip}")
    print("=" * 55)

    # Random delay between 3 and 5 seconds
    wait_time = random.uniform(3.0, 5.0)
    cycle_wifi(interface, wait_time)

    new_ip = wait_for_connection()

    print("-" * 55)
    print(f" Previous IP : {old_ip}")
    print(f" New IP      : {new_ip}")

    if new_ip != "Unavailable / Offline" and new_ip != old_ip:
        print("[✓] SUCCESS: IP address changed successfully!")
        return True
    else:
        print(
            "[!] NOTICE: IP remained the same (or reconnect failed). See note below."
        )
        return False


if __name__ == "__main__":
    rotate_ip()
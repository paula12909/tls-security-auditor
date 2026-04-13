import ssl
import socket

def scan_tls(host, port):
    context = ssl.create_default_context()

    try:
        with socket.create_connection((host, port)) as sock:
            with context.wrap_socket(sock, server_hostname=host) as ssock:
                print(f"\n[+] Scanning {host}:{port}")
                print("Protocol:", ssock.version())
                print("Cipher:", ssock.cipher())
    except Exception as e:
        print(f"[-] Error scanning {host}:{port} -> {e}")

if __name__ == "__main__":
    scan_tls("insecure_service", 443)
    scan_tls("secure_service", 443)

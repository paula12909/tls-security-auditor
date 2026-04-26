import socket
import ssl
import subprocess
import os


HOST = "0.0.0.0"
PORT = 9443


def generate_cert():
    if os.path.exists("cert.pem") and os.path.exists("key.pem"):
        return

    subprocess.run([
        "openssl",
        "req",
        "-x509",
        "-newkey",
        "rsa:2048",
        "-keyout",
        "key.pem",
        "-out",
        "cert.pem",
        "-days",
        "365",
        "-nodes",
        "-subj",
        "/CN=secure-localhost"
    ], check=True)


def main():
    generate_cert()

    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")

    # Hardened configuration: require TLS 1.2 or newer.
    context.minimum_version = ssl.TLSVersion.TLSv1_2

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((HOST, PORT))
        sock.listen(5)

        print(f"Secure TLS server listening on port {PORT}")

        with context.wrap_socket(sock, server_side=True) as secure_sock:
            while True:
                conn, addr = secure_sock.accept()
                conn.sendall(b"secure tls service\n")
                conn.close()


if __name__ == "__main__":
    main()
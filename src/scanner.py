import socket
import ssl


def scan_target(host: str, port: int) -> dict:
    if port < 1 or port > 65535:
        raise ValueError("Invalid port number")

    result = {
        "host": host,
        "port": port,
        "connected": False,
        "tls_version": None,
        "cipher": None,
        "certificate_present": False,
        "self_signed": False,
        "error": None
    }

    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    try:
        with socket.create_connection((host, port), timeout=3) as sock:
            with context.wrap_socket(sock, server_hostname=host) as tls_sock:
                result["connected"] = True
                result["tls_version"] = tls_sock.version()

                cipher = tls_sock.cipher()
                result["cipher"] = cipher[0] if cipher else None

                cert = tls_sock.getpeercert(binary_form=True)
                result["certificate_present"] = cert is not None

    except Exception as error:
        result["error"] = str(error)

    return result
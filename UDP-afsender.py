import socket
import time
import random

def send_sale_message():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    
    server_address = ('localhost', 14014)

    product_no = 8013
    amount_sold = random.randint(1, 10)

    message = f"Salg: ProductNo={product_no}, AmountSold={amount_sold}"

    try:
        udp_socket.sendto(message.encode(), server_address)
        print(f"Besked sendt: {message}")

    finally:
        udp_socket.close()

if __name__ == "__main__":
    while True:
        send_sale_message()
        time.sleep(random.uniform(1, 3))

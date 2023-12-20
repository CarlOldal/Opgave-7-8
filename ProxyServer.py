import socket
import requests
import json

def receive_sale_data():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    local_address = ('localhost', 14014)
    udp_socket.bind(local_address)

    api_endpoint = 'http://localhost:5000/api/EasterEgg/'

    try:
        while True:
            data, client_address = udp_socket.recvfrom(1024)
            sale_data = data.decode()

            product_no, amount_sold = parse_sale_data(sale_data)

            update_api(api_endpoint, product_no, amount_sold)

    finally:
        udp_socket.close()

def parse_sale_data(sale_data):
    parts = sale_data.split(', ')
    product_no = int(parts[0].split('=')[1])
    amount_sold = int(parts[1].split('=')[1])
    return product_no, amount_sold

def update_api(api_endpoint, product_no, amount_sold):
    update_data = {"ProductNo": product_no, "AmountSold": amount_sold}
    response = requests.put(api_endpoint + str(product_no), json=update_data)

    if response.status_code == 200:
        print(f"Opdatering vellykket for ProductNo={product_no}, AmountSold={amount_sold}")
    else:
        print(f"Opdatering mislykkedes med statuskode {response.status_code}")

if __name__ == "__main__":
    receive_sale_data()

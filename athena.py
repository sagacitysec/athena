import os
import base64
import requests
import socket
import subprocess
import sys

from platform   import system as system_name  
from subprocess import call   as system_call  
from datetime import datetime

cursor = "-> "

def main():
    print_menu()

def clear_screen():
    command = 'cls' if system_name().lower().startswith('win') else 'clear'

    system_call([command])

def print_watermark():
    print(" ▄▄▄     ▄▄▄█████▓ ██░ ██ ▓█████  ███▄    █  ▄▄▄      ")
    print("▒████▄   ▓  ██▒ ▓▒▓██░ ██▒▓█   ▀  ██ ▀█   █ ▒████▄    ")
    print("▒██  ▀█▄ ▒ ▓██░ ▒░▒██▀▀██░▒███   ▓██  ▀█ ██▒▒██  ▀█▄  ")
    print("░██▄▄▄▄██░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄ ▓██▒  ▐▌██▒░██▄▄▄▄██ ")
    print(" ▓█   ▓██▒ ▒██▒ ░ ░▓█▒░██▓░▒████▒▒██░   ▓██░ ▓█   ▓██▒")
    print(" ▒▒   ▓▒█░ ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░░ ▒░   ▒ ▒  ▒▒   ▓▒█░")
    print("  ▒   ▒▒ ░   ░     ▒ ░▒░ ░ ░ ░  ░░ ░░   ░ ▒░  ▒   ▒▒ ░")
    print("  ░   ▒    ░       ░  ░░ ░   ░      ░   ░ ░   ░   ▒   ")
    print("      ░  ░         ░  ░  ░   ░  ░         ░       ░  ░")
    print("\n")

def print_commands():
    print("- type exit to leave athena.")
    print("- made by sagacitysec \n")
    print("[1] encode base64")
    print("[2] decode base64")
    print("[3] geolocate ip")
    print("[4] portscan ip")
    print("[5] ping ip")
    print("\n")

def print_menu_without_input():
    clear_screen()

    print_watermark()
    print_commands()

def print_menu():
    clear_screen()

    print_watermark()
    print_commands()

    while True:
        option = input(cursor)

        clear_screen()
        print_menu_without_input()

        if option == "1":
            message = input("message to encode: \n" + cursor)
            print_menu_without_input()
            print(b64encode(message))
        elif option == "2":
            message = input("message to decode: \n" + cursor)
            print_menu_without_input()
            print(b64decode(message))
        elif option == "3":
            address = input("ip address to geolocate: \n" + cursor)
            print_menu_without_input()
            print(geolocate(address))
        elif option == "4":
            address = input("ip address to scan: \n" + cursor)
            print_menu_without_input()
            port = input("port to scan: \n" + cursor)
            print_menu_without_input()
            print(portscan(address, port))
        elif option == "5":
            address = input("ip address to ping: \n" + cursor)
            print_menu_without_input()
            print(ping(address))
        elif option == "exit":
            sys.exit()

def b64encode(message):
    message_bytes = message.encode("ascii")
    base64_bytes = base64.b64encode(message_bytes)
    return base64_bytes.decode("ascii")

def b64decode(message):
    base64_bytes = message.encode("ascii")
    message_bytes = base64.b64decode(base64_bytes)
    return message_bytes.decode("ascii")

def geolocate(ip):
    response = requests.get(f'https://ipapi.co/{ip}/json/').json()
    city = response.get("city")
    region = response.get("region")
    country = response.get("country_name")

    location_data = "ip: " + ip + "\ncity: " + city + "\nregion: " + region + "\ncountry: " + country

    return location_data

def portscan(ip, port):
    server_ip = socket.gethostbyname(ip)

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((ip, port))    

        if result == 0:
            return "port " + str(port) + " on " + str(ip) + " is open."
        else:
            return "port " + str(port) + " on " + str(ip) + " is closed."
    except:
        return "port " + str(port) + " on " + str(ip) + " is closed."

def ping(ip):
    win_cmd = "ping -n 3 " + ip
    other_cmd = "ping -c 3 " + ip

    if sys.platform == 'win32':
        ret = subprocess.call(win_cmd, shell=True, stdout=subprocess.DEVNULL)

        if ret == 0:
            return ip + " is online."
        else:
            return ip + " is offline."
    else:
        ret = subprocess.call(other_cmd, shell=True, stdout=subprocess.DEVNULL)

        if ret == 0:
            return ip + " is online."
        else:
            return ip + " is offline."


main()
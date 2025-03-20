#QR CODE Generator
#Enjoy😘

import qrcode
import time
import re
from urllib.parse import urlparse
from termcolor import colored


qr_link = input(colored("Your QR Code link: ", "cyan")).strip()


parsed_url = urlparse(qr_link)
clean_name = parsed_url.netloc if parsed_url.netloc else parsed_url.path 
clean_name = re.sub(r'[^\w\-_.]', '_', clean_name) 


img = qrcode.make(qr_link)
img.save(f"{clean_name}.png")


print(colored("\nGenerating QR Code", "yellow"), end="")
for _ in range(3):
    time.sleep(0.5)
    print(colored(".", "yellow"), end="", flush=True)

time.sleep(0.5)
print(colored(f"\nQR Code generated successfully as '{clean_name}.png' 🎉", "green"))

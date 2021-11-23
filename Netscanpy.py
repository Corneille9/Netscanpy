# Create at 09:27am 10/07/2021
# DESKTOP-CORNEILLE-EUSPFD3
# Author : Corneille Bkle
import os
import socket
import threading

host = {}
ipaddress = ""
ipbytes = socket.gethostbyname(socket.gethostname()).split(".")
for i in range(0, 3):
    ipaddress += ipbytes[i] + "."

userhome = ""
try:
    userhome = os.environ["USERPROFILE"]
except:
    try:
        userhome = os.getenv('USERPROFILE')
    except:
        userhome = os.path.expanduser('~' + os.environ['USERNAME'])


class NetscanThread(threading.Thread):
    def __init__(self, address):
        self.address = address
        threading.Thread.__init__(self)

    def run(self):
        self.lookup(self.address)

    def lookup(self, address):
        global host
        try:
            hostname, alias, _ = socket.gethostbyaddr(address)
            host[address] = hostname
        except socket.herror:
            host[address] = None


# print("Démarage du programme :" + str(now()))
# print("Scan en cours...")

if __name__ == "__main__":
    addresses = []
    mods = []
    for ping in range(1, 254):
        addresses.append(ipaddress + str(ping))

    threads = []

    netscanthreads = [NetscanThread(address) for address in addresses]

    for thread in netscanthreads:
        thread.start()
        threads.append(thread)

    for t in threads:
        t.join()

    file1 = userhome + "\\.netscanpy\\Netscanpy_IP.data"
    file2 = userhome + "\\.netscanpy\\Netscanpy_HostWithIp.data"
    if not os.path.exists(userhome + "\\.netscanpy"):
        os.makedirs(userhome + "\\.netscanpy")

    with open(file1, "w") as fic:
        with open(file2, "w") as file:
            for address, hostname in host.items():
                if (hostname != None):
                    print(address, "=>", hostname)
                    fic.write(address + "\n")
                    file.write(address + "=>" + hostname + "\n")
            file.close()
        fic.close()
# print("Fin du scan")
# print("Fin du programme " + str(now()))

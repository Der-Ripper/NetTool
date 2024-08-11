import subprocess

def linuxMacChanger():
    print('In Linux')
    subprocess.call(f"ifconfig", shell=True)
    interface = input('Interface: ')
    new_mac = input('New MAC-address: ')
    subprocess.call(f"ifconfig {interface} down", shell=True)
    subprocess.call(f"ifconfig {interface} hw ether {new_mac}", shell=True)
    subprocess.call(f"ifconfig {interface} up", shell=True)
    return 0

import subprocess
from Windows.winMacChanger import *

def mac_change(os_version):
    if os_version == 'Windows':
        winMacChanger()
    if os_version == 'Linux':
        print('In Linux')
    if os_version == 'MacOS':
        print('In MacOS')
        
def restart(os_version):
    if os_version == 'Windows':
        subprocess.run('cls', shell=True)
    if os_version == 'Linux':
        subprocess.run('clear', shell=True)
    if os_version == 'MacOS':
        subprocess.run('cls', shell=True)

def toMenu(os_version):
    print('Options')
    print('     [1] Repeat')
    print('     [2] To menu')
    print('     [3] Exit')
    param = input('Option: ')
    if (param == '1'):
        mac_change(os_version)
    elif (param == '2'):
        restart(os_version)
        main()
    elif (param == '3'):
        print('\nGoodbye (´• ω •)\n')
        raise SystemExit(0)
    toMenu(os_version)
        

def main():
    print('Choose optinos')
    print('     [1] Change MAC-address')
    print('     [2] ')
    print('     [3] ')
    print('     [4] ')
    print('     [5] Exit')
    param = input('Option: ')
    os_version = 'Windows'
    if param == '1':
        mac_change(os_version)
    elif param == '5':
        print('\nGoodbye (´• ω •)\n')
        return 0
    else:
        restart(os_version)
        main()
    toMenu(os_version)
        


if __name__ == '__main__':
    main()
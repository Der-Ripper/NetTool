import subprocess
import platform

def winMacChanger():
    print('In Windows')
    res = subprocess.run(['powershell.exe', r'netsh interface show interface'], capture_output=True, text=True, encoding='cp866')
    interfaces = res.stdout
    errors = res.stderr
    print(interfaces, errors)
    if errors:
       return 1 
    else:
        interfaces = interfaces.split('\n')[3:-2]
        print(interfaces)
        names = []
        for i in interfaces:
            i = '      '.join(i.split('      ')[3:])
            print(i)
            names.append(i)
        print(names)


# netsh interface show interface - показ интерфейсов
# ipconfig -all || ipconfig/all  - 1-powershell || 2-cmd 
# Set-NetAdapter -Name "Имя_Интерфейса" -MacAddress "Новый_MAC_Адрес"
#
#
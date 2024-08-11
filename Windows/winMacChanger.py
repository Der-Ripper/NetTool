import subprocess


def winMacChanger():
    print('In Windows')
    #subprocess.run(['powershell.exe', r'Set-NetAdapter -Name "Имя_Интерфейса" -MacAddress "Новый_MAC_Адрес"'])
    #subprocess.run(['powershell.exe', r'netsh interface show interface'])
    interfaces = subprocess.check_output(['powershell.exe', r'netsh interface show interface'])
    print(interfaces)
    #subprocess.check_output(['powershell.exe', r'ipconfig -all'])

    return 0


# netsh interface show interface - показ интерфейсов
# ipconfig -all || ipconfig/all  - 1-powershell || 2-cmd 
#
#
#
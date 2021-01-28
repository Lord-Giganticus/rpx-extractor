import os
import time

if os.getcwd() != os.path.dirname(__file__):
    os.chdir(os.path.dirname(__file__))

def dumpling_extract(x:str): # This is for the dumpling option, x is either "Games", "Updates", or "DLC".
    if x != "Games":
        if x != "Updates":
            if x != "DLC":
                print("Improper usage. Exiting.")
                time.sleep(2)
                exit()
    folders = []
    if os.path.isdir(x) == False:
        print(x,'folder not found. Exiting.')
        time.sleep(2)
        exit()
    os.chdir(x)
    for dir in os.listdir(os.getcwd()):
        if os.path.isdir(dir) == True:
            folders.append(dir)
    print(folders[:])
    folder_choice = str("")
    while folder_choice not in folders:
        folder_choice = input("Enter the name of the folder you want to get the rpx from:\n")
    if folder_choice in folders:
        os.chdir(folder_choice)
        if os.path.isdir('code') == False:
            print("code folder not found. Exiting.")
            time.sleep(2)
            exit()
        os.chdir('code')
        rpx_files_found = int(0)
        rpx_files = []
        for file in os.listdir(os.getcwd()):
            if os.path.isfile(file) == True:
                if file.endswith('.rpx') == True:
                    rpx_files_found += 1
                    rpx_files.append(file)
        if rpx_files_found > 1:
            print("There is more than one rpx file! You'll have to decide which one is correct!")
        move = int(input("Do you want to copy the rpx file?\n[1]Yes\n[2]No\n"))
        if move == 1:
            print(rpx_files[:])
            rpx_file = input("Enter the EXACT name of the rpx file you want to copy:\n")
            folder = input("Enter the directory you want it to be copied to:\n")
            os.system('cmd /c xcopy '+rpx_file+' '+folder)
        else:
            pass
    print("Complete. Exiting.")
    time.sleep(5)
    exit()

choice = int(input("Enter the number corresponding to the format you wish to dump the rpx file.\n[1]WUP\n[2]Loadiine\n[3]FTPiiU_Everywhere\n[4]Dumpling\n"))
if choice == 1:
    from cryptography.fernet import Fernet
    import string
    from ctypes import windll
    if os.path.isfile('key.key') == False:
        os.system('cmd /c curl -L https://github.com/Lord-Giganticus/rpx-extractor/releases/download/core/key.key > key.key')
    file = open('key.key','rb')
    key = file.read()
    file.close()
    os.system('cmd /c curl -L https://github.com/Lord-Giganticus/rpx-extractor/releases/download/core/common_key.txt > common_key.txt')
    enc_message = open('common_key.txt','rb')
    data = enc_message.read()
    enc_message.close()
    f = Fernet(key)
    decrypted = f.decrypt(data)
    decrypted = decrypted.decode()
    os.remove('key.key')
    os.remove('common_key.txt')

    drives = [] # From https://stackoverflow.com/a/827398
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.ascii_uppercase:
        if bitmask & 1:
            drives.append(letter)
        bitmask >>= 1
    
    entry = 0
    entry = int(entry)
    length = len(drives)
    while entry < length:
        try:
            name = str(drives[entry])
            if name.endswith(':') == False:
                name = name+':'
                drives[entry] = name
                try:
                    os.chdir(drives[entry])
                except:
                    print("Drive is bad. Removing from list.")
                    drives.pop(entry)
                    entry -= 1
            entry += 1
        except:
            entry = length +1
    entry = int(0)
    found = int(0)
    while found != 1:
        try:
            os.chdir(drives[entry])
        except IndexError:
            print("No drive found with the install folder. Exiting.")
            time.sleep(2)
            exit()
        if os.path.isdir('install') == False:
            entry += 1
        else:
            found += 1
    if found == 1:
        print('install folder found in drive "'+drives[entry]+'". If this is NOT the correct drive please use Control + C to stop the progam.')
        time.sleep(5)
        os.chdir('install')
        folders = []
        for dir in os.listdir(os.getcwd()):
            if os.path.isdir(dir) == True:
                folders.append(dir)
        print(folders[:])
        folder_choice = input("Enter the name of the folder you want to dump the rpx from:\n")
        if folder_choice in folders:
            os.chdir(folder_choice)
        else:
            print('Incorrect input. Exiting...')
            time.sleep(5)
            exit()
        dec_key = open('keys.txt','w')
        dec_key.write(decrypted)
        dec_key.close()
        os.system('cmd /c curl -L https://github.com/Lord-Giganticus/rpx-extractor/releases/download/core/CDecrypt.exe > CDecrypt.exe')
        os.system('cmd /c curl -L https://github.com/Lord-Giganticus/rpx-extractor/releases/download/core/libeay32.dll > libeay32.dll')
        os.system('cmd /c CDecrypt.exe '+os.getcwd()+' '+os.getcwd()+'\output')
        delete = int(input('Do you wish to delete the WUP files?\n[1]Yes\n[2]No\n'))
        if delete == 1:
            os.remove('title.tmd')
            os.remove('title.tik')
            os.system('cmd /c del /f *.app')
            os.system('cmd /c del /f *.h3')
            os.system('cmd /c del /f *.cert')
            os.system('cmd /c del /f *.tik')
            os.system('cmd /c del /f *.tmd')
        else:
            pass
        os.remove('CDecrypt.exe')
        os.remove('libey32.dll')
        os.remove('keys.txt')
        os.chdir('output')
        os.chdir('code')
        rpx_file = []
        for file in os.listdir(os.getcwd()):
            if os.path.isfile(file) == True:
                if file.endswith('.rpx'):
                    rpx_file.append(file)
        rpx_file = str(rpx_file[0])
        move = int(input("rpx file found it's name is "+rpx_file+'\nWould you like to copy it somewhere?\n[1]Yes\n[2]No\n'))
        if move == 1:
            folder = input('Enter where you want to copy it:\n')
            os.system('cmd /c xcopy '+rpx_file+' '+folder)
            os.chdir('../')
            print("Complete. "+rpx_file+' has been copied to '+folder+'\nExiting.')
            time.sleep(5)
            exit()
        elif move == 2:
            print("Complete. "+rpx_file+' is in '+os.getcwd()+'\nExiting.')
            time.sleep(5)
            os.system('cmd /c start '+os.getcwd())
            exit()
elif choice == 2:
    os.system('cmd /c curl -L https://github.com/Lord-Giganticus/rpx-extractor/releases/download/core/titledumper.exe > titledumper.exe')
    import socket
    ip = socket.gethostbyname(socket.gethostname())
    print('The ip you need to enter on the Wii U side is "'+ip+'".')
    try:
        os.system('titledumper.exe /vol/code '+os.getcwd()+'\output')
    except KeyboardInterrupt:
        pass
    print('Complete. The rpx is in "'+os.getcwd()+'\output". Exiting.')
    os.remove('titledumper.exe')
    time.sleep(5)
    exit()
elif choice == 3:
    try:
        input("WARNING: ONLY USE THIS IF YOU KNOW WHAT YOU ARE DOING THIS CAN CAUSE BRICKS!!\nIf you are sure to move on press enter.\nIf not press control + c")
    except KeyboardInterrupt:
        exit()
    from ftplib import FTP
    ip = input("Input your wii u's ip.\n")
    ftp = FTP(ip)
    output = input("Enter the location where you want to save the rpx file:\n")
    os.chdir(output)
    ftp.login()
    ftp.cwd('storage_mlc')
    ftp.cwd('user')
    ftp.cwd('title')
    version = int('Enter the number corresponding to the game type you want to rip from:\n[1]BASE\n[2]UPDATE\n[3]DLC')
    if version == 1:
        ftp.cwd('00050000')
    elif version == 2:
        ftp.cwd('0005000e')
    elif version == 3:
        ftp.cwd('0005000c')
    titleID = input("Enter the last 8 digits of the game's titleID (you can find this by google searching that one title key site):\n")
    try:
        ftp.cwd(titleID)
    except:
        print("TitleID doesn't exist on MLC! Exiting.")
        time.sleep(5)
        exit()
    ftp.cwd('code')
    files = ftp.nlst()
    for file in files:
        if file.endswith('.rpx'):
            print("Downloading..." + file)
            ftp.retrbinary("RETR " + file ,open(file, 'wb').write)
    print('Complete. Exiting.')
    time.sleep(5)
    exit()
elif choice == 4:
    import string
    from ctypes import windll
    drives = [] # From https://stackoverflow.com/a/827398
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.ascii_uppercase:
        if bitmask & 1:
            drives.append(letter)
        bitmask >>= 1
    
    entry = 0
    entry = int(entry)
    length = len(drives)
    while entry < length:
        try:
            name = str(drives[entry])
            if name.endswith(':') == False:
                name = name+':'
                drives[entry] = name
                try:
                    os.chdir(drives[entry])
                except:
                    print("Drive is bad. Removing from list.")
                    drives.pop(entry)
                    entry -= 1
            entry += 1
        except:
            entry = length +1
    entry = int(0)
    found = int(0)
    while found != 1:
        try:
            os.chdir(drives[entry])
        except IndexError:
            print("No drive found with the dumpling folder. Exiting.")
            time.sleep(2)
            exit()
        if os.path.isdir('dumpling') == False:
            entry += 1
        else:
            found += 1
    if found == 1:
        print('dumpling folder found in drive "'+drives[entry]+'". If this is NOT the correct drive please use Control + C to stop the progam.')
        time.sleep(5)
        os.chdir('dumpling')
        ver = int(input("Enter the number corresponding to the type of game it is:\n[1]BASE\n[2]UPDATE\n[3]DLC\n"))
        if ver == 1:
            choice = str("Games")
            dumpling_extract(choice)
        elif ver == 2:
            choice = str("Updates")
            dumpling_extract(choice)
        elif ver == 3:
            choice = str("DLC")
            dumpling_extract(choice)
        else:
            print("Improper choice. Exiting.")
            time.sleep(2)
            exit()
elif choice < 1 or choice > 4:
    print("Improper choice. Exiting.")
    time.sleep(2)
    exit()
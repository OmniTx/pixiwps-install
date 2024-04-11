import os
print('''\033[1;36;35mPIXIWPS Installer By OmniTx
A ROOT access is REQURED \n''')
os.system("pkg install -y root-repo")
os.system("pkg install -y git tsu python wpa-supplicant pixiewps iw")
os.system("git clone https://github.com/omnitx/pixiwps")

os.system("chmod +x pixiwps/run.py")

print("\033[1;34;36mThanks.\nInstallation Done.\nEnter This Command :\nsudo python pixiwps/run.py -i wlan0 -K")

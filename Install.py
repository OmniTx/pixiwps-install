import os
print('''\033[1;36;40mPIXIWPS Installer By OmniTx
A ROOT access is REQURED \n''')
os.system("pkg install -y root-repo")
os.system("pkg install -y git tsu python wpa-supplicant pixiewps iw")
os.system("cd ..;git clone https://github.com/omnitx/pixiwps")

os.system("cd ..;chmod +x pixiwps/run.py")

print("\033[1;34;40mThanks.\nInstallation Done.\nNow Go To Home Directory[~] And Enter This Command :\nsudo python pixiwps/run.py -i wlan0 -K")

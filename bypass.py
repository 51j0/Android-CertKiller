import sys
from logger import logging

class Bypass:

    def __init__(self,input):
        self.input = input
        self.logger = logging.getLogger('adb')

    def udpateNetworkSecurityConfig(self):
        f=open(self.input+"/AndroidManifest.xml", "r")
        if f.mode != 'r':
            print("Error l100000x.1")
            sys.exit(2)
        contents = f.read()
        if "android:networkSecurityConfig" not in contents:
            contents = contents.replace("<application", "<application android:networkSecurityConfig=\"@xml/networkSecurityConfig\"")
        else:
            result = re.sub('android:networkSecurityConfig="(.*?)"',  'android:networkSecurityConfig="@xml/networkSecurityConfig"',    contents)
            contents = result
        f.close()
        f=open(self.input+"/AndroidManifest.xml", "w+")
        f.write(contents)
        f.close()

        dirName = self.input+"/res/xml"
        if not os.path.exists(dirName):
            os.mkdir(dirName)

        f=open("dependency/networkSecurityConfig.xml", "r")
        contents = f.read()
        f.close()
        f=open("base/res/xml/networkSecurityConfig.xml", "w+")
        f.write(contents)
        f.close()

    def mainfestdebuggable(self):
        f=open(self.input+"/AndroidManifest.xml", "r")
        if f.mode != 'r':
            print("Error l100000x.2")
            sys.exit(2)
        contents = f.read()
        if "android:debuggable" not in contents:
            contents = contents.replace("<application", "<application android:debuggable=\"true\"")
        elif "android:debuggable=\"false\"" in contents:
            contents = contents.replace("android:debuggable=\"false\"", "android:debuggable=\"true\"")
        f.close()
        f=open("base/AndroidManifest.xml", "w+")
        f.write(contents)
        f.close()

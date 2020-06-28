import optparse
from adb import Adb
from apktool import Apktool


# parser = optparse.OptionParser()
# parser.add_option('-i','--install',dest="install",default="help")
# parser.add_option('-d','--decompile',dest="decompile",default="help")
# parser.add_option('-c','--compile', dest="compile")
# parser.add_option('-f','--fetch', dest="fetch")
# parser.add_option('-s','--sign', dest="sign")
# parser.add_option('-h','--help', default="auto")
# options, remainder = parser.parse_args()


val = False

if val:
    #Package name
    adb = Adb("grab")
    print(adb.packagename())

    #Package path
    adb = Adb("grab")
    print(adb.getPackagePath())

    #Input Text
    adb = Adb("grab")
    print(adb.inputext())

    #Fetch APK
    adb = Adb("grab")
    print(adb.fetchApk("alan.apk"))

    #Fetch APK
    adb = Adb("grab")
    print(adb.uninstall())

    #Fetch APK
    adb = Adb("51j0.apk")
    print(adb.install())

    apktool = Apktool("alan.apk")
    print(apktool.decompile())


    apktool = Apktool("alan")
    print(apktool.compile())

    apktool = Apktool("alan/dist/alan.apk")
    print(apktool.sign())

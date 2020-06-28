import optparse
from adb import Adb
from apktool import Apktool
from bypass import Bypass


parser = optparse.OptionParser()
parser.add_option('-i','--install',dest="install",default="none")
parser.add_option('-r','--uninstall',dest="uninstall",default="none")
parser.add_option('-d','--decompile',dest="decompile",default="none")
parser.add_option('-c','--compile', dest="compile",default="none")
parser.add_option('-p','--pull', dest="fetch",default="none")
parser.add_option('-s','--sign', dest="sign",default="none")
parser.add_option('-f','--find', dest="find",default="none")
parser.add_option('-u','--unlock',dest="unlock",action="store",default="none")
#parser.add_option('-h','--help', default="auto")
options, remainder = parser.parse_args()



if options.install != 'none':
    adb = Adb(options.install)
    print(adb.install())
if options.uninstall != 'none':
    adb = Adb(value)
    print(adb.uninstall())
elif options.find != 'none':
    value = options.find
    adb = Adb(value)
    name = adb.packagename()
    path = adb.getPackagePath()
    if(name != ''):
        print("#Package Name:")
        print(name)
        print("\n#Path:")
        print(path)
    else:
        print("Coundnt find any apk matching %s" %s)
elif options.fetch != "none":
    adb = Adb(options.fetch)
    print(adb.fetchApk("%s.apk"%options.fetch))
elif options.unlock != 'none':
    print("Unlocking your phone...")
    adb = Adb(options.unlock)
    print(adb.inputext())
elif options.compile != "none":
    apktool = Apktool(options.compile)
    print(apktool.compile())
    text = input("Would you like to sign the apk (y/N): ")
    if text == 'y' or text == "Y":
        apktool = Apktool("%s/dist/%s.apk"%(options.compile,options.compile))
        print(apktool.sign())
    else:
        sys.exit(2)
elif options.decompile != "none":
    apktool = Apktool(options.decompile)
    print(apktool.decompile())
elif options.sign != "none":
    apktool = Apktool(options.sign)
    print(apktool.sign())
    




else:
    print("Unknown Option")

#print(options)

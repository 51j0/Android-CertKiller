![alt text](https://raw.githubusercontent.com/51j0/Android-CertKiller/master/res/network.png "icon")
## Android-CertKiller
###### v1.0

An automation script to **bypass SSL/Certificate pinning**  in Android


Requirements
- Java 8 (JRE 1.8)
- Python3
- Basic knowledge of Android SDK, AAPT and smali


Currently Supporting

 * Bypassing default CA restrictions in Android Nougat & above [Read more](https://developer.android.com/training/articles/security-config)


Usage
------------------

```bash
git clone https://github.com/51j0/Android-CertKiller.git
cd Android-CertKiller/
python main.py

Options:
  -b  --bypass=sslpinning/debugging/backup/root
  -i  --install           #Install apk
  -d  --decompile         #Decompile APK
  -c  --compile           #Compile and build .apk file
  -s  --sign              #Sign APK
  -f  --Fetch <Package>   #Fetch APK from device           
  -v  --verbose           #Verbose
  -h  --help              #Help
  
Example:
root$ python main.py --bypass=sslpinning --file <>.apk/<folder>/<package>
```

- ###### Install APK

```bash
root$ python main.py --install <>.apk
root$ python main.py -i <>.apk
```

- ###### Compile APK

```bash
root$ python main.py --compile <Folder>
root$ python main.py -c <folder>
```

- ###### Decompile APK

```bash
root$ python main.py --decompile <>.apk
root$ python main.py -d <>.apk
```

- ###### Sign APK

```bash
root$ python main.py --sign <>.apk
root$ python main.py -s <>.apk
```

- ###### Fetch APK from device

```bash
root$ python main.py --fetch <package>
root$ python main.py -f <package>
```




![alt text](https://raw.githubusercontent.com/51j0/Android-Storage-Extractor/master/res/android.png "icon")
<div>Icons made by <a href="https://www.freepik.com/" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" 			    title="Flaticon">www.flaticon.com</a> is licensed by <a href="http://creativecommons.org/licenses/by/3.0/" 			    title="Creative Commons BY 3.0" target="_blank">CC 3.0 BY</a></div>

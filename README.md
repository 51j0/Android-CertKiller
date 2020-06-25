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
  -w  --wizard            #Extract APK from device
  -v  --verbose           #Verbose
  -p  --Path              #APK path
  -h  --help              #Help
  -d  --debugging-mode    #for setting android:debugging flag to true

Example:
root$ python main.py -w #(Wizard mode)
 #or
root$ python main.py -p 'root/Desktop/base.apk' #(Manual mode)

```


```bash
Install the apk
root$ python main.py --install <APK>
```

![alt text](https://raw.githubusercontent.com/51j0/Android-Storage-Extractor/master/res/android.png "icon")
<div>Icons made by <a href="https://www.freepik.com/" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" 			    title="Flaticon">www.flaticon.com</a> is licensed by <a href="http://creativecommons.org/licenses/by/3.0/" 			    title="Creative Commons BY 3.0" target="_blank">CC 3.0 BY</a></div>

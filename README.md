![alt text](https://raw.githubusercontent.com/51j0/Android-CertKiller/master/res/network.png "icon")
## Android-CertKiller
###### v0.1

Script to **bypass** SSL/Certificate Pinning  in Android


Currently Supporting

 * Bypassing default CA Restrictions in  Nougat & Above [Read more](https://developer.android.com/training/articles/security-config)


Usage
------------------

```python
git clone https://github.com/51j0/Android-CertKiller.git
cd Android-CertKiller/

root$ python main.py
------------------
Options:
  -w  --wizard            #Extract APK from device
  -v  --verbose           #Verbose
  -p  --Path              #APK path
  -d  --debuggable-mode   #Setting 'androd:debuggable' flag to true
------------------
Example:
root$ python main.py -w #(Wizard mode)
 #or
root$ python main.py -p 'root/Desktop/base.apk' #(Manual mode)

```


![alt text](https://raw.githubusercontent.com/51j0/Android-Storage-Extractor/master/res/android.png "icon")
<div>Icons made by <a href="https://www.freepik.com/" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" 			    title="Flaticon">www.flaticon.com</a> is licensed by <a href="http://creativecommons.org/licenses/by/3.0/" 			    title="Creative Commons BY 3.0" target="_blank">CC 3.0 BY</a></div>

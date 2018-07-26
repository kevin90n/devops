''' This program is for installing Tomcat and it's dependency Java(If not already installed) '''


###### Importing modules######
import os
import subprocess
import urllib
import tarfile
###### Importing modules######

###### Setting global variables######
java_status=""

###### Setting global variables######


#######Checking if Java is installed##########
try:
  subprocess.call(["java", "-version"])
except:
  java_status="No"
#######Checking if Java is installed##########


#######Downloading and installing Java##########
if(java_status == "No"):
  print("Downloading java")
  os.chdir("/usr/local/src")

  def download(cookie, license, url, filename):
    print(url)
    print(filename)
    opener = urllib2.build_opener()
    opener.addheaders.append((cookie, license))
    f = opener.open(url)
    with open(filename, 'w+') as save:
      save.write(f.read())


  cookie = 'Cookie'
  license = 'oraclelicense=accept-securebackup-cookie'
  url = 'http://download.oracle.com/otn-pub/java/jdk/8u181-b13/96a7b8442fe848ef90c96a2fad6ed6d1/jdk-8u181-linux-x64.tar.gz'
  filename = 'jdk-8u181-linux-x64.tar.gz'

  download(cookie, license, url, filename)

  print("extracting java tar file")
  tar = tarfile.open("/usr/local/src/jdk-8u181-linux-x64.tar.gz")
  tar.extractall()
  tar.close()

  print("Installing Java using alternatives)

  subprocess.call(["/usr/sbin/alternatives", "--install", "/usr/bin/java", "java", "/opt/jdk1.8.0_181/bin/java", "2"])

  print("Installing Tomcat package")
  
  subprocess.call(["yum", "install", "tomcat"])

  print("Starting Tomcat")

  subprocess.call(["systemctl", "start", "tomcat"])

#######Downloading and installing Java##########

else:
  print("Installed already")







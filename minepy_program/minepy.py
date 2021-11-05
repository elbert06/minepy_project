from subprocess import run
import subprocess
import sys
import os
import shutil
import requests
import zipfile
from urllib.request import urlretrieve
# server.properites의 online mode에 대해 true인지 false 인지 체크해주는 변수
onlinemode = True
# upnp가 탑재된 공유기에 portminerplugin이 탑재될지의 변수
Portminer = False
#서버를 열지 말지에 대한 변수
server = False
#기본 다운로드 링크
link = "https://www.googleapis.com/drive/v3/files/FileID?alt=media&key="
#API 코드
link += "AIzaSyAGKUPHxNQm0bR_SUYR1g_iuVx5umVs9EQ"
#JAVA의 환경변수 지정하는것이다.
os.environ['JAVA_HOME'] = "C:/Program Files/Java/jdk-11.0.11"
#JAVA의 path지정중이다(gradle에 필요하다)
os.environ['Path'] = "C:/Program Files/Java/jdk-11.0.11/bin;"+os.environ.get('Path')
# -argument를 받아주는 리스트() 
argu = []
local_file = ""

for m in sys.argv:
    if m.__contains__("py"):
        m = m.replace("\\","")
    m = m.replace("-","")
    argu.append(m)
for h in argu:
    if h == "s":
        server = True
    elif h == "p":
        Portminer = True
    elif h == "n":
        onlinemode = False
    elif h.__contains__(".py") and h != "minepy.py":
        md = h
        break
if not os.path.isdir("C:\Program Files\Java\jdk-11.0.11\lib"):
    print("loading......")
    # local_file의 다운로드 아이디
    remote_url = '1ryrgnjwIFpTEkxkuWl3ipyxIAd8nwspw'
    local_file = 'jdk-11.0.11_windows-x64_bin.exe'
    remote_url = link.replace("FileID",remote_url)
    urlretrieve(remote_url,local_file)
    os.system("jdk-11.0.11_windows-x64_bin.exe /s")
    os.remove("jdk-11.0.11_windows-x64_bin.exe")
if not os.path.isdir("data/gradle"):
    print("loading...")
    # local_file의 다운로드 아이디
    remote_url = '1_EbDfTi58EEaxRy3rr72OQLU1NOK_09O'
    local_file = 'data.zip'
    sys.stdout.write(remote_url)
    remote_url = link.replace("FileID",remote_url)
    urlretrieve(remote_url,local_file)
    os.system("powershell.exe Expand-Archive data.zip")    
    os.remove("data.zip")
os.system("@echo on")
var = subprocess.getoutput("del result.jar")
sys.stdout.write(var)
if str(var).__contains__("없습니다"):
    pass
else:
    os.system("del result.jar")
os.chdir("data")
os.system("gradlew clean build --stacktrace")
os.chdir("build")
os.chdir("libs")
os.system("move data-1.0.0.jar ..")
os.chdir("..")
os.system("move data-1.0.0.jar ..")
os.chdir("..")
os.system("move data-1.0.0.jar ..")
os.chdir("..")
os.system("rename data-1.0.0.jar result.jar")
if server == True:
    if not os.path.isdir("server"):
        os.makedirs("server")
        shutil.copy("data\craftbukkit-1.16.5.jar","server")
    if not os.path.isdir("server/plugins"):
        os.makedirs("server/plugins")
        os.system("move result.jar server/plugins")
    if onlinemode == False:
        # local_file의 다운로드 아이디
        remote_url = '1kTgSv_TJVXd5Kgu9Rt49XXOd5xao2WZ5'
        local_file = 'server.properties'
        remote_url = link.replace("FileID",remote_url)
        urlretrieve(remote_url,local_file)
        var = subprocess.getoutput("ipconfig")
        ipcode = ""
        var = var.split("서브넷 마스크")[0]
        var = var.split("IPv4")[1]
        var = "IPv4"+var
        ip = var.split(":")[1]
        ip = ip.replace(" ","")
        file = open("server.properties","r")
        for k in file.readlines():
            if k.__contains__("server-ip="):
                k = k.replace("\n","")
                k += ip
            else:
                pass
            ipcode += k
        file.close() 
        file = open("server.properties","w")
        file.write(ipcode)
        file.close()
        os.system("move server.properties server")
    if Portminer == True:
        # local_file의 다운로드 아이디
        remote_url = '1qKxgp52_0cX3fIOuWMqXs8_x3tKkUj4i'
        local_file = 'PortMinerPlugin.jar'
        remote_url = link.replace("FileID",remote_url)
        urlretrieve(remote_url,local_file)
        os.system("move PortMinerPlugin.jar server/plugins")
    os.system("move result.jar server/plugins")
    os.chdir("server")
    file = open("eula.txt","w", encoding="UTF8")
    file.write("eula=true")
    file.close()
    os.system("java -jar craftbukkit-1.16.5.jar")
else:
    os.system("exit")
# from google_drive_downloader import GoogleDriveDownloader as gdd
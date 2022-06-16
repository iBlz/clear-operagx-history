import getpass
import os

try:
    import psutil
except ImportError as e:
    os.system("pip install psutil")
    import psutil
    pass

def checkIfProcessRunning(processName): # https://thispointer.com/python-check-if-a-process-is-running-by-name-and-find-its-process-id-pid/
    '''
    Check if there is any running process that contains the given name processName.
    '''
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;

user = getpass.getuser()
print("User : " , user)

if not os.path.exists('C:\\Users\\{}\\AppData\Roaming\\Opera Software\\Opera GX Stable'.format(user)):
    print("Directory not found!")

if checkIfProcessRunning('opera'):
    print("Please close operagx!")
    exit()

os.remove('C:\\Users\\{}\\AppData\Roaming\\Opera Software\\Opera GX Stable\\History'.format(user))

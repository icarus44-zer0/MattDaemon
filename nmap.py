import subprocess

def nmap(args): 
    bashCommand = "nmap 192.168.1.1/24 >> " + str(args)
    process = subprocess.run(bashCommand, shell=True, check=True)
    print(process)
    #output, error = process.communicate()
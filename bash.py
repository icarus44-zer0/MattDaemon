import subprocess
result = subprocess.run(['nmap', '192.168.1.168'], stdout=subprocess.PIPE)
result.stdout
print(result)



# netcat 192.168.1.237 8000 <<END
# HEAD / HTTP/1.1
# Host: 192.168.1.237
# END
# HTTP/1.0 200 OK
# Server: SimpleHTTP/0.6 Python/3.8.5
# Date: Thu, 18 Feb 2021 16:14:23 GMT
# Content-type: text/html; charset=utf-8
# Content-Length: 338


# i = 0
# while (i < 23):
#     netcat(targetAddr,i,content)
#     i+=1

 # commands to hit with bash scripts 
 
 # Active service 
    # systemctl list-units --type=service

    # Net Cat 
    # nc -v -n 8.8.8.8 1-1000




import requests

for i in range(476 + 1):
    n=str(i)
    while(len(n) != 5):
        n = '0'+n
    risposta = requests.get(f"https://virusshare.com/hashfiles/VirusShare_{n}.md5")



with open ("./HashMD5.txt","wb") as f:
    for line in risposta:
        f.write(line)


print("Finito")
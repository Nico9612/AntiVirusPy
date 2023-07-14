import requests


risposta = requests.get("https://virusshare.com/hashfiles/VirusShare_00000.md5")



with open ("./HashMD5.txt","wb") as f:
    for line in risposta:
        f.write(line)


print("Finito")
import os
import hashlib
import requests


def calcola_hash(nomefile):

    with open(nomefile, "rb") as f:
        data = f.read()

    return hashlib.md5(data).hexdigest()

def scan_directory(percorso):

    for cartella, sottocartella, files in os.walk(percorso):

        for file in files:

            file_path = os.path.join(cartella, file)

            file_hash = calcola_hash(file_path)
            containfetti = 0
            for i in range(476 + 1):
                n=str(i)
                while(len(n) != 5):
                    n = '0'+n
            
                risposta = requests.get(f"https://virusshare.com/hashfiles/VirusShare_{n}.md5")
            
                for line in risposta:
                    if file_hash == line:
                        print(f"{file_path} è infetto!")
                        containfetti += 1
            if containfetti == 0:
                print(f"{file_path} è sicuro!")

if __name__=="__main__":
    
  
    
    ok_percorso=False
    
    while not ok_percorso:
        percorso = input("Inserire il percorso del file o della cartella da scannerizzare: ")
        try:
            if os.path.isdir(percorso):
                scan_directory(percorso)
                ok_percorso=True
                break
        except:
            print("Inserire il percorso di una cartella")   
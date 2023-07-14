import os
import hashlib

def calcola_hash(nomefile):

    with open(nomefile, "rb") as f:
        data = f.read()

    return hashlib.md5(data).hexdigest()

def scan_directory(percorso):

    for cartella, sottocartella, files in os.walk(percorso):

        for file in files:

            file_path = os.path.join(cartella, file)

            file_hash = calcola_hash(file_path)
            with open("/home/nicola/Documenti/CORSO_INFORMATICA_2023/Python(Ardizzoni)/AntiVirusPy/HashMD5.txt","rb") as f: 
                for line in f:
                    if file_hash == line:
                        print(f"{file_path} è infetto!")


if __name__=="__main__":
    scan_directory(input("Inserire il percorso del file o della cartella da scannerizzare: "))
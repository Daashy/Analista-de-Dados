import os
import zipfile
import glob
import pandas as pd

# 1. Localização das pastas do projeto
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
RAW_DIR = os.path.join(PROJECT_ROOT, "data", "raw")
INTERIM_DIR = os.path.join(PROJECT_ROOT, "data", "interim")

def extrair_zips():
   # Extrai todos os arquivos .zip de data/raw para data/interim.

   zip_files = glob.glob(os.path.join(RAW_DIR, "*.zip"))

   if not zip_files:
      print ("Nenhum arquivo .zip foi encontrado em data/raw/")
      return
   
   for zip_path in zip_files:
      print (f"Extraindo: {zip_path}")

      with zipfile.ZipFile(zip_path, 'r') as z:
         for file in z.namelist():

            #Apenas CSVs
            if file.lower().endswith(".csv"):
               output_path = os.path.join(INTERIM_DIR, os.path.basename(file))
               print(f"Extraindo arquivo: {file} -> {output_path}")

               z.extract(file, INTERIM_DIR)

               # Move e renomeia se necessário
               old_path = os.path.join(INTERIM_DIR, file)
               if old_path != output_path:
                  os.rename(old_path, output_path)

   print("Extração concluída!")
   
if __name__ == "__main__":
   extrair_zips()


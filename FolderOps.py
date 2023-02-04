import os
import shutil
import Config

def CreateFolder(folder):
  try:
    os.mkdir(folder)
  except:
    # print("Folder \"" + folder + "\" already exists")
    pass
    
def MoveCsvFiles():
  for file in os.listdir(Config.config["downloadDir"]):
    if not Config.config["downloadFilePattern"].upper() in file.upper():
        continue
        
    filePath = os.path.join(Config.config["downloadDir"], file)
    shutil.move(filePath, Config.config["rodentExterminationDir"])
    
def DeleteCsvFiles():
  for file in os.listdir(Config.config["rodentExterminationDir"]):
    if not file.upper() == Config.config["combinedFileName"].upper() and not file.upper() == ".GIT":
      filePath = os.path.join(Config.config["rodentExterminationDir"], file)
      os.remove(filePath)        
import os

def CreateFolder(folder):
  try:
    os.mkdir(folder)
  except:
    # print("Folder \"" + folder + "\" already exists")
    pass
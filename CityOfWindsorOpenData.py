from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
from FolderOps import *
from Grouping import *
#import shutil
import os
import Config

def DownloadCsvFiles(URL):
  CreateFolder(Config.config["rodentExterminationDir"])
   
  driver = webdriver.Firefox()
  driver.get(URL)
  FileListObject = driver.find_element_by_class_name("k-reset")
  FileObjects    = FileListObject.find_elements(By.TAG_NAME,"li")

  # Save the files from the Web URL
  for FileObject in FileObjects:
    link  = "https://opendata.citywindsor.ca/Uploads/" + FileObject.find_element(By.TAG_NAME,"a").text

    #Click on the link to download each file
    clickableLink = FileObject.find_element(By.TAG_NAME,"a")
    clickableLink.click()

  driver.close()
  return

def CombineCSVFiles ():
  ii = 1
  
  # Combine all of the files into RecordList
  RecordList = []
  
  for file in os.listdir(Config.config["rodentExterminationDir"]):
    if not Config.config["downloadFilePattern"].upper() in file.upper():
      continue

    fileName = os.path.join(Config.config["rodentExterminationDir"], file)
    csvReader = csv.reader(open(fileName,'r'))
    
    for row in csvReader:
      if row != None and row!="" and len(row) >= 5:
        block  = row[4]
        street = row[5]
        ward   = row[6]
        if block.rstrip() != "":
          RecordList.append([block, street, ward])     
  return RecordList

def ExportExcelFile(URL):
  DownloadCsvFiles(URL)
  MoveCsvFiles()
  RecordList  = CombineCSVFiles()
  GroupedList = GroupList(RecordList)
  DeleteCsvFiles()
  with open(Config.config["rodentExterminationDir"] + Config.config["combinedFileName"] + ".csv", 'w') as f:
    f.write("Block,Street,Ward,# Calls in past 5 years\n")
  for group in GroupedList:
    with open(Config.config["rodentExterminationDir"] + Config.config["combinedFileName"] + ".csv", 'a') as f:
      f.write(group[0] + ',' + group[1] + ',' + group[2] + ',' + str(group[3]) + "\n")
  
  return RecordList
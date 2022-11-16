from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
from requests import get
from FolderOps import CreateFolder
from Grouping import *


def GetCsvFiles(URL, FolderName):
  CreateFolder(FolderName)
    
  driver = webdriver.Firefox()
  driver.get(URL)
  FileListObject = driver.find_element_by_class_name("k-reset")
  FileObjects    = FileListObject.find_elements(By.TAG_NAME,"li")

  # Save the files from the Web URL
  iNumFiles = 1
  for FileObject in FileObjects:
    link  = "https://opendata.citywindsor.ca/Uploads/" + FileObject.find_element(By.TAG_NAME,"a").text
    response = get(link)
    data     = response.text
    data     = data.replace("\n\n", "")
    with open(FolderName + "\\" + FolderName + str(iNumFiles) + ".csv", 'w') as f:
      f.write(data)

    iNumFiles += 1

  driver.close()
  return iNumFiles

def CombineCSVFiles (NumFiles, FolderName):
  ii = 1
  
  # Combine all of the files into RecordList
  RecordList = []
  for ii in range(1, NumFiles):
    filename = FolderName + "\\" + FolderName + str(ii) + ".csv"
    csvReader = csv.reader(open(filename,'r'))
    
    for row in csvReader:
      if row != None and row!="" and len(row) >= 5:
        block  = row[4]
        street = row[5]
        ward   = row[6]
        if block.rstrip() != "":
          RecordList.append([block, street, ward])     
  return RecordList

def ExportExcelFile(URL, FolderName):
  NumFiles    = GetCsvFiles(URL, FolderName)
  RecordList  = CombineCSVFiles(NumFiles, FolderName)
  GroupedList = GroupList(RecordList)
  with open(FolderName + "\\" + FolderName + ".csv", 'w') as f:
    f.write("Block,Street,Ward,# Calls in past 5 years\n")
  for group in GroupedList:
    with open(FolderName + "\\" + FolderName + ".csv", 'a') as f:
      f.write(group[0] + ',' + group[1] + ',' + group[2] + ',' + str(group[3]) + "\n")
  
  return RecordList
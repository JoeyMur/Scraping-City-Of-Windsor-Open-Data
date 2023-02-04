from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
from requests import get
from FolderOps import CreateFolder

def GroupSortedList(list):
  grCount = 1
  outputList = []
  prev = []
  for elem in list:
    if prev == elem:
      grCount += 1
    else:
      if prev != []:
        outputList.append(prev + [grCount])
      prev = elem
      grCount = 1
  outputList.append(prev + [grCount]) #Last record needs to be added
  return outputList
  
def GroupList(list):
  list.sort()
  GroupedList = GroupSortedList(list)
  GroupedList.sort(key=GetGroupCount, reverse=True)
  return GroupedList
  
def GetGroupCount(listItem):
  return listItem[3]
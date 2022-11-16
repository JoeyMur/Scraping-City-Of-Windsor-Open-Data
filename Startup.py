from FolderOps import CreateFolder
# from Grouping import *
from CityOfWindsorOpenData import *

TotalList = []
TotalList += ExportExcelFile("https://opendata.citywindsor.ca/Opendata/Details/134", "RodentExtermination")

# This is only necessary when you want to combine open data from multiple types into one file
# TotalList = GroupList(TotalList)
# with open("RodentExtermination\\" + "TotalList.csv", 'w') as f:
  # f.write("Block,Street,Ward,# Calls in past 5 years\n")
# for group in TotalList:
  # with open("RodentExtermination\\" + "TotalList.csv", 'a') as f:
    # f.write(group[0] + ',' + group[1] + ',' + group[2] + ',' + str(group[3]) + "\n")
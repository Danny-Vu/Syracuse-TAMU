"""
extracting the raw .seq1 files to excel files for processing
RStudio
"""

library(writexl) #to import a library use command install.packages('___')
library(stringr)
library(readr)

temp = list.files(path = "____",pattern="*.seq1") # a list of the files ending with seq1
#temp is a list of .seq1 files from a certain folder

path="____"
#path is where you want the new data to go

tempnew=c() #empty list for data changes
newname=c() #empty list for data name changes

for (i in 1:length(temp)) { 
  tempfile<-read_delim(paste(path,temp[i],sep = '/'), 
             delim = "\t", escape_double = FALSE, trim_ws = TRUE) 
  tempname <- str_sub(temp[i], end = -6) # enters the list of .seq1 files and removes the .seq1 part
  write_xlsx(tempfile,paste(path,paste(tempname,'.xlsx',sep=''),sep = '/')) 
  #creates an excel file with the new data organization and attached the .xlsx to the end of the name
}

#run for the other folders now to get all of the data in excel files(make sure to organize!)


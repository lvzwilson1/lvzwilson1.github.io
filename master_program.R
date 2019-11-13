rm(list = ls())

library(rmarkdown)  # For rendering documents
library(magrittr)   # For piping commands
library(jsonlite)   # For importing Json
library(dplyr)      # For munging data
library(combinat)   # For combinations of schedules
library(ggplot2)    # For general plotting
library(ggalt)      # For dumbbell plots
library(knitr)      # For tables in documents
library(reticulate) # For running python data download code
library(tidyr)      # Several functions (spread)
library(scales)     # For readusting scale on position plot
library(gdata)      # For object cleanup keep function

# Local Flags 
download.data = 0
thisWeek      = 10

# Locations of sub-routines
pythonDownloadScript = 'C:/Users/lvwilson/Documents/GitHub/lvzwilson1.github.io/data_down_loader.py'
rDataImportScript    = 'C:/Users/lvwilson/Documents/GitHub/lvzwilson1.github.io/data_creation.R'
rMarkdownWeeklyScript= 'C:/Users/lvwilson/Documents/GitHub/lvzwilson1.github.io/weekly_ratings.Rmd'

# download data
if (download.data==1) py_run_file(pythonDownloadScript)

# import data
import.data = 1
if (import.data==1)   source(rDataImportScript, local = TRUE)

# run report for all weeks
for (REPORTNO in thisWeek:1) {
  
  OutFileName = ifelse(REPORTNO==thisWeek, 'index.html', paste0('weekly_report_',REPORTNO,'.html'))
  OutFileDir  = 'C:/Users/lvwilson/Documents/GitHub/lvzwilson1.github.io'
  
  rmarkdown::render(rMarkdownWeeklyScript, output_file=OutFileName, output_dir=OutFileDir)
}

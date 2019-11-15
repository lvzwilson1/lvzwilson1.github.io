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
library(prettydoc)  # For rendering

# Local Flags 
download.data = 0
thisWeek      = 10

# Locations of sub-routines
rDataImportScript    = 'C:/Users/lvwilson/Documents/GitHub/lvzwilson1.github.io/Programs/data_creation.R'
rMarkdownWeeklyScript= 'C:/Users/lvwilson/Documents/GitHub/lvzwilson1.github.io/Programs/weekly_ratings.Rmd'

# download data
if (download.data==1) py_run_file('C:/Users/lvwilson/Documents/GitHub/lvzwilson1.github.io/Programs/data_down_loader.py')

# import data
import.data = 1
if (import.data==1)   source(rDataImportScript, local = TRUE)

# Set up Lists to capture weekly results for overall page
datWeekWins.LIST   <- vector(mode = "list", length = thisWeek)
pyThagStats.LIST   <- vector(mode = "list", length = thisWeek)
merged2.LIST       <- vector(mode = "list", length = thisWeek)
ratingsWhores.LIST <- vector(mode = "list", length = thisWeek)

# run report for all weeks
for (REPORTNO in 10:thisWeek) {
  
  OutFileName = ifelse(REPORTNO==thisWeek, 'index.html', paste0('weekly_report_',REPORTNO,'.html'))
  OutFileDir  = 'C:/Users/lvwilson/Documents/GitHub/lvzwilson1.github.io'
  
  rmarkdown::render(rMarkdownWeeklyScript, output_file=OutFileName, output_dir=OutFileDir)
}

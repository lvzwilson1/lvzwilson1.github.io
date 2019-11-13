rm(list = ls())

library(rmarkdown)
library(magrittr)
library(jsonlite)
library(dplyr)
library(combinat)
library(ggplot2)
library(ggalt)
library(knitr)
library(reticulate)
library(tidyr)
library(scales)
library(gdata)

download.data = 0
if (download.data == 1) py_run_file("C:/Users/lvwilson/Documents/GitHub/lvzwilson1.github.io/data_down_loader.py")

thisWeek = 10

for (REPORTNO in 1:thisWeek) {
  
  OutFileName = ifelse(REPORTNO==thisWeek, 'index.html', paste0('weekly_report_',REPORTNO,'.html'))
  OutFileDir  = ifelse(REPORTNO==thisWeek, 'C:/Users/lvwilson/Documents/GitHub/lvzwilson1.github.io/',
                                           'C:/Users/lvwilson/Documents/GitHub/lvzwilson1.github.io/')
  
  rmarkdown::render('C:/Users/lvwilson/Documents/GitHub/lvzwilson1.github.io/weekly_ratings_v1.Rmd',
                    output_file = OutFileName, 
                    output_dir =  OutFileDir)
}
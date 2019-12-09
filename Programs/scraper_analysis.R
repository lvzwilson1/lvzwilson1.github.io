rm(list = ls())
options(scipen = 999)

library(dplyr)
library(magrittr)
library(jsonlite)
library(tidyr)

dirdir = "C:/Users/lvwilson/Downloads/Fantasy Leagues-20191206T184717Z-001/Fantasy Leagues"
# Combine Datasets
for (i in 0:9) {
  filename = paste0("dataframe_",as.character(i*100000),".csv")
  if (i == 0) {
    aggregated = read.csv(file.path(dirdir,filename), header = TRUE, stringsAsFactors = FALSE)
  }
  else {
    aggregated = rbind(aggregated, read.csv(file.path(dirdir,filename), header = TRUE, stringsAsFactors = FALSE))
  }
  
}

# Select only valid responses
valid_leagues = aggregated %>% filter(statusCode == 200) 

# extract json from valid responses
res <- jsonlite::stream_in(textConnection(valid_leagues$textResponse)) 

# extract team level detail
#purrr::map_chr(teams_expanded$owners, typeof)  %>% table()
teams_expanded  <- res %>% unnest(teams) %>% 
  mutate(nelements = nchar(owners)) %>% 
  group_by(id) %>%
  mutate(minChar = min(nelements)) %>%
  filter(minChar > 12) %>%
  unnest(owners) 

# most common abbreviations follow the most common last names kinda
x <- table(teams_expanded$owners) %>% as.data.frame() %>% arrange(desc(Freq))

# extract member level detail
membs_expanded <- res %>% unnest(members) %>% select(id, id1, displayName, isLeagueManager)

# %>% 
#   group_by(id, id1) %>%
#   mutate(key = row_number()) %>%
#   spread(key, owners)

# most common abbreviations follow the most common last names kinda
x <- table(teams_expanded$abbrev) %>% as.data.frame() %>% arrange(desc(Freq))

df %>% 
  unnest(a) %>% 
  group_by(id) %>% 
  mutate(key = row_number()) %>% 
  spread(key, a)

test <- res2 %>% group_by(id) %>% mutate(nteams = n(), nthTeam = seq_along(id1))

# What is the most common league size?
test2 <- test %>% filter(nthTeam == nteams)
table(test2$nteams)


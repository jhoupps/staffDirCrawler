library(stringr)

setwd("~/Documents/current_quarter_academics/info_300/staffDirScraper/")

jobs <- data.frame(read.csv("position_data.csv"))
salary <- read.csv("AnnualEmployeeSalary2013thru2017.csv")

salary <- salary[salary$AgyCode == 360,] #university of washington
salary$Agency <- NULL
salary$AgyCode <- NULL

clean_names <- c()
for(i in 1:length(salary$Name)){
  name_parts <- strsplit(as.character(salary$Name[i]), ", ")[[1]]
  clean_names[i] = paste(str_trim(name_parts[2]), str_trim(name_parts[1]))
  clean_names[i] = str_to_title(clean_names[i])
}

salary$Name <- clean_names

merged = merge(x = salary, y = jobs, by = "Name", all.x = TRUE)









































































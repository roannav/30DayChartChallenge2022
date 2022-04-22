# load packages
library(ggplot2)
library(RColorBrewer)
library(hrbrthemes)

# Create a data frame.
data <- read.csv("energy.csv")
# print(data)

# print(is.data.frame(data))
print(ncol(data))
print(nrow(data))
print("_________________________________________________________")

# 'Electricity from renewables (TWh)' was renamed to 'Electricity'
# Header: Entity,Code,Year,Electricity
# Units: (TWh)


# Get the data frame's structure
str(data)
print("_________________________________________________________")

print(summary(data))
print("_________________________________________________________")


# Get the max Year from data frame.
max_year <- max(data$Year)
print("max_year is")
print(max_year)

# Grab just specific columns
#result <- data.frame( data$Entity, data$Year, data$Electricity)
#print(result)
#print("_________________________________________________________")

# Grab the first 2 rows
result <- data[1:2,]     # looks similar to Pandas
print("Printing the first 2 rows:")
print(result)
print("_________________________________________________________")

# Grab the 3rd and 5th row, with the 2nd and 4th columns 
result <- data[c(3,5), c(2,4)]     # looks similar to Pandas
print(result)
print("_________________________________________________________")

# Get the country with max electricity 
row <- subset(data, Electricity == max(Electricity))  # returns a row
print(row)
print("_________________________________________________________")

# Header: Entity,Code,Year,Electricity

# 2021 rows
year_2021 <- subset(data, Year == 2021)
print("All rows with year 2021")
print(year_2021)
print("_________________________________________________________")

# Get the countries with max electricity  in 2021
# sort by Electricity
print("All rows with year 2021, sorted by Electricity column")
year_2021[order(year_2021$Electricity), c(1,2,3,4)]

print("_________________________________________________________")

# 2020 rows
year_2020 <- subset(data, Year == 2020)

# Get the countries with max electricity  in 2020
# sort by Electricity
print("All rows with year 2020, sorted by Electricity column")
year_2020[order(year_2020$Electricity), c(1,2,3,4)]


print("_________________________________________________________")

# get all the rows with China
rows_China <- subset( data, Entity == "China")    # return several rows
#print(rows_China)

# get all the rows with "United States" 
rows_US <- subset( data, Entity == "United States")

# get all the rows with China or "United States" 
rows_China_and_US <- subset( data, Entity %in% c("China", "United States"))
#print(rows_China_and_US)


# get all the rows with the top electricity generating countries
top_countries = c("China", "United States", "Brazil", "Canada", "India", "Germany", "Japan", "Russia", "Norway", "United Kingdom", "Spain")
rows_top_countries <- subset( data, Entity %in% top_countries)
print("rows_top_countries")

print("_________________________________________________________")

print(class(data))               # data.frame
print(class(rows_China))         # data.frame
print(length(rows_China$Year))   # 56 years
print("_________________________________________________________")

print("List of the Countries and Other Entities")
#print(unique(data$Entity))

print("_________________________________________________________")


# open a graphics device
# Give the chart file a name
png(file = "day20_new_tool.png") # optional params:  width and height in inches


print("Top countries dataframe")
data1 <- data.frame(rows_top_countries$Year, rows_top_countries$Electricity, rows_top_countries$Entity)

data1[1:2,]     # print first 2 rows.  looks similar to Pandas

print("_________________________________________________________")


Year <- rows_top_countries[["Year"]]
yVal <- rows_top_countries$Electricity
Country <- rows_top_countries$Entity

print(Year)
print("_________________________________________________________")

print(yVal)
print("_________________________________________________________")

print(Country)
print("_________________________________________________________")


#Palette notes:
#   BuGn is hard to see
#   Set1 has 9 colors, but I have 11 diff categories
#   Set3 has 12 colors, but is kinda ugly for this chart
#   Paired has 12 colors


# stacked area chart
plot1 = ggplot(data1, aes(x=Year, y=yVal, fill=Country)) +
    #coord_flip() +  # to flip x and y axis
    geom_area( color="white") + 
    scale_fill_brewer(palette = "Paired") +   
    theme_ipsum(grid="Y") +
    ggtitle("Electricity Generation from Renewables") +

    # Add text to plot
    annotate("text", x = 1970, y = 4500, size=5,
        hjust=0,  # left-align text.   default is center alignment.
        label = "Renewables include hydropower,\nsolar, wind, geothermal,\nbioenergy, wave,\nand tidal.") +
    ylab("Electricity Generation (TWh)")

print(plot1)

# close the graphics device
# Save the file
dev.off()

# World Encyclopedia

import numpy as np
import matplotlib.pyplot as plt

class Country: # Class to define a variable and print the selected country
    """A class used to create a Country object.

        Attributes:
        - country (str): String that represents the country's name

    """
    def __init__(self, country):
        self.country = country 
    def print_all_stats(self):
        """A function that prints the name of the country instance.

            Parameters: None
            Return: None

        """
        print(f"\n-----> Displaying important information of {self.country} <-----\n")
def main(): # Main function of the program 
    Country_Data = np.genfromtxt("Country_Data.csv", delimiter = ",", skip_header = True, dtype = str) # CVS file imported as string, removing comas and headers
    Population_Data = np.genfromtxt("Population_Data.csv", delimiter = ",", skip_header = True, dtype = str) # CVS file imported as string, removing comas and headers
    Threatened_Species = np.genfromtxt("Threatened_Species.csv", delimiter = ",", skip_header = True, dtype = str) # CVS file imported as string, removing comas and headers
    Country_Data_Integers = np.genfromtxt("Country_Data.csv", delimiter = ",", skip_header = True, dtype = int) # CVS file imported as integer, removing comas and headers
    Population_Data_Integers = np.genfromtxt("Population_Data.csv", delimiter = ",", skip_header = True, dtype = int) # CVS file imported as integer, removing comas and headers
    Threatened_Species_Integers = np.genfromtxt("Threatened_Species.csv", delimiter = ",", skip_header = True, dtype = int) # CVS file imported as integer, removing comas and headers
    Country_List =[] # List of the countries in the world
    for x in Population_Data: # For loop to create the list of countries
        Country_List.append(x[0])
    while True: # Main loop of the program / menu of the program
        print("\n--------------------------------------------------\n \n--------------> World Encyclopedia <--------------\n")
        print("1 -----> Introduction to the program")
        print("2 -----> Country Data")
        print("3 -----> Population Data")
        print("4 -----> Threatened Species")
        print("5 -----> To enter a country to know more about it")
        print("0 -----> Exit")
        print("--------------------------------------------------\n")
        user_input = input("Select -----> ") # User input in the menu to run the selection
        if user_input == "0": # If statement for the exit
            print("\n-------------------------------------------------------------")
            print("\n-----> Thanks for using the World Encyclopedia Program <-----\n")
            print("-------------------------------------------------------------")
            break # Break statement for the main loop of the program (exit of the program)
        elif user_input == "1": # If statement for the introduction to the program
            print("\n-----> Introduction to the Program <-----\n")
            print("* This program shows information about each country over the world.\n* Important aspects such as population, threteaned species and country (region, sub-region and size).\n* Specific data for a country of your choice.\n \n")
        elif user_input == "2": # If statement for country data
            Total_Size = Country_Data_Integers[:,3].sum() # Variable for the sum of the territory of all countries
            print("\n-----> Country Data <-----\n")
            print(f"- The total combined area territory of America, Europe, Asia and Oceania is {Total_Size:.2f} square kilometers.\n \n") # Printing statement with format with the variable in it
        elif user_input == "3": # If statement for the population data
            Total_Population_2020 = Population_Data_Integers[:,21].sum() # Variable for the sum of the population of all countries in an specific column
            Total_Population_2000 = Population_Data_Integers[:,1].sum() # Variable for the sum of the population of all countries in an specific column
            Total_Population = (Total_Population_2020 - Total_Population_2000) # Variable for the difference between the population of all countries in two specific columns
            Mean_Population = Population_Data_Integers[:,21].mean() # Variable for the average of the population of all countries in an specific column
            Max_Population = Population_Data_Integers [:,21].max() # Variable for the sum of threatened species of all countries in a specific column
            Min_Population = Population_Data_Integers[:,21].min() # Variable for the smallest population of all countries
            Region_Population = (Population_Data_Integers[:,21].sum())/5 # Variable for divison between the total population of all countries in an specific column and 5 which represents the regions
            print("\n-----> Population Data <-----\n")
            print(f"- The total population in the world in 2020 was {Total_Population_2020:.0f} people.\n") # Printing statement with format with the variable in it
            print(f"- The change in the world population from 2000 to 2020 is {Total_Population:.0f} people.\n") # Printing statement with format with the variable in it
            print(f"- The total mean population in the world is approximately {Mean_Population:.0f} people.\n") # Printing statement with format with the variable in it
            print(f"- The mean population per region of the world is approximately {Region_Population:.0f} people.\n") # Printing statement with format with the variable in it
            print(f"- The country with the largest population in the world has {Max_Population:.0f} people.\n") # Printing statement with format with the variable in it
            print(f"- The country with the smallest population in the world has {Min_Population:.0f} people.\n \n") # Printing statement with format with the variable in it
            Population_2000 = Population_Data_Integers[:,1].sum() # Variable for the sum of the population of all countries in a specific column
            Population_2001 = Population_Data_Integers[:,2].sum() # Variable for the sum of the population of all countries in a specific column
            Population_2002 = Population_Data_Integers[:,3].sum() # Variable for the sum of the population of all countries in a specific column
            Population_2003 = Population_Data_Integers[:,4].sum() # Variable for the sum of the population of all countries in a specific column
            Population_2004 = Population_Data_Integers[:,5].sum() # Variable for the sum of the population of all countries in a specific column
            Population_2005 = Population_Data_Integers[:,6].sum() # Variable for the sum of the population of all countries in a specific column
            Population_2006 = Population_Data_Integers[:,7].sum() # Variable for the sum of the population of all countries in a specific column
            Population_2007 = Population_Data_Integers[:,8].sum() # Variable for the sum of the population of all countries in a specific column
            Population_2008 = Population_Data_Integers[:,9].sum() # Variable for the sum of the population of all countries in a specific column
            Population_2009 = Population_Data_Integers[:,10].sum() # Variable for the sum of the population of all countries in a specific column
            Population_2010 = Population_Data_Integers[:,11].sum() # Variable for the sum of the population of all countries in a specific column
            Population_2011 = Population_Data_Integers[:,12].sum() # Variable for the sum of the population of all countries in a specific column
            Population_2012 = Population_Data_Integers[:,13].sum() # Variable for the sum of the population of all countries in a specific column
            Population_2013 = Population_Data_Integers[:,14].sum() # Variable for the sum of the population of all countries in a specific column
            Population_2014 = Population_Data_Integers[:,15].sum() # Variable for the sum of the population of all countries in a specific column
            Population_2015 = Population_Data_Integers[:,16].sum() # Variable for the sum of the population of all countries in a specific column
            Population_2016 = Population_Data_Integers[:,17].sum() # Variable for the sum of the population of all countries in a specific column
            Population_2017 = Population_Data_Integers[:,18].sum() # Variable for the sum of the population of all countries in a specific column
            Population_2018 = Population_Data_Integers[:,19].sum() # Variable for the sum of the population of all countries in a specific column
            Population_2019 = Population_Data_Integers[:,20].sum() # Variable for the sum of the population of all countries in a specific column
            Population_2020 = Population_Data_Integers[:,21].sum() # Variable for the sum of the population of all countries in a specific column
            plt.plot([2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020],[Population_2000, Population_2001, Population_2002, Population_2003, Population_2004, Population_2005, Population_2006, Population_2007, Population_2008, Population_2009, Population_2010, Population_2011, Population_2012, Population_2013, Population_2014, Population_2015, Population_2016, Population_2017, Population_2018, Population_2019, Population_2020], label = "Population during the years", color = "brown", linestyle = "-", linewidth = 2) # Statement to set up the plot with the x and y axis values, color, linestyle and linewidth 
            plt.title("World Population 2000 - 2020") # Title of tle plot
            plt.legend(shadow = True, loc = "upper left") # Statement to set up the label of the plot
            plt.xlabel("Years") # Title of the x axis
            plt.ylabel("Population In Billions") # Title of the y axis
            plt.xticks(np.arange(2000, 2021, step = 1)) # Satetement to set up the distance between the x values 
            plt.grid() # Statement to put a grid in the plot
            plt.show() # Statement to show the plot
        elif user_input == "4": # If statement for the threatened species data
            print("\n-----> Threatened Species <-----\n")
            Total_Threatened_Plants = Threatened_Species_Integers[:,1].sum() # Variable for the sum of threatened species of all countries in a specific column
            Total_Threatened_Birds = Threatened_Species_Integers[:,3].sum() # Variable for the sum of threatened species of all countries in a specific column
            Total_Threatened_Mammals = Threatened_Species_Integers[:,4].sum() # Variable for the sum of threatened species of all countries in a specific column
            Total_Threatened_Fish =Threatened_Species_Integers[:,2].sum() # Variable for the sum of threatened species of all countries in a specific column
            Max_Threatened_Plants = Threatened_Species_Integers[:,1].max() # Variable for the largest number of threatened species of all countries in a specific column
            Max_Threatened_Fish = Threatened_Species_Integers[:,2].max() # Variable for the largest number of threatened species of all countries in a specific column
            Max_Threatened_Birds = Threatened_Species_Integers[:,3].max() # Variable for the largest number of threatened species of all countries in a specific column
            Max_Threatened_Mammals = Threatened_Species_Integers[:,4].max() # Variable for the largest number of threatened species of all countries in a specific column
            print("- There are {0} total threatened plant species in the world and the country with the most threatened plant species has {1} species.\n".format(Total_Threatened_Plants, Max_Threatened_Plants)) # Printing statement with format with the variable in it
            print("- There are {0} total threatened fish species in the world and the country with the most threatened fish species has {1} species.\n".format(Total_Threatened_Fish, Max_Threatened_Fish)) # Printing statement with format with the variable in it
            print("- There are {0} total threatened bird species in the world and the country with the most threatened bird species has {1} species.\n".format(Total_Threatened_Birds, Max_Threatened_Birds)) # Printing statement with format with the variable in it
            print("- There are {0} total threatened mammal species in the world and the country with the most threatened mammal species has {1} species.\n \n".format(Total_Threatened_Mammals, Max_Threatened_Mammals)) # Printing statement with format with the variable in it
            Threatened_Plants = "Plants"
            Threatened_Fish = "Fish"
            Threatened_Birds = "Birds"
            Threatened_Mammals = "Mammals"
            plt.bar([Threatened_Plants, Threatened_Fish, Threatened_Birds, Threatened_Mammals], [Total_Threatened_Plants, Total_Threatened_Fish, Total_Threatened_Birds, Total_Threatened_Mammals], color = "cyan", width = 0.6) # Statement to set up the bar plot with the x axis names and y axis values, color and width 
            plt.title("Threatened World Species") # Bar plot title
            plt.xlabel("Species") # Title of the x axis
            plt.ylabel("Number of Threatened Species") # Title of the y axis
            plt.grid(axis = "y") # Statement to put a grid in the y axis of the plot
            plt.show() # Statement to show the plot
            Species = ["Plants", "Fish", "Birds", "Mammals"] # List of the headers 
            plt.pie([Total_Threatened_Plants, Total_Threatened_Fish, Total_Threatened_Birds, Total_Threatened_Mammals], labels = Species, autopct='%1.2f%%', startangle = 90) # Statement to set up the pie plot with the x values, labels, percentages and starting angle
            plt.title(f"% Of Threatened Species In The World") # Title of the pie plot
            plt.show() # Statement to show the plot
        elif user_input == "5": # If statement to selecet an specific country
            while True: # While loop for the if statement
                print("\n--------------------------------------------------\n")
                Country_Input = input("Enter country -----> ") # Variable for the country entered
                if Country_Input not in Country_List: # If statement for everythng except countries
                    print(" \n--------------------------------------------------\n \nInvalid input.\nYou must enter a country starting with capital letter.")
                elif Country_Input in Country_List: # If statement for just countries
                    Value_1 = Country(Country_Input) # Statement to save a variable in the class
                    Value_1.print_all_stats() # Statement to call the class
                    Country_Variable = Country_List.index(Country_Input) # Statement to save the selected country index in a variable
                    population_difference = (Population_Data_Integers[Country_Variable][21] - Population_Data_Integers[Country_Variable][1]) # Variable for the difference between the population of an specific country in 2000 and the population of an specific country in 2020
                    print("- The population of {0} in 2020 was {1} people.\n".format(Country_Input, Population_Data[Country_Variable][21])) # Print statement with format with two variables in it 
                    print("- The change in population from 2000 to 2020 in {0} is {1} people.\n".format(Country_Variable, population_difference)) # Print statement with format with two variables in it
                    print("- {0} is located in the region of {1} and the sub-region of {2}.\n".format(Country_Input, Country_Data[Country_Variable][1], Country_Data[Country_Variable][2])) # Print statement with format with three variables in it
                    print("- {0} has a size of {1} square kilometers.\n".format(Country_Input, Country_Data[Country_Variable][3])) # Print statement with format with two variables in it
                    print("- {0} has {1} threatened plant species, {2} threatened fish species, {3} threatened bird species and {4} threatened mammal species.\n \n".format(Country_Input, Threatened_Species[Country_Variable][1], Threatened_Species[Country_Variable][2], Threatened_Species[Country_Variable][3], Threatened_Species[Country_Variable][4])) # Print statement with format with five variables in it
                    Country_Population_2000 = Population_Data_Integers[Country_Variable][1] # Variable for the population in a specific country in a specific column
                    Country_Population_2001 = Population_Data_Integers[Country_Variable][2] # Variable for the population in a specific country in a specific column
                    Country_Population_2002 = Population_Data_Integers[Country_Variable][3] # Variable for the population in a specific country in a specific column
                    Country_Population_2003 = Population_Data_Integers[Country_Variable][4] # Variable for the population in a specific country in a specific column
                    Country_Population_2004 = Population_Data_Integers[Country_Variable][5] # Variable for the population in a specific country in a specific column
                    Country_Population_2005 = Population_Data_Integers[Country_Variable][6] # Variable for the population in a specific country in a specific column
                    Country_Population_2006 = Population_Data_Integers[Country_Variable][7] # Variable for the population in a specific country in a specific column
                    Country_Population_2007 = Population_Data_Integers[Country_Variable][8] # Variable for the population in a specific country in a specific column
                    Country_Population_2008 = Population_Data_Integers[Country_Variable][9] # Variable for the population in a specific country in a specific column
                    Country_Population_2009 = Population_Data_Integers[Country_Variable][10] # Variable for the population in a specific country in a specific column
                    Country_Population_2010 = Population_Data_Integers[Country_Variable][11] # Variable for the population in a specific country in a specific column
                    Country_Population_2011 = Population_Data_Integers[Country_Variable][12] # Variable for the population in a specific country in a specific column
                    Country_Population_2012 = Population_Data_Integers[Country_Variable][13] # Variable for the population in a specific country in a specific column
                    Country_Population_2013 = Population_Data_Integers[Country_Variable][14] # Variable for the population in a specific country in a specific column
                    Country_Population_2014 = Population_Data_Integers[Country_Variable][15] # Variable for the population in a specific country in a specific column
                    Country_Population_2015 = Population_Data_Integers[Country_Variable][16] # Variable for the population in a specific country in a specific column
                    Country_Population_2016 = Population_Data_Integers[Country_Variable][17] # Variable for the population in a specific country in a specific column
                    Country_Population_2017 = Population_Data_Integers[Country_Variable][18] # Variable for the population in a specific country in a specific column
                    Country_Population_2018 = Population_Data_Integers[Country_Variable][19] # Variable for the population in a specific country in a specific column
                    Country_Population_2019 = Population_Data_Integers[Country_Variable][20] # Variable for the population in a specific country in a specific column
                    Country_Population_2020 = Population_Data_Integers[Country_Variable][21] # Variable for the population in a specific country in a specific column
                    plt.plot([2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020],[Country_Population_2000, Country_Population_2001, Country_Population_2002, Country_Population_2003, Country_Population_2004, Country_Population_2005, Country_Population_2006, Country_Population_2007, Country_Population_2008, Country_Population_2009, Country_Population_2010, Country_Population_2011, Country_Population_2012, Country_Population_2013, Country_Population_2014, Country_Population_2015, Country_Population_2016, Country_Population_2017, Country_Population_2018, Country_Population_2019, Country_Population_2020], label = "Population during the years", color = "magenta", linestyle = "-", linewidth = 2) # Statement to set up the plot with the x and y axis values, color, linestyle and linewidth 
                    plt.title(f"Population Of {Country_Input} 2000 - 2020") # Title of the plot
                    plt.legend(shadow = True, loc = "upper left") # Statement to set up the label of the plot
                    plt.xlabel("Years") # Title of the x axis
                    plt.ylabel("Population") # Title of the y axis
                    plt.xticks(np.arange(2000, 2021, step = 1)) # Satetement to set up the distance between the x values
                    plt.grid() # Statement to put a grid in the plot
                    plt.show() # Statement to show the plot
                    Total_Threatened_Plants = Threatened_Species_Integers[Country_Variable][1] # Variable for the threatened plants in a specific country
                    Total_Threatened_Birds = Threatened_Species_Integers[Country_Variable][3] # Variable for the threatened birds in a specific country
                    Total_Threatened_Mammals = Threatened_Species_Integers[Country_Variable][4] # Variable for the threatened mammals in a specific country
                    Total_Threatened_Fish =Threatened_Species_Integers[Country_Variable][2] # Variable for the threatened fish in a specific country
                    Species = ["Plants", "Fish", "Birds", "Mammals"] # List of the headers 
                    plt.pie([Total_Threatened_Plants, Total_Threatened_Fish, Total_Threatened_Birds, Total_Threatened_Mammals], labels = Species, autopct='%1.2f%%', startangle = 90) # Statement to set up the pie plot with the x values, labels, percentages and starting angle
                    plt.title(f"% Of Threatened Species In {Country_Input}") # Title of the pie plot 
                    plt.show() # Statement to show the pie plot
                    Total_Size = Country_Data_Integers[:,3].sum() # Variable for the sum territory of all countries
                    Country_Size = Country_Data_Integers[Country_Variable][3] # Variable for the threatened species in a specific country in a specific column
                    Total_Total = (Total_Size - Country_Size) # Difference betweet the total territory and the the country territory
                    Names = ["Rest Of The World", Country_Input] # List of the pie plot labels
                    plt.pie([Total_Total, Country_Size], labels = Names, autopct='%1.2f%%', startangle = 90) # Statement to set up the pie plot with the x values, labels, percentages and starting angle
                    plt.title(f"Territory Of {Country_Input} With Respect To The World") # Title of the pie plot
                    plt.show() # Statemet to show the pie plot
                    break # Break loop for the if country selection statement
        else: # Else statement for anything that is not in the countries list
            print("\nYou must enter a valid input.\n \n")
if __name__ == '__main__': # If statement of the main fuinction
    main() # Call the main function 


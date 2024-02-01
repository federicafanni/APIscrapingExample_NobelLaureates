import requests
import json #for scraping through the API
import pygal #for data visualization

print("NOBEL LAUREATES: EXTRACTION OF LAUREATES' NAMES AND COUNTRY OF ORIGIN")

url = "https://api.nobelprize.org/2.1/laureates"
data = requests.get(url)  # Getting the page
parsed_data = data.json()  # Parsing the data into json

laureates = parsed_data["laureates"] # Getting the info within the "laureates" element
numberofLaureates = len(laureates) #Getting how many laureates are in the list
print("Laureates: ", numberofLaureates) 

countriesList = [] #Creating the list of country names for the data visualization
countriesOccurrences = [] #Creating the list of country occurrences for the data visualization
for person in laureates: #For each laureate within the group of laureates:
    fullName = person["fullName"] #store the laureate's name values into the fullName variable
    print(fullName.get("en")) #print the English name/value of the laureate
    birthplace = person["birth"] #I created this variable to access the dictionary called "birth",
                                # which will allow to access the "place" dictionary and then extract the English value for the "country" key.
    try:
        laureatePlace = birthplace["place"] #Accessing the "place" dictionary
        country = laureatePlace["countryNow"]#Accessing the "countryNow" dictionary
        country = country.get("en") #Getting the value of the "en" key and storing it into the country variable
    except KeyError: #If there's a key error
        country = "country_unknown" #then assign "country_unknown" as the value of the country variable

    print(country, "\n--------") #Printing the country name the laureate is from and adding a line break
    countriesList.append(country)#Appending that country name to the list of countries (countriesList)

#The lines below create a variable for each country, which stores the times a country name appears
occurrencesCountryUSA = countriesList.count("USA")
occurrencesCountryDenmark = countriesList.count("Denmark")
occurrencesCountryIsrael = countriesList.count("Israel")
occurrencesCountryLithuania = countriesList.count("Lithuania")
occurrencesCountrycountry_unknown = countriesList.count("country_unknown")
occurrencesCountryPakistan = countriesList.count("Pakistan")
occurrencesCountryIndia = countriesList.count("India")
occurrencesCountryEthiopia = countriesList.count("Ethiopia")
occurrencesCountryGermany = countriesList.count("Germany")
occurrencesCountryArgentina = countriesList.count("Argentina")
occurrencesCountryEgypt = countriesList.count("Egypt")
occurrencesCountryJapan = countriesList.count("Japan")
occurrencesCountryFrance = countriesList.count("France")
occurrencesCountryUK = countriesList.count("United Kingdom")
occurrencesCountryNewZealand = countriesList.count("New Zealand")
occurrencesCountryPoland = countriesList.count("Poland")
occurrencesCountryAlgeria = countriesList.count("Algeria")
occurrencesCountryBelgium = countriesList.count("Belgium")

#The lines below append the occurrence variable just created to the countriesOccurrences list
countriesOccurrences.append(occurrencesCountryAlgeria)
countriesOccurrences.append(occurrencesCountryArgentina)
countriesOccurrences.append(occurrencesCountryBelgium)
countriesOccurrences.append(occurrencesCountryDenmark)
countriesOccurrences.append(occurrencesCountryEgypt)
countriesOccurrences.append(occurrencesCountryEthiopia)
countriesOccurrences.append(occurrencesCountryFrance)
countriesOccurrences.append(occurrencesCountryGermany)
countriesOccurrences.append(occurrencesCountryIndia)
countriesOccurrences.append(occurrencesCountryIsrael)
countriesOccurrences.append(occurrencesCountryJapan)
countriesOccurrences.append(occurrencesCountryLithuania)
countriesOccurrences.append(occurrencesCountryNewZealand)
countriesOccurrences.append(occurrencesCountryPakistan)
countriesOccurrences.append(occurrencesCountryPoland)
countriesOccurrences.append(occurrencesCountryUSA)
countriesOccurrences.append(occurrencesCountrycountry_unknown)
countriesOccurrences.append(occurrencesCountryUK)

bar_chart = pygal.Bar()#Creating a bar chart
bar_chart.title = "Number of Nobel laureates per country"

uniqueCountriesSet= set(countriesList) #Converting to set to have one instance per country
uniqueCountriesList = list(uniqueCountriesSet)#Converting back to list to use for the data visualization,
                                              #but the order of the countries changes every time due to the set creation, 
                                              #hence doesn't match the order of the occurrences in the other list, so it needs sorting
                            
uniqueCountriesListSorted = sorted(uniqueCountriesList)#Sorting the countries by name

def mergeLists(list1, list2): #This function creates tuples getting the items from two lists.
    newList = [(list1[i], list2[i]) for i in range(0, len(list1))] 
    return newList

countryNumberPrizesList = mergeLists(uniqueCountriesListSorted, countriesOccurrences) #Calling the function to create tuples (country name andcountry occurrence)
for country, numberOfPrizes in countryNumberPrizesList:
    bar_chart.add(country, numberOfPrizes)#Adding the tuples to the bar chat

bar_chart.render_to_file("Laureates_chart.svg")#Rendering the bar chart in svg format

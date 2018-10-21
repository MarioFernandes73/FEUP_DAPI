import pandas as pd
from datetime import datetime

countries_with_space = ["Hong Kong",  "South Korea", "New Zealand", "South Africa", "Ivory Coast" , "Burkina Faso", "Czech Republic", "Chad France", "Puerto Rico",
"West Germany", "Sri Lanka","Costa Rica","Dominican Republic", "Serbia and Montenegro", "United Arab Emirates", "Congo (Brazzaville)","Saudi Arabia","Georgia (Republic)",
"North Korea (Korean People's Democratic Republic)","Arab Emirates"]

flags = ["Questionable for Children", "Suitable for Teens", "Violence", "Adult Situations" , 
"Humor", "Adult","Profanity", "Scary Moments", "Nudity", "Sexual Situations",
"Drug Content", "Strong Sexual Content", "Sci-Fi", "Gore", "Brief", "Not For Children",
"War", "Language", "Mild", "Smoking", "Substance Abuse", "Alcohol Consumption",
"Suitable for Children", "Children in Peril", "Graphic", "Situations", "Slapstick",
"Torture", "Youth Substance Use", "Rape & Sexual Abuse", "Western", "Excellent For Children",
"Watch With Your Teen", "Scatological", "Strong Content", "Rape & Abuse", "Watch With Your Kids",
"Child Classic"]

attributes =["High Production Values", "High Artistic Quality", "High Budget", "Low Artistic Quality",
"Low Budget", "Cult Film", "High Historical Importance", "Sleeper", "Low Production Values"]

def splitarrays(column_name, separator):
    path = base_path + column_name + ".csv"
    out = open(path,"w+",encoding="utf-8")

    out.write(column_name)

    for i in range(0, len(df[column_name])):
        record = df[column_name][i]
        
        if ("nan" in str(record)):
            out.write("\nunknown")
        elif separator in record:
            if(separator == " "):
                '''
                # check for countries with spaces
                for j in range(0,len(countries_with_space)):
                    #found
                    if(countries_with_space[j] in record):
                        print("found: " + countries_with_space[j])
                        out.write("\n" + countries_with_space[j])
                        print("before: " + record)
                        record = record.replace(" " + countries_with_space[j],'')
                        record = record.replace(countries_with_space[j] + " ",'')
                        record = record.replace(countries_with_space[j],'')
                        print("after: " + record)
                
                # check for flags with spaces
                for j in range(0,len(flags)):
                    #found
                    if(flags[j] in record):
                        #print("found: " + flags[j])
                        out.write("\n" + flags[j])
                        #print("before: " + record)
                        record = record.replace(" " + flags[j],'')
                        record = record.replace(flags[j] + " ",'')
                        record = record.replace(flags[j],'')
                        #print("after: " + record)

                # check for attributes with spaces
                for j in range(0,len(attributes)):
                    #found
                    if(attributes[j] in record):
                        #print("found: " + flags[j])
                        out.write("\n" + attributes[j])
                        #print("before: " + record)
                        record = record.replace(" " + attributes[j],'')
                        record = record.replace(attributes[j] + " ",'')
                        record = record.replace(attributes[j],'')
                        #print("after: " + record)
                '''
            if(record != ""):
                print(record)

            if separator in record:
                parts = record.split(separator)
                for k in range(0,len(parts)):
                    if(parts[k] != " "):
                        out.write("\n" + parts[k])
        else:
            out.write("\n" + record)
        

    out.close()   

base_path = "C:\\Users\\Catarina Ramos\\Documents\\FEUP\\DAPI\\"
path_data = base_path + "all_movies_without_missing_values_release_date.csv"

df = pd.read_csv(path_data, sep=";", skiprows= 1, header=None,encoding="ISO-8859-1", names=["title","genres","subGenres","releaseDate","duration","countries","mpaaRating","allmovieRating","flags","directedBy","producedBy","releasedBy","moods","themes","keywords","attributes","synopsis","actors","relatedMovies"])

columns_arrays_bar = ["genres","subGenres","themes","actors","relatedMovies","moods"]
columns_arrays_space = ["countries", "keywords", "flags","attributes"]
columns_arrays_bar2 = ["directedBy","releasedBy"]

splitarrays(columns_arrays_bar2[1]," ")
'''
for column in columns_arrays_bar:
    splitarrays(column," | ")

for column in columns_arrays_space:
    splitarrays(column," ")
'''

import json
import os
import matplotlib.pyplot as plt


fname = "sorted_output.json"

#sentence splicing function for titles
def break_sen (year_of_interest):
    list_of_commons = ['a','of','the','and','with','for','in','from','The','A','by','on','to','at']
    for subject in year_of_interest:
        break_sentence = subject.split()
        for word in break_sentence:
            if word not in list_of_commons:
                list_of_words.append(word)
    return list_of_words

#opening JSON file (takes a while)
print("Please wait while data is being loaded...")
str_data = open(fname).read()
json_data = json.loads(str_data)
print("Data is loaded")

#searchable fields
list_options = [
"accessionYear"
,"isPublicDomain"
,"department"
,"objectName"
,"title"
,"culture"
,"period"
,"dynasty"
,"reign"
,"artistDisplayName"
,"artistNationality"
,"artistBeginDate"
,"artistEndDate"
,"artistGender"
,"medium"
,"dimensions"
,"creditLine"
,"city"
,"state"
,"county"
,"country"
,"region"
,"subregion"
,"locale"
,"locus"
,"excavation"
,"river"
,"classification"
]

#user friendly names for searchable fields
list_user_option=[
"accession year"
,"is public domain"
,"department"
,"object name"
,"subject"
,"culture"
,"period"
,"dynasty"
,"reign"
,"artist name"
,"artist nationality"
,"artist birth date"
,"artist death date"
,"artist gender"
,"medium"
,"dimensions"
,"credit line"
,"city"
,"state"
,"county"
,"country"
,"region"
,"subregion"
,"locale"
,"precise location"
,"excavation"
,"river"
,"classification"]


for i in range(20):
    u_input = input("Enter a year: ") 
    u_input_year = int(u_input)
    print("List of Options:")
    i = 1
    #adding a number to represent each field, plus aligning numbers for aesthetics
    for opt in list_user_option:
        if i < 10:
            print(str(i)+".  " +opt)
        else:
            print(str(i)+". " +opt)
        i += 1
    #user chooses number corresponding to the field they are interested in 
    u_interest = input("Selected Number: ")  
    u_interest_int =int(u_interest)
    database_category = list_options[u_interest_int-1]

    #lists #Elina will rename these maybe 
    year_of_interest = []
    list_of_words = []

    dictofwords = dict()

    for item in json_data:
        if u_input_year == item["objectEndDate"]:
            year_of_interest.append(item[database_category])


    if u_interest_int == 5 :
        list_of_words = break_sen (year_of_interest)
    else:
        list_of_words = year_of_interest



    for item in list_of_words:
        if item in dictofwords:
            dictofwords[item] += 1
        else:
            dictofwords[item] = 1

    os.system('clear')
    listofword = list()

    for word, number in dictofwords.items() : 
        listofword.append( (number, word))

    listofword = sorted(listofword, reverse=True)


    flag_NI = 0

    for i, item in enumerate(listofword):
        if item[1] == '':
            if u_interest_int == 14 :
                listofword[i] = (item[0], 'Probably Male')
            else:
                # Create a new tuple with the updated value
                listofword[i] = (item[0], 'No Info')
                flag_NI = i

    short_list = listofword[:25]

    if len(short_list) == 0:
        print("Insufficient data related to this category.")
    else:
        print(short_list)

    short_list = [item for item in short_list if item[1] != 'No Info']

    # Extract numbers and words

    numbers = [item[0] for item in short_list]
    words = [item[1] for item in short_list]

    # Create the bar plot
    plt.figure(figsize=(10, 6))
    plt.bar(words, numbers, color='skyblue')

    # Add labels and title
    plt.xlabel(list_user_option[u_interest_int-1])
    plt.ylabel('Count')
    plt.title('Bar Plot of ' + list_user_option[u_interest_int-1] + ' vs popularity')

    # Rotate the x-axis labels for better readability
    plt.xticks(rotation=45, ha='right')

    # Display the plot
    plt.tight_layout()
    plt.show()

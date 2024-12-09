Welcome to the Metropolitan Museum of Art metadata analysis program made by Eavan and Elina for the LIBR 559c course at the UBC iSchool!

<b>What the project does:</b>

The program takes user input on a year of interest and a metadata element, and creates a bar graph for users on the top occurrences under that element in the given year. For example, if the user inputs the year 1950 and chooses “subject” as their metadata element, the program will return the most common subject terms used in the year 1950 among the items found at the MET. The MET provides metadata for almost half a million items, so this program has the possibility to reflect historical trends. 

<b>Why the project is useful:</b>

This program was mainly developed to be explored by art enthusiasts, but could be helpful for research by art historians and students as well!

<b>How users can get started with the project:</b>

The JSON and python files for this program should be saved into the same file. Open your python environment, and run the METadataAnalysis.py file. 
The program will initially take around 25 seconds to run due to the size of the JSON file. It will then prompt the user to enter a year of interest. After entering a year, the user can select the number corresponding to the metadata element they are interested in. The program will search the JSON data for occurrences of the year, and extract relevant information from those sections. If the highest occurring item under the selected metadata field is “no info,” it is removed from the graph for visual clarity, but the user may check the console to see the number of “no info” fields. 

<b>Who maintains and contributes to the project:</b>

The JSON file can be redownloaded using the data acquisition program if needed. If new items are added to the MET collections, users can contribute to this program by adding them to the file. The item ID range can be adjusted to gather information from only those items, and not the full 500,000. 


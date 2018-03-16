'''
Created on Nov 13, 2017

@author: jschmid3@stevens.edu
Pledge:    I pledge my honor that I have abided by the Stevens Honor System -Joshua Schmidt

CS115 - Hw 10 musicrecplus
'''
import sys

# musicrecplus.py
# Read and write operations on user preferences file.

# File format: Text file, one line per user.  Each line:
# username:artist1,artist2,...,artistN

# To process the file we need to:
# - split into lines
# - for each line, split at the colon, to get username and artists
# - split at commas to get artists
# - remove leading and trailing spaces, and convert all letters to lower case
#   (so comparisons work reasonably).

# Example of putting names in standard format
# example_artist = "  the clash of Death  "
# print example_artist.strip().lower()

# Note if we were to now:
# print example_artist
# it would still be "  the clash of Death  ", as strings
# are immutable and methods that operate on strings actually
# return new strings.
    
def check_name_in_file(name_to_check, data):
    """checks if name is in file and returns True if it is"""
    if name_to_check in data:
        return True
    return False

def menu():
    """has the menu of options to choose from"""
    cont = False
    while cont == False:
        choice = input("Enter a letter to choose an option:\n" +
            "e - Enter preferences\nr - Get recommendations\n" +
            "p - Show most popular artists\nh - How popular is the most popular\n" +
            "m - Which user has the most likes\nq - Save and quit\n")
        if isinstance(choice, str):
            cont = True
        else:
            print("please enter one of the choices above")
    return choice

#E - enter preferences
def enter_preferences():
    """allows user to enter preferences for music"""
    stop = False
    artists_to_add = []
    while stop == False:
        new_artist = input("Enter an artist that you like (Enter to finish)\n")
        if new_artist == "":
            stop = True
        artists_to_add += [new_artist]
    return artists_to_add

#R - get recommendations
def get_recommendations(name, data):
    """gives recommendations for music based on likes and what others
    liked that the user likes that is different"""
    #sorts preferences in alphabetical order
    #do this to make it easier to compare
    for key in data:
        data[key] = selection_sort(data[key])
    most_similar_key = ""
    max_matches = 0
    for key in data:
        if not(key[-1] == "$" or data[key] == data[name]):
            """if the person is not private or does not have the same data"""
            matches = num_matches(data[key], data[name])
            if matches > max_matches:
                most_similar_key = key
                max_matches = matches
    if most_similar_key == "":
        print("No recommendations available at this time")
        return 1
    else:
        final_recommendations = []
        for x in data[most_similar_key]:
            if x not in data[name]:
                final_recommendations += [x]
        return final_recommendations
#P - get most popular artists
def get_most_popular_artists(data):
    """gives the most liked artist(s), excluding the private $ users"""
    #list of artists
    artists = []
    for key in data:
        if key[-1] != "$":
            for x in data[key]:
                artists += [x]
    sorted_artists = selection_sort(artists)
    count = 1
    max_count = 1
    max_artists = []
    for i in range(len(sorted_artists)-1):
        #ends at second to last index because I use i and i + 1
        if sorted_artists[i] == sorted_artists[i+1]:
            count += 1
        else:
            if count == max_count:
                max_artists += [sorted_artists[i]]
                count = 1
            elif count > max_count:
                max_artists = []
                max_artists += [sorted_artists[i]]
                max_count = count
                count = 1
    return max_artists

#H
def how_popular_most_popular(data):
    """gets the amount of times the most popular is liked"""
    #list of artists
    artists = []
    for key in data:
        if key[-1] != "$":
            for x in data[key]:
                artists += [x]
    sorted_artists = selection_sort(artists)
    count = 1
    max_count = 1
    max_artists = []
    for i in range(len(sorted_artists)-1):
        #ends at second to last index because I use i and i + 1
        if sorted_artists[i] == sorted_artists[i+1]:
            count += 1
        else:
            if count == max_count:
                max_artists += [sorted_artists[i]]
                count = 1
            elif count > max_count:
                max_artists = []
                max_artists += [sorted_artists[i]]
                max_count = count
                count = 1
    return max_count

def most_likes(data):
    """gets the user that likes the most artists"""
    max_likes = 0
    for key in data:
        num_likes = len(data[key])
        if num_likes >= max_likes:
            max_likes = num_likes
    most_likes_users = []
    for key in data:
        if key[-1] != "$":
            num_likes = len(data[key])
            if num_likes == max_likes:
                most_likes_users += [key]
    return most_likes_users

# Writing a file.
def write_file(filename, data):
    '''Open existing or new file named filename.
       Write the data dictionary to it.'''
    #sorts preferences in alphabetical order
    users = selection_sort(list(data))
    result = []
    for u in users:
        data[u] = selection_sort(data[u])
        result += [u, data[u]]
    output_file = open(filename, 'w')
    for i in range(len(result)):
        if i % 2 == 0:
            output_file.write(result[i])
        else:
            output_file.write(":")
            for j in range(len(result[i])):
                if result[i][j] != "" and j != len(result[i])-1:
                    output_file.write(result[i][j] + ",")
                elif j == len(result[i])-1:
                    output_file.write(result[i][j])
            if i != len(result) - 1:
                output_file.write("\n")
    output_file.close()

def swap(lst, a, b):
    """swaps 2 things based on index"""
    temp = lst[a]
    lst[a] = lst[b]
    lst[b] = temp

def selection_sort(L):
    """sorts a list alphabetically"""
    n = len(L)
    for i in range(n-1):
        min_index = i
        for j in range(i + 1, n):
            if L[j] < L[min_index]:
                min_index = j
        if i != min_index:
            swap(L, i, min_index)
    return L

def num_matches(list1, list2):
    """returns the number of elements that the
    2 lists have in common"""
    #sorted already?
    #list1.sort()
    #list2.sort()
    matches = i = j = 0
    lenLst1 = len(list1)
    lenLst2 = len(list2)
    while i < lenLst1 and j < lenLst2:
        if list1[i] < list2[j]:
            i+=1
        elif list1[i] > list2[j]:
            j+=1
        else: #they are the same
            matches+=1
            i+=1
            j+=1
    return matches

def run_the_program():
    """RUN THE PROGRAM"""
    file_name_input = "musicrecplus.txt"
    file_name_output = "musicrecplus.txt"
    
    data = {}
    ##put data into data
    try:
        input_file = open(file_name_input, 'r')   # Open the file for reading.
    except IOError: #ERROR!
        sys.exit(1)
    """asks for name"""
    name = input("Enter your name (put a $ symbol after your name if you wish your "
        + "preferences to remain private):\n")
    
    for line in input_file:            # Get one line at a time.
        user, artists = line.split(':')
        artists = artists.split(',')
        for i in range(len(artists)):
            artists[i] = artists[i].strip()
        #if you want to print everything
        #print(user + ' : ' + str(artists))
        data[user] = artists
        user = user.strip()
    input_file.close() # Important - do not forget to close the file
    
    if not check_name_in_file(name, data):
        #if the name is in the file just go to the menu
        #otherwise add the name to the file
        data[name] = enter_preferences()
        
    #go through the menu:
    end = False
    selection = ""
    while end == False:
        selection = menu()
        if selection == "e":
            #enter preferences
            data[name] =  enter_preferences()
        elif selection == "r":
            #get recommendations
            recommendations = get_recommendations(name, data)
            #print(recommendations)
            if recommendations != 1:
                for artist in recommendations:
                    print(artist)
        elif selection == "p":
            #show most popular artists
            popArtists = get_most_popular_artists(data)
            if len(popArtists) == 0:
                print("Sorry, no artists found")
            else:
                for x in popArtists:
                    print(x)
        elif selection == "h":
            #how popular is the most popular
            result = how_popular_most_popular(data)
            if result == 0:
                print("Sorry, no artists found")
            else:
                print(result)
        elif selection == "m":
            #which user has the most likes
            users = most_likes(data)
            if len(users) == 0:
                print("Sorry, no user found")
            else:
                for x in users:
                    print(x)
        elif selection == "q":
            #quit
            end = True
        else:
            #did not pick correctly
            print("please input selection from above")
    #FINISH:
    write_file(file_name_output, data)
    sys.exit(0)

run_the_program()
chest = {
'42': 'It is the Answer to Life the Universe and Everything.',
'666': 'If you would be a real seeker after truth, it is necessary that at least once in your life you doubt, as far as possible, all things.',
'8': 'It is wrong always, everywhere and for everyone, to believe anything upon insufficient evidence.',
'13': 'The Truth is in the Heart.',
'0': 'Freedom is secured not by the fulfilling of ones desires, but by the removal of desire.',
'9': 'The unexamined life is not worth living.',
'76': 'Life is a series of natural and spontaneous changes.',
'70': 'God is dead! He remains dead! And we have killed him.'
}

# Q.1  Sort the dictionary by its keys. Using traditional sorting
def sort_list(data_list, sort="asc"):

    for i in range(1,len(data_list)):

        for j in range(len(data_list)-i):

            #compare and and swap
            if sort=="desc":
                if int(data_list[j]) < int(data_list[j+1]):     
                    data_list[j],data_list[j+1] =data_list[j+1],data_list[j]
            else:
                if int(data_list[j]) > int(data_list[j+1]):     
                    data_list[j],data_list[j+1] = data_list[j+1],data_list[j]

    return data_list

   
def sort_dict(data_dict, sort="asc"):
    dict_keys = list(data_dict.keys())
    dict_keys = sort_list(dict_keys, sort)
    sorted_dict = {}

    for key in dict_keys:
        sorted_dict[str(key)] = chest[str(key)]

    return sorted_dict


sorted_dict = sort_dict(chest)
print("Sorted chest: ", sorted_dict)



# Q.2 Get the values of first, second, last and second last keys
dict_values = list(sorted_dict.values())
first_val, second_val, second_last_val, last_val = dict_values[0], dict_values[1], dict_values[-2], dict_values[-1] 
print("first val: ", first_val)
print("second val: ", second_val)
print("last val: ", last_val)
print("second last val: ", second_last_val)

#Q.3  Concatenate the values of obtained keys in a string
conc_str = first_val +" " + second_val +" " +last_val +" " +second_last_val
print("concatenated string value is: , ",conc_str)

# Q.4 Get first and last characters of each word in concatenated string, no spaces in between
str_split = conc_str.split()  #splitted concatednated string to get list of string 

fst_lst_str =''
for i in range(len(str_split)):
    fst_lst_str += str_split[i][0] + str_split[i][-1]  #Adding first and last chaarcters of each elements of the list
print("first and last characters are ",fst_lst_str)

# Q.5 Get the number of occurrences of each letter in the resulting string and get top 5 letters
# without using any python package. The uppercase character should be counted in the lower
# case. Eg: ‘A’ character should result in an increment of key ‘a.’.
# Result should be in the format: {'a':32,'b':12,'c':10,'d':8,'e':6}
# number_of_occurences = [32,12,10,8,6]
occurences = {}
  
for ch in fst_lst_str:
    if ch in occurences:
        occurences[ch] += 1
    else:
        occurences[ch] = 1
# print("Number of occurences of each letter of the string is", occurences)
count_values_desc = sort_list(list(occurences.values()), sort="desc")[:5]
desc_letters = dict()

for count in count_values_desc:

    for key, value in occurences.items():

        #breaking if dict size is greater than 5
        if len(desc_letters) >= 5: break

        if int(value) == int(count):
            desc_letters[key] = value

print("top 5 letters",desc_letters)

top_letters = {}
for key in desc_letters:
    top_letters[key] = occurences[key]  #sorted top 5 dictionary values

print("top five occuring characters are",top_letters)
top_vals = list(top_letters.values()) # Number of occurences of each letters
print("NO of occurences",top_vals)

# Q.6 On the chest infront of you, there is a list of numbers
key_list = [52,51,61,71,58]

#Q.7  Sum the number_of_occurrences of the resulting dictionary with values of the key_list you
#found in the chest.
sum_list = [a+b for a, b in zip(key_list, top_vals)]
print("sum of two list is", sum_list)

# Q.8  Then, get the ascii character of those 5 summed values and you shall get the treasure.
ascii_values = []
for elements in sum_list:
	ascii_values.extend(ord(character) for character in str(elements)) 

print("ASCII values of the characters of the list is",ascii_values)


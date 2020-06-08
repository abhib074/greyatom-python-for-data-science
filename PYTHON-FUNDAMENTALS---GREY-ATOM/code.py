# --------------
# Code starts here

# Create the lists
class_1=['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
class_2=['Hilary Mason','Carla Gentry','Corinna Cortes']
# Concatenate both the strings
new_class=class_1+class_2
print(new_class)
# Append the list
new_class.append('Peter Warden')
# Print updated list
print(new_class)

# Remove the element from the list
new_class.remove('Carla Gentry')
# Print the list
print(new_class)
# Create the Dictionary
courses={"Math":65,"English":70,"History":80,"French":70,"Science":60}


# Slice the dict and stores  the all subjects marks in variable
marks_math=courses.get('Math')
marks_english=courses.get('English')
marks_history=courses.get('History')
marks_french=courses.get('French')
marks_science=courses.get('Science')
# Store the all the subject in one variable `Total`
Total=marks_english+marks_french+marks_history+marks_science+marks_math
# Print the total
print(Total)
# Insert percentage formula
print((Total/500)*100)
# Print the percentage




# Create the Dictionary
mathematics={"Geoffrey Hinton":78,"Andrew Ng":95,"Sebastian Raschka":65,"Yoshua Benjio":50,"Hilary Mason":70,"Corinna Cortes":66,"Peter Warden":75}
max_marks_scored=max(courses,key=courses.get)
print(max_marks_scored)
topper=max(mathematics,key=mathematics.get)
print(topper)
# Given string
string = topper

# Create variable first_name
last_name,first_name=topper.split()
# Create variable Last_name and store last two element in the list

# Concatenate the string
full_name=first_name+' '+last_name
# print the full_name
print(full_name)
# print the name in upper case
certificate_name=full_name.upper()
print(certificate_name)
# Code ends here



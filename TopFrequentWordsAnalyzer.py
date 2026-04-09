filename = input("Enter your file name:  ")       #HERE FILENAME TAKE AS INPUT

try:
  file = open(filename,"r")
except:                                         #OPEN FILE + SAFETY IF FILE DOESN'T EXIST
  print("File doesn't exist")
  exit()

lines = file.readlines()
file.close()                                    #FILE READ HERE

word_count = {}                                 #EMPTY DICTIONARY CREATE 

#Step 1 : Count Words
for line in lines:
  words = line.lower().split()
  
  for word in words:
    if word in word_count:                  #COUNT LOGIC HERE
      word_count[word]+= 1                  #AGAR WORD AYA TO +1 VERNA NEW ENTRY BANA DO
    else:                                   #Eg: hello -> 1 , hello -> 2 , world -> 1  
      word_count[word] = 1

#Step 2: Print total & unique
total_words = sum(word_count.values())
unique_words = len(word_count)

print("Total Words:",total_words)
print("Unique Words:",unique_words)

#Step3: Sort by frequency
sorted_words = sorted(word_count.items(), key=lambda x:x[1],reverse=True)

#Step 4: Top 3 Words
print("\nTop 3 Words: ")
for word,count in sorted_words[:3]:
  print(word,":",count)
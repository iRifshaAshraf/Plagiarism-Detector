#!/usr/bin/env python
# coding: utf-8
#!/usr/bin/env python
# coding: utf-8
import hashlib #helps to identify to read a file
import os
#Takes in the file paths of the target document and the source documents, and returns the percentage of the target document that matches the source documents.
def check_plagiarism(target_file, source_files):
 with open(target_file, 'r') as f:
    target_text = f.read()
    target_tokens = tokenize(target_text)
    source_tokens = []
 for source_file in source_files:
    with open(source_file, 'r') as f:
        source_text = f.read()
        source_tokens += tokenize(source_text)
        matching_words = compare_documents(target_tokens, source_tokens)
        percentage = (matching_words / len(target_tokens)) * 100
        return percentage
# Takes in a string of text and returns a list of tokens (words) in the text
5
def tokenize(text):
 return text.split()
# Takes in a list of tokens and returns a hashmap where the keys are the tokens and the values are the number of times each token appears in the list.
def create_hashmap(tokens):
 hashmap = {}
 for token in tokens:
    hashmap[token] = hashmap.get(token, 0) + 1
    return hashmap
#Takes in two lists of tokens (the target document and the source documents) and returns the number of matching words between the two lists
def compare_documents(target_tokens, source_tokens):
 target_hashmap = create_hashmap(target_tokens)
 source_hashmap = create_hashmap(source_tokens)
 matching_words = 0
 for target_token, target_count in target_hashmap.items():
    if target_token in source_hashmap:
        matching_words += min(target_count,
        source_hashmap[target_token])
        return matching_words
def text_plagiarismDetector(text1, text2):
 # Convert texts to lowercase
 text1 = text1.lower()
 text2 = text2.lower()

 # Tokenize texts
 text1_tokens = text1.split()
 text2_tokens = text2.split()
 # Find the intersection of the two lists of tokens
 common_tokens = set(text1_tokens).intersection(text2_tokens)
 # Calculate the percentage of similarity
 similarity = (len(common_tokens) / len(text1_tokens)) * 100
 return similarity
target_file = 'file1.txt'
def userFile():
 source_files = []
 while True:
    file_path = input("Enter the path of file or type 'done' if you have entered all the files: ")
    if file_path.lower() == 'done':
        break
    source_files.append(file_path)
    plagiarism_percentage = check_plagiarism(target_file, source_files)
 print(f'Plagiarism percentage: {plagiarism_percentage:.2f}%')

# Interface
print("Welcome to Plagiarism Detector")
print("==============================")
7
print("Press 1 \t To input file to detect plagiarism....: ")
print("Press 2 \t To input texts to detect plagiarism...: ")
option = int(input("Input: "))
print("\nYou entered...: ", option)
if option == 1:
 print("\nTo input file to detect plagiarism")
 print("----------------------------------\n")
 userFile()
elif option == 2:
 print("\nTo input file to detect plagiarism")
 print("----------------------------------\n")
 text1 = input('Enter your text 1..: ')
 text2 = input('Enter your text 2..: ')

 x = text_plagiarismDetector(text1, text2)
 print("The plagiarism is...: ", x)
else:
 print("\nInvalid Input!")
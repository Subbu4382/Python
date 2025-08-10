# import os
# os.getcwd()
# f=open(r'C:\Users\subra\OneDrive\Desktop\Practice\Python\factorial.py')
# a=f.read()
# print(a)
# a=f.readline()
# print(f.close())
# print(a) 

# f=open(r'sample.txt','w')
# f.write("this is written by subbu") # write() mode Overwriters the before text
# f.close()

# f1=open(r'sample.txt','a')   #append
# f1.write(" .learning file using python") # Add text to end of a file
# f1.close()

# # Creates a file and write text if file not exists
# f2=open(r'sample3.txt','w')
# f2.write('we are adding to write a text on the file which does not exists')
# f2.close()


# if os.path.exists("sample.txt"):
#     print("File exists.")
# else:
#     print("File not found.")

# # os.remove('sample2.txt')   # deletes the file


# # The with block ensures the file is automatically closed, 
# # even if an error occurs — making your code safer and cleaner.

# with open("sample.txt", "r") as f:
#     lines = f.readlines()
#     print(len(lines))
#     for i in range(len(lines)):
#         print(f"Line {i+1}: {lines[i].strip()}")

# with open("sample.txt", "r") as f:
#     content = f.read()
#     words = content.split()
#     characters = len(content)

# print("Word count:", len(words))
# print("Character count:", characters)

# with open("sample.txt", "r") as f:
#     words = f.read().split()
#     freq = {}
#     for word in words:
#         if word in freq:
#             freq[word] += 1
#         else:
#             freq[word] = 1

# # Find the word with max frequency
# max_word = max(freq, key=freq.get)
# print("Most frequent word:", max_word)

# try:
#     f=open("sample.txt","r")
#     a=f.read()
#     print(a)
# except FileNotFoundError:
#     print("file not found")
# else:
#     print("no error in code")
# finally:
#     print("program executed")


# # . Count the number of lines in a file
# with open("sample.txt","r") as f:
#     count=0
#     for i in f.readlines():
#         count+=1
# print(count)

# # Read a file and print the longest line
# with open("sample.txt","r") as f:
#     longest=""
#     for i in f:
#         if len(i)>len(longest):
#             longest=i
#     print(longest)

# # Write and read student data (name, age, grade) to/from a file
# with open ("sample.txt","a") as f:
#     f.write(" subbu,21,42r batch")
# with open ("sample.txt","r") as f:
#     print(f.readlines())

# # Append a line to an existing file
# with open("sample.txt","a") as f:
#     f.write("\nthis line is added")

# # Read a file and count the occurrence of each word
# freq={}
# with open("sample.txt","r") as f:
#     for line in f:
#         words=line.split()
#         for word in words:
#             if word in freq:
#                 freq[word]+=1
#             else:
#                 freq[word]=1
# print(freq)

import os 
import glob
import socket

#write it to result.txt
#f = open("C:\\Users\\Jsmit_1n8uqvk\\Desktop\\Cloud Computing\\Homework2\\home\\output\\result.txt", "w")
f = open("/home/output/result.txt", "w")
#list all the text files at location: /home/data
#os.chdir("C:\\Users\\Jsmit_1n8uqvk\\Desktop\\Cloud Computing\\Homework2\\home\\data")
os.chdir("/home/data")
for file in glob.glob("*.txt"):
    print(file, file=f)
#Read the text files and count total number of words in each text files
#Reads the first data.txt word count
#file = open("C:\\Users\\Jsmit_1n8uqvk\\Desktop\\Cloud Computing\\Homework2\\home\\data\\data.txt", "rt")
file = open("/home/data/data.txt", "r")
data = file.read()
words = data.split()
print('Data.txt file has: {} words'.format(len(words)))
#Reads the second data1.txt word count
#file1 = open("C:\\Users\\Jsmit_1n8uqvk\\Desktop\\Cloud Computing\\Homework2\\home\\data\\data1.txt", "rt")
file1 = open("/home/data/data1.txt", "r")
data1 = file1.read()
words1 = data1.split()
print('Data1.txt file has: {} words'.format(len(words1)))
#Reads the thrid data2.txt word count
#file2 = open("C:\\Users\\Jsmit_1n8uqvk\\Desktop\\Cloud Computing\\Homework2\\home\\data\\data2.txt", "rt")
file2 = open("/home/data/data2.txt", "r")
data2 = file2.read()
words2 = data2.split()
print('Data2.txt file has: {} words'.format(len(words2)))
#Reads the fourth data3.txt word count
#file3 = open("C:\\Users\\Jsmit_1n8uqvk\\Desktop\\Cloud Computing\\Homework2\\home\\data\\data3.txt", "rt")
file3 = open("/home/data/data3.txt", "r")
data3 = file3.read()
words3 = data3.split()
print('Data3.txt file has: {} words'.format(len(words3)))

#Total word count of all the files:
total = len(words) + len(words1) + len(words2) + len(words3)
print("Total number of words in all files: {}".format(total), file=f)
print("Total number of words in all files: {}".format(total))

#list the file name with the maximum number of words
print("Data.txt has the maximum word count: {} words".format(len(words)), file=f)
print("Data.txt has the maximum word count: {} words".format(len(words)))
#Find the IP address of your machine:
hostName = socket.gethostname()
IPAddr = socket.gethostbyname(hostName)
print("Your computer name is: {}".format(hostName), file=f)
print("Your computer name is: {}".format(hostName))
print("Your computer IP address is: {}".format(IPAddr), file=f)
print("Your computer IP address is: {}".format(IPAddr))
f.close()


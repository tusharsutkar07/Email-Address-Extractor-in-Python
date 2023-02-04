'''
Purpose: For only education purpose.
Description: email extractor -
This is a program that will take url link and
print email addresses only, from that website,
if emails available in that webpage,
and it can also work with txt file also.
'''

from bs4 import BeautifulSoup
import requests
import re

print("wellcome to the email address extractor")
while True:
    print("\npress 1 to extract emails form a website\n"
          "press 2 to extract emails from a text file\n"
          "press e to exit")
    user_input=input()
    try:
        if user_input=="1":
            url=input("Enter url here: ")
            ra=requests.get(url)
            soup=BeautifulSoup(ra.text, "html.parser")

            full_text=soup.find_all()
            list1=[]
            for i in str(full_text).split():
                if "@" in i:
                    b=re.findall(r"[a-z0-9A-Z\.\-+_]+@[a-z0-9A-Z\.\-+_]+\.[a-zA-Z]+",i)
                    for i in b:
                        if i not in list1:
                            list1.append(i)
            count=0
            for i in list1:
                count+=1
                print(f"Email no {count}: {i}")

        elif user_input=="2":
            file_path=input("Enter file path: ")
            file_name=input("Enter file name without .txt extension: ")
            file=open(f"{file_path}\{file_name}.txt")
            e=file.read()
            b=re.findall(r"[a-z0-9A-Z\.\-+_]+@[a-z0-9A-Z\.\-+_]+\.[a-zA-Z]+", e)
            n=0
            list2=[]
            for i in b:
                if i not in list2:
                    list2.append(i)
            for i in list2:
                n+=1
                print(f"email no-{n}: {i}")
            file.close()

        elif user_input=="e":
            print("exited")
            exit()
        else:
            print("wrong input")

    except Exception as e:
        print("error")

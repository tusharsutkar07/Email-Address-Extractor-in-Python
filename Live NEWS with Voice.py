'''
Purpose: For only education purpose.
Description: Live NEWS with Voice -
This is a program that will take the
10 NEWS headlines from the News API, and
we can read those headlines, or we have an
option of NEWS Speaking feacher also.
'''

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("sapi.spvoice")
    speak.speak(str)

def news():
    import requests

    query_params = {
            "source": "bbc-news",
            "sortBy": "top",
            "apiKey": "4dbc17e007ab436fb66416009dfb59a8"
        }

    main_url = " https://newsapi.org/v1/articles"

    a=requests.get(main_url,params=query_params)
    open_bbc_news_page=a.json()
    artical=open_bbc_news_page["articles"]
    result= []

    for ar in artical:
        result.append(ar["title"])

    for i in range(len(result)):
        print(i + 1, result[i])

    try:
        print("\nPress r to read the NEWS"
              "\nPress e to exit")

        def speak(str):
            from win32com.client import Dispatch
            speak = Dispatch("sapi.spvoice")
            speak.speak(str)
        speak(",this is the today's NEWS, now, "
              ",press r, to read the NEWS, press e, to exit the NEWS")

        while True:
            user_input=input()
            if user_input=="r":
                from win32com.client import Dispatch
                speak = Dispatch("SAPI.Spvoice")
                speak.Speak(result)
                break
            if user_input=="e":
                print("Exited")
                speak(",Exited")
                exit()
            else:
                print("Invalid input")
                continue

    except Exception as e:
        print(e)

while True:
    print("Press 1 for NEWS"
          "\nPress e to exit")
    speak("\nPress 1 for NEWS, press e to exit")
    try:
        user_input = input()
        if user_input == "1":
            print("Please wait...")
            news()
        if user_input=="e":
            exit()
        if user_input!="e" and user_input!="1":
            print("Wrong input")
            continue
        else:
            print()
    except Exception as e:
        print(e)
        speak(e)

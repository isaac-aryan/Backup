#IMPORTED STUFF
import webbrowser
import time
import random

#Introduction. If you're confused, check README.md

print("\t~Instagram and Twitter Bot~")
print("\n\n[+]Welcome! This is the fastest and easiest way to gain folloers on Instagram or Twitter.")

#Choice of Social Media platform
smchoice=input("[+]Enter the social media platform you want to gain followers on.\n")

if smchoice.lower()=="twitter":
    print("\nTWITTER BOT")

    #Asking for handle. (This doesn't make a difference at all.)
    print("\n[+]Enter your Twitter handle...\n")
    handle=input()
    print("\n[+]The handle you have entered is @"+handle)

    #Asking for number of followers. Also does not matter
    print("\n[+]Enter the number of followers you want to gain...(Maximum 2000)\n")
    fol=int(input())
    if fol>=0:
        print("[+]Generating followers...(this shouldn't take long)")
        time.sleep(3)
        visit="https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        webbrowser.open(visit)
    else:
        visit="https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        webbrowser.open(visit)

elif smchoice=="insta" or "instagram":
    print("\nINSTAGRAM BOT")

    #Asking for handle. (This doesn't make a difference at all.)
    print("\n[+]Enter your Instagram handle...\n")
    handle=input()
    print("\n[+]The handle you have entered is @"+handle)

    #Asking for number of followers. Also does not matter
    print("\n[+]Enter the number of followers you want to gain...(Maximum 2000)\n")
    fol=int(input())
    if fol>=0:
        print("[+]Generating followers...(this shouldn't take long)")
        time.sleep(5)
        visit="https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        webbrowser.open(visit)
    else:
        visit="https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        webbrowser.open(visit)

else:
    print("SIKE!")
    visit="https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    webbrowser.open(visit)



#MEME MAKER

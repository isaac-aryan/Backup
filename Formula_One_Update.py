#FORMULA ONE A.I

#This is an updated and more functional version of Aryan's initial Formula One A.I

#CODE

#Imported modules
import speech_recognition as sr
import webbrowser as wb
r=sr.Recognizer()

#Introduction
print("Welcome to this all new Formula One A.I developed by Aryan Bhobe.\nThe purpose of this program is to provide as much information needed to draw attention to this fascinating sport that is not as celebrated as, say, Football or Cricket.\n")

#Choice- Constructor or General
print("First you must choose whether you want to learn about Formula One in general or a specific Formula One constructor(team).\n\n")

def main():
    with sr.Microphone() as source:
        print("To choose General F1 Questions, say 'general'.\n")
        print("To choose a Specific Constructor, say 'constructor'.\n\n")
        print("You may speak now...\n")

        audio = r.listen(source)

        try:

            choice=r.recognize_google(audio)
            choice=choice.lower()   #Choice of constructor or general stored in choice variable

            print("You said ",str(choice))


        except:
            print("Invalid choice. Pleas rerun program.")

        #Outcome of choice
        if 'general' in choice:
            print("You have chosen to know about Formula One in general.")


        elif 'constructor' in choice:
            print("You have chosen to know about a specific constructor.")

            #Constructor Display and Choice
            print("\n\nGreat! Now that you have chosen to learn about a specific constructor you are ready to choose one. \nBut first, what is a constructor?\n->A constructor in f1 is basically a team. Each constructor consists of two drivers and a reserve driver.\n\n")
            print("\nThere are altogether 10 Constructors in Formula One this season. Your job is to choose the one that intrigues you the most and I will do as much as I can to inform you about it.\n")
            print("The following are the Formula One constructors...")

            print("--------------------------------------------------------------")

            print("\t1) Aston Martin Red Bull Racing [RB]\n")

            print("\t2) McLaren F1 Team [MC]\n")

            print("\t3) Renault F1 Team [RN]\n")

            print("\t4) Red Bull Toro Rosso Honda [TR]\n")

            print("\t5) Mercedes-AMG Petronas Motorsport [MR]\n")

            print("\t6) Racing Point F1 Team [RP]\n")

            print("\t7) Williams Racing [WI]\n")

            print("\t8) Rich Energy Haas F1 Team [HA]\n")

            print("\t9) Alfa Romeo Racing [AR]\n")

            print("\t10) Scuderia Ferrari [FR]\n")

            print("--------------------------------------------------------------")

            print("\n\nRead through all of them and continue when you are done.\n")

            contd=input("Press 'c' to continue...")
            if contd=='c':
                with sr.Microphone() as source:
                    print("Choose your constructor by saying the 2 letter code given in the brackets.\nYou may speak now...")

                    audio = r.listen(source)

                    try:

                        constructor = r.recognize_google(audio)
                        constructor = constructor.lower()
                        print("You said: ", str(text))

                        #Constructo choice outcomes

                        #Aston Martin Red Bull Racing
                        if constructor=="rb":
                            print("You have chosen Aston Martin Red Bull Racing!\n")
                            print("Normally we just refer to this constructor as Red Bull.\n")
                            
                        elif constructor=="mc":
                            print("You have chosen McLaren F1 Team!\n")
                            print("Normally, we just refer to this constructor as McLaren.\n")
                            
                        elif constructor=="rn":
                            print("You have chosen Renault F1 Team!\n")
                            print("Normally, we just refer to this constructor as Renault.\n")
                            
                        elif constructor=="tr":
                            print("You have chosen Red Bull Toro Rosso.")


                    except:
                        print("I did not understand what you spoke.")

main()




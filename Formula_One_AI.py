import speech_recognition as sr

r=sr.Recognizer()

#Formula One A.I
name=str(raw_input("Enter your name.."))
#Introduction and input request
con="CON"
form="FOR"

print("Hello! Welcome to the all new Formula One A.I developed by Aryan Isaac Bhobe.\n")
print("\nThe purpose of this A.I is to draw attention as well as provide information about this incredible sport that is not as celebrated as Football, Cricket etc.\n")

#CHOICE 1- f1 or constructor
print("First you need to choose what you would like to know...\n\n")
print("Would you like to know something about Current Formula One in general or something about a specific Constructor??\n\n")

print("If you would like to know something about Formula One in general type FOR\nIf you would like to know something about a specific team type CON\n")
choice1=raw_input()

if choice1==con:

    print("So you want to know something about a particular F1 Team? Great!\n")
    print("\nFirst, please enter the two-lettered code of your racing team [Constructor]. The code is in the brackets as follows:\n\n")

    #Constructor Display

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

    constructor=raw_input("\n\nPlease enter the code of your Constructor..\n")

    #TEAM IF/ELSE

    #Aston Martin Red Bull Racing

    if constructor=="RB" or constructor=="rb":
        print("You have chosen Aston Martin Red Bull Racing!\n")
        print("Normally we just refer to this constructor as Red Bull.\n")

        #BADGE
        rbd=raw_input("If you want a team badge, press y..")
        if rbd=="y":
            print("*****************************************************************************************\n")
            print("||                       - - Aston Martin Red Bull Racing - -                           ||\n")
            print("||                                                                                      ||\n")
            print("||   SOOO..You have chosen Red Bull eh? That's an incredible choice!                    ||\n")
            print("||                                                                                      ||\n")
            print("||   Remember: Red Bull is all about quick thinking and efficient decision making!      ||\n")
            print("||                                                                                      ||\n")
            print("||   That is the reason why we boast the fastest pit-stop in the history of Formula One!||\n")
            print("||                                                                                      ||\n")
            print("||   This also means you are willing to do whatever it takes to DESTROY Scuderia Ferrari||\n")
            print("||                                                                                      ||\n")
            print("||   GOOD LUCK                                                                          ||\n")
            print("||                                                                                      ||\n")
            print("*****************************************************************************************\n\n")
        else:
            print("Ok then, your loss.")


        print("\nWhat would you like to know about Red Bull?")

    #Mclaren F1 Team

    elif constructor=="MC" or constructor=="mc":
        print("You have chosen McLaren F1 Team!\n")
        print("Normally we just refer to this constructor as McLaren.\n")
        print("\nWhat would you like to know about McLaren?")

    #Renault F1 Team

    elif constructor=="RN" or constructor=="rn":
        print("You have chosen Renault F1 Team!\n")
        print("Normally we just refer to this constructor as Renault.\n")
        print("\nWhat would you like to know about Renault?")

    #Red Bull Toro Rosso Honda

    elif constructor=="TR" or constructor=="tr":
        print("You have chosen Red Bull Toro Rosso Honda!\n")
        print("Normally we just refer to this constructor as Toro Rosso.\n")
        print("\n What would you like to know about Toro Rosso?")

    #Mercedes-AMG Petronas Motorsport

    elif constructor=="MR" or constructor=="mr":
        print("You have chosen Mercedes-AMG Petronas Motorsport!\n")
        print("Normally we just refer to this constructor as Mercedes.\n")
        print("\nWhat would you like to know about Mercedes?")

    #Racing Point F1 Team

    elif constructor=="RP" or constructor=="rp":
        print("You have chosen Racing Point F1 Team!\n")
        print("Normally we just refer to this constructor as Racing Point.\n")
        print("\nWhat would you like to know about Racing Point?")

    #Williams Racing

    elif constructor=="WI" or constructor=="wi":
        print("You have chosen Williams Racing!\n")
        print("Normally we just refer to this constructor as Williams.\n")
        print("\nWhat would you like to know about Williams?")

    #Rich Energy Haas F1 Team

    elif constructor=="HA" or constructor=="ha":
        print("You have chosen Rich Energy Haas F1 Team!\n")
        print("Normally we just refer to this constructor as Haas.\n")
        print("\nWhat would you like to know about Haas?")

    #Alfa Romeo Racing

    elif constructor=="AR" or constructor=="ar":
        print("You have chosen Alfa Romeo Racing!\n")
        print("Normally we just refer to this constructor as Alfa Romeo.\n")
        print("What would you like to know about Alfa Romeo?")

    #Scuderia Ferrari

    elif constructor=="FR" or constructor=="fr":
        print("You have chosen Scuderia Ferrari!\n")
        print("Normally we just refer to this constructor as Ferrari.\n")
        print("What would you like to know about Ferrari?")

    else:
        print("Are you sure that's a Formula One Team? Maybe check the codes again.")


elif choice1==form:

    print("So you want to know something about Current Formula One in general? No problem.\n\nType your question..")

    forq=raw_input()

    #Question and Answers
    if forq=="show me the constructor standings":
        print("**************************************************************************************************************************************\n")
        print("\n\t\tFORMULA ONE CONSTRUCTOR STANDINGS")

        print("\n\nCONSTRUCTOR                            POINTS    WINS       PODIUMS")

        print("\n1] Mercedes-AMG Petronas Motorsport    527        10\t      23\n")

        print("2] Scuderia Ferrari                    394        3\t      15\n")

        print("3] Aston Martin Red Bull Racing        289        2\t      6\n")

        print("4] McLaren F1 Team                     89         0\t      0\n")

        print("5] Renault F1 Team                     67         0\t      0\n")

        print("6] Red Bull Toro Rosso Honda           55         0\t      1\n")

        print("7] Racing Point F1 Team                46         0\t      0\n")

        print("8] Alfa Romeo Racing                   35         0\t      0\n")

        print("9] Rich Energy Haas                    26         0\t      0\n")

        print("10] Williams Racing                    1          0\t      0\n\n")
        print("****************************************************************************************************************************************")


        #Australian GP
    elif forq=="who won the australian gp" or forq=="australian gp":
        print("Here's what happened in Melbourne, Australia:\n1] V. Bottas [MERCEDES] [FINLAND]\n2] L. Hamilton [MERCEDES] [UNITED KINGDOM]\n3] M. Verstappen [RED BULL] [NETHERLANDS]\n")
    
        #Bahrain GP
    elif forq=="who won the bahrain gp" or forq=="bahrain gp":
        print("Here's what happened in Bahrain,Bahrain:\n1] L. Hamilton [MERCEDES] [UNITED KINGDOM]\n2] V. Bottas [MERCEDES] [FINLAND]\n3] C. Leclerc [FERRARI] [MONACO]\n")

        #Chinese GP
    elif forq=="who won the chinese gp" or forq=="chinese gp":
        print("Here's what happened in Shanghai, China:\n1] L. Hamilton[MERCEDES] [UNITED KINGDOM]\n2] V. Bottas [MERCEDES] [FINLAND]\n3] S. Vettel [FERRARI] [GERMANY]\n")

        #Azerbaijan GP
    elif forq=="who won the azerbaijan gp" or forq=="azerbaijan gp":
         print("Here's what happened in Baku, Azerbaijan:\n1] V. Bottas [MERCEDES] [FINLAND\n2] L.Hamilton [MERCEDES] [UNITED KINGDOM]\n3] S. Vettel [FERRARI] [GERMANY]\n")
    
         #Spanish GP
    elif forq=="who won the spanish gp" or forq=="spanish gp":
        print("Here's what happened in Barcelona, Spain:\n1] L. Hamilton [MERCEDES] [UNITED KINGDOM]\n2] V. Bottas [MERCEDES] [FINLAND]\n3] M. Verstappen [RED BULL] [NETHERLANDS]\n")

        #Monaco GP
    elif forq=="who won the monaco gp" or forq=="monaco gp":
        print("Here's what happened in Monaco. Monaco:\n1] L. Hamilton [MERCEDES] [UNITED KINGDOM]\n2] S. Vettel [FERRARI] [GERMANY]\n3] V. BOTTAS [MERCEDES] [FINLAND]\n")

        #Canadian GP
    elif forq=="who won the canadian gp" or forq=="canadian gp":
        print("Here's what happened in Montreal, Canada:\n1] L. Hamilton [MERCEDES] [UNITED KINGDOM]\n2] S. Vettel [FERRARI] [GERMANY]\n3] C. Leclerc [FERRARI] [MONACO]\n")

        #French GP
    elif forq=="who won the french gp" or forq=="french gp":
        print("Here's what happened in Le Castellet, France:\n1] L. Hamilton [MERCEDES] [UNITED KINGDOM]\n2] V. Bottas [MERCEDES] [FINLAND]\n3] C. Leclerc [FERRARI] [MONACO]\n")

        #Austrian GP
    elif forq=="who won the austrian gp" or forq=="austrian gp":
        print("Here's what happened in Spielberg, Austria:\n1] M. Verstappen [RED BULL] [NETHERLANDS]\n2] C. Leclerc [FERRARI] [MONACO]\n3] V. Bottas [MERCEDES] [FINLAND]\n")

        #British GP
    elif forq=="who won the british gp" or forq=="british gp":
        print("Here's what happened in Silverstone, England:\n1] L. Hamilton [MERCEDES] [UNITED KINGDOM]\n2] V. Bottas [MERCEDES] [FINLAND]\n3] C. Leclerc [FERRARI] [MONACO]\n")

        #German GP
    elif forq=="who won the german gp" or forq=="german gp":
        print("Here's what happened in Hockenheim, Germany:\n1] M. Verstappen [RED BULL] [NETHERLANDS]\n2] S. Vettel [FERRARI] [GERMANY]\n3] D. Kvyat [TORO ROSSO] [RUSSIA]\n")

        #Hungarian GP
    elif forq=="who won the hungarian gp" or forq=="hungarian gp":
        print("Here's what happened in Budapest, Hungary:\n1] L. Hamilton [MERCEDES] [UNITED KINGDOM]\n2] M. Verstappen [RED BULL] [NETHERLANDS]\n3] S. Vettel [FERRARI] [GERMANY\n")

        #Belian GP
    elif forq=="who won the belgian gp" or forq=="belgian gp":
        print("Here's what happened in Spa, Belgium:\n1] C. Leclerc [FERRARI] [MONACO]\n2] ")
    else:
        print("error")
else:
    print("Error")


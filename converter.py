def gender_converter(gender):
    if(gender == "Male"):
        return 0
    elif(gender == "Female"):
        return 1

def foreign_converter(foreign):
    if(foreign == "Yes"):
        return 1
    elif(foreign == "No"):
        return 0

def purpose_converter(purpose):
    if(purpose == "Work"):
        return 0
    elif(purpose == "Recreation"):
        return 1
    elif(purpose == "Education"):
        return 2

def EatingHabit_converter(EatingHabit):
    if(EatingHabit == "Vegetarian"):
        return 0
    elif(EatingHabit == "Non-Vegetarian"):
        return 1

def PrefferedPartner_converter(PrefferedPartner):
    if(PrefferedPartner == "Solo"):
        return 0
    elif(PrefferedPartner == "Friends"):
        return 1
    elif(PrefferedPartner == "Family"):
        return 2

def TravelTaste_converter(TravelTaste):
    if(TravelTaste == "Beach"):
        return 0
    elif(TravelTaste == "Hill"):
        return 1
    elif(TravelTaste == "Desert"):
        return 2
    elif(TravelTaste == "Plain"):
        return 3

def RecentVisit1_converter(RecentVisit1):
    if(RecentVisit1 == "Beach"):
        return 0
    elif(RecentVisit1 == "Hill"):
        return 1
    elif(RecentVisit1 == "Desert"):
        return 2
    elif(RecentVisit1 == "Plain"):
        return 3

def RecentVisit2_converter(RecentVisit2):
    if(RecentVisit2 == "Beach"):
        return 0
    elif(RecentVisit2 == "Hill"):
        return 1
    elif(RecentVisit2 == "Desert"):
        return 2
    elif(RecentVisit2 == "Plain"):
        return 3

def Stay_converter(Stay):
    if(Stay == "Dormitory"):
        return 0
    elif(Stay == "Hostel"):
        return 1
    elif(Stay == "Hotel 3*"):
        return 2
    elif(Stay == "Hotel 4*"):
        return 3
    elif(Stay == "Hotel 5*"):
        return 4



print(Stay_converter("Dormitory"))
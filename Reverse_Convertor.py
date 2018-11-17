
def TravelTaste_Predictor(TravelTaste):
    if(TravelTaste == 0):
        return "Beach"
    elif(TravelTaste == 1):
        return "Hill"
    elif(TravelTaste == 2):
        return "Desert"
    elif(TravelTaste == 3):
        return "Plain"

def PrefferedPartner_Predictor(PrefferedPartner):
    if(PrefferedPartner == 0):
        return "Solo"
    elif(PrefferedPartner == 1):
        return "Friends"
    elif(PrefferedPartner == 2):
        return "Family"

def Stay_Predictor(Stay):
    if(Stay == 0):
        return "Dormitory"
    elif(Stay == 1):
        return "Hostel"
    elif(Stay == 2):
        return "Hotel 3*"
    elif(Stay == 3):
        return "Hotel 4*"
    elif(Stay == 4):
        return "Hotel 5*"

def foreign_Predictor(foreign):
    if(foreign == 1):
        return "Yes"
    elif(foreign == 0):
        return "No"


print(Stay_Predictor(1))


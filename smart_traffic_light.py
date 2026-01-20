#Smart Traffic Light System

def traffic_light_controller(currentSignal, isEmergencyVehicle):

    if isEmergencyVehicle:
        return "IMMEDIATE GREEN"
    
    currentSignal = currentSignal.upper()
    
    if currentSignal == "RED":
        return "STOP"
    
    elif currentSignal == "YELLOW":
        return "PREPARE TO STOP"
    
    elif currentSignal == "GREEN":
        return "GO"
    
    else:
        return "INVALID SIGNAL"
    

#Test  
print(traffic_light_controller("RED", True))
print(traffic_light_controller("RED", False))
print(traffic_light_controller("GREEN", True))
print(traffic_light_controller("GREEN", False))
print(traffic_light_controller("YELLOW", True))
print(traffic_light_controller("YELLOW", False))
print(traffic_light_controller("Yellow", False))
print(traffic_light_controller("Violet", False))
    


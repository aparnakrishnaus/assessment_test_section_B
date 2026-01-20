#The Loyalty Points Calculator 

def calculate_loyalty_points(membershipTier, totalSpent):

    if totalSpent < 100:
        return 0
    
    points = 0

    if membershipTier == "Gold":
        points = (totalSpent // 100) * 10

        if totalSpent > 500:
            points = points + 50

    elif membershipTier == "Silver":
        points = (totalSpent // 100) * 5

        if totalSpent > 500:
            points = points + 20

    elif membershipTier == "Regular":
        points = (totalSpent // 100) * 2

    
    return int(points)

#Test
print(calculate_loyalty_points("Gold",90))
print(calculate_loyalty_points("Silver",90))
print(calculate_loyalty_points("Gold", 450))
print(calculate_loyalty_points("Silver", 620))
print(calculate_loyalty_points("Regular",320))
print(calculate_loyalty_points("Regular",100))
print(calculate_loyalty_points("Regular",90))

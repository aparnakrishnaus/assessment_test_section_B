#Inventory Stock-Out Alert 

def check_stock(stock_levels):

    for i, stock in enumerate(stock_levels):
        if stock == 0:
            print(f"Item {i}- Out of Stock")
        elif 1 <= stock <= 5:
            print(f"Item {i}- Restock Immediately")

    
#Test
stock_levels = [25,4,9,10,2,0]
check_stock(stock_levels)
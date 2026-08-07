def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 4==0 :
         #print(" aleap year")
         leap = True
         if  year %100==0 :
            #print(" Not aleap year")
            leap = False

            if year %400==0 :
                   # print(" aleap year")
                    leap = True 
    else:
       # print(" Not aleap year")
        leap = False
    
    
    return leap










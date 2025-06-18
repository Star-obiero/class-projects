
        #Default value
day = 5
match day:
            case 6:
                print('Today is saturday')
            case 7:
                print('Today is sunday')
            case _:
                print('looking foward to the weekend')

                

        #combinevalues

day = 4
match day:
                case 1|2|3|4|5:
                  print("Today is a weekend")
                case 6|7:
                  print('I love weekends')



#While loop
i = 1
while i < 6:
    print(i)  # Indent this line
    if (i == 3):  # Indent this line
        break  # Indent this line
    i += 1  # Indent this line
#continue
i=0
while i<6:
      i+=1
      if i==3:
            continue
      print(i)




  #For loop

  for x in "banana":
       print(x)

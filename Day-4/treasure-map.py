'''
WE HAVE TO HIDE yYOUR TREASURE, BASED ON THE INPUT
IF THE INPUT IS GIVEN AS B3. YOU HAVE TO SHOW 'X' MARK AS HIDDEN PLACE OF TREASURE
  A  B  C
1 ■  ■  ■
2 ■  ■  ■
3 ■  ■  ■

OUTPUT FOR INPUT B3:
  A  B  C
1 ■  ■  ■
2 ■  ■  ■
3 ■  X  ■
'''
#MY SOLUTION:
line1=["■","■","■"]
line2=["■","■","■"]
line3=["■","■","■"]
#name=input("Enter your name : ")
print("HIDE YOUR TREASURE")
position=input("Enter your position to hide").lower()
row_index=position[0]
if row_index=='a':
    letter=0
elif row_index=='b':
    letter=1
else:
    letter=2
    
number=int(position[-1])
map=[line1,line2,line3]
map[letter][number] = 'X'
print(f"{line1}\n{line2}\n{line3}")

#SOLUTION2:
letter=position[0].lower()
abc=["a","b","c"]
letter_index=abc.index(letter) #based on the above list it will give index for input B3as B=1
number_index=int(position[1])-1 #In B3, it will take 3 and index will be 3-1=2
map[number_index][letter_index]
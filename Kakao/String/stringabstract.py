# -*- coding: utf-8 -*-
"""StringAbstract.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LtaiSBa8vX-fvpqX_PSck2QzRPWY8bat
"""

"aabbaccc"	7
"ababcdcdababcdcd"	9
"abcabcdede"	8
"abcabcabcabcdededededede"	14
"xababcdcdababcdcd" 17

s = "aabbaccc"
sub = s[7:8]
print(sub)

# solution.py

def solution(s):
    answer = 0

    # set the answer as the length of s
    answer = len(s)
    answer_str = ""
   
    # working string
    string = ""

  #debugging
    this_str = ""
    next_str = ""

    # temporary string
    temp_str = ""
  
    # how many substring is in the string
    counter = 1

    # for loop for the length of strings from 1 to 1000
    for i in range(1,int(len(s)/2) + 1):

      #length of string named s
      string = s[0:i]

      #test
      print( "i is " + "{}".format(i) + " string is "+ string)

      for x in range(len(string), len(s), len(string)):
        substring = s[x:x + len(string)]
        print(substring)
        
        # substring matches
        if string == substring:
          if x != len(s):
            counter += 1
            continue
          else:
             # update the temp_str
            temp_str = temp_str + "{}".format(counter)+ string

        # substring does not match
        else:
          # if there are more than one matching
          if counter != 1:
            # update the temp_str
            temp_str = temp_str + "{}".format(counter)+ string
          # just one string 
          else:
            temp_str += string
        
        # change the working string
        string = substring
        # reset the counter
        counter = 1

      print("nested for loop, temp_string: " + temp_str + " string: " + string)

      #check the min length
      if answer > len(temp_str):
        answer = len(temp_str)
        answer_str = temp_str
        print("this is the answer: " +"{}".format(answer)  )
        print(answer_str)

      #reset the temp_str
      temp_str = ""


    return answer
 
solution("aabbaccc")

# temp 2

# solution.py

def solution(s):
    answer = 0

    # set the answer as the length of s
    answer = len(s)
    answer_str = ""
   
    # working string
    string = ""

  #debugging
    this_str = ""
    next_str = ""

    # temporary string
    temp_str = ""
  
    # how many substring is in the string
    counter = 1

    #flag for checking the last input or not
    flag = false

    # for loop for the length of strings from 1 to 1000
    for i in range(1,int(len(s)/2) + 1):

      #length of string named s
      this_str = s[0:i]

      #test
      print( "length of string is " + "{}".format(i) + " string is "+ this_str +"\n")

      for x in range(len(this_str), len(s), len(this_str)):

  #print("{}".format(x)+"th trial" )
        substring = s[x:x + len(this_str)]
  #print("{}".format(x)+"th trial after" )
        print("current string is: " + substring)
        
        # substring matches
        if this_str == substring:
          print("string matches! ") #debug
          counter += 1 
          # if this is not the last character
          if x + len(this_str) != len(s):
          #if x != len(s):
            #print("continue! " + "{}".format(x) + " "+"{}".format(len(s)))
            continue
          # Last char case.
          else:             
            # update the temp_str
            #temp_str = temp_str + "{}".format(counter)+ string + "{}".format(x) 
            temp_str = temp_str + "{}".format(counter)+ substring #+ "{}".format(x) 

        # substring does not match
               
        else:
          print("string does not matches! ")   # debug
          print("before temp_str: " + temp_str )
          # if there are more than one matching
          if counter != 1:
            # update the temp_str
            #temp_str = temp_str + "{}".format(counter)+ this_str
            temp_str = temp_str + "{}".format(counter) + this_str
          # just one string 
          else:
            temp_str += this_str
          print("after temp_str: " + temp_str)




        
        print("case "+ "i: " "{}".format(i) + " x: " + "{}".format(x) +" temp_string: " + temp_str + " this_str: " + this_str + " temp_str: " + temp_str + " substring:"+ substring +" counter: " + "{}".format(counter))
        #print("temp_str: " + temp_str )
        # change the working string
        this_str = substring
        # reset the counter
        counter = 1

  #      print("Loop2 :" + "{}".format(x) +" temp_string: " + temp_str + " this_str: " + this_str)

 #     print("Loop1 :" + "{}".format(x) +" temp_string: " + temp_str + " this_str: " + this_str)

      #check the min length
      if answer > len(temp_str):
        answer = len(temp_str)
        answer_str = temp_str
        print("this is the answer: " +"{}".format(answer)  )
        print(answer_str)

      #reset the temp_str
      temp_str = ""


    return answer
 
solution("aabbaccc")


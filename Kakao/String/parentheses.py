# -*- coding: utf-8 -*-

# parentheses example

def solution(p):

  #print("solution called, p is: " + p + "\n" )

  answer = ""

  #strings and substrings
  #w = ""
  u = ""
  v = ""
  temp_str = ""
  rev_str = ""

  #number of parentheses
  left = 0
  right = 0
  count  = 0

  # flag
  correct = True;

  #step 1
  #if p is an empty string, return p;
  if len(p) == 0:
    #print("empty string!")
    return p

  # step 2
  #count the number of parentheses 
  for i in range(0, len(p)):
    if p[i] == "(" :
      left += 1
    else:
      right += 1

    # this is the first case the number of left and right are the same
    if left == right:
      u = p[0: 2*left]
      v = p[2*left:]

      #print("u: " + u)
      #print("v: " + v)
      break
  
  
  # check this is the correct parenthese ()
  for i in range(0, len(u)):

    #count the number of "("
    if u[i] == "(":
      count += 1

    # find ")"
    else:
      # if the first element is not "("
      if count == 0 and i == 0 :
        #print("u: "+ u +" change to false")
        correct = False
        break

      # reduce the number of counter
      count -= 1

      if count < 0:
        correct = False
        break;
      else:
        continue
    
    """
      for j in range(1, count + 1):
        print("i is " + "{}".format(i) + " j is " + "{}".format(j)  + " count: " + "{}".format(count) + " lenth of u is " + "{}".format(len(u)))
        
        #
        #if u[i+j] == "(" :
        if count < 0:
        
        
        
          print( " change to false " + "i is " + "{}".format(i) + " j is " + "{}".format(j)  + " count: " + "{}".format(count))
          correct = False
          break
        else:
          continue
    """
  # reset the counter
  count = 0
  #print( "u: " + u + " v: " + v)

  #if the string u is correct
  if correct == True:
    temp = u + solution(v)
    #print(" u is " + u +" CORRECT! and return: " + temp)
    return temp
  # if the string u is not correct  
  else:
    #print(" u is " + u +" INCORRECT!")
    #print("check: " + check)
    temp_str = "(" + solution(v) + ")"
    # remove the first and the last character
    temp_u = u[1:len(u)-1]

    # change parentheses from ( to ) and ) to (
    for i in range(len(temp_u)):
      if temp_u[i] == "(":
        rev_str += ")"
      else:
        rev_str += "("

  #print("temp_str: " + temp_str + " rev_str: " + rev_str)

  answer = temp_str + rev_str
  #print("end! \n")
  return answer

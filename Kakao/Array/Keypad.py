
#2020 Kakao Internship Question1
#Keypad 

def distance(num, Lcur, Rcur, hand):
  
  Ldis = abs(num[0] - Lcur[0]) + abs(num[1] - Lcur[1])
  Rdis = abs(num[0] - Rcur[0]) + abs(num[1] - Rcur[1])

  if Ldis > Rdis:
    return (num,"R")
  
  elif Ldis < Rdis:
    return (num,"L")

  else:
    x = hand.upper()
    return (num, x[0])
  

def solution(numbers, hand):

  answer = ''
  dist = [(3,1),
        (0,0),(0,1),(0,2),
        (1,0),(1,1),(1,2),
        (2,0),(2,1),(2,2),
        (3,0),(3,2)]

  Lcur =  dist[10]
  Rcur =  dist[11]
  
  for i in range(len(numbers)):
    # if number is either 1,4, or 7
    if numbers[i]%3 == 1:
      Lcur = dist[numbers[i]]
      answer+= "L"
    
      #if number is either 3,6,9
    elif numbers[i]%3 == 0 and numbers[i] != 0:
      Rcur = dist[numbers[i]]
      answer+="R"
      # the numbers are either 2, 5, 8, 0
    else:
      tup = distance(dist[numbers[i]], Lcur, Rcur, hand)
      dir = tup[1]
      answer+=dir
      if dir == "L":
        Lcur = dist[numbers[i]]
      else:
        Rcur = dist[numbers[i]]
                    
  return answer


# Test Case
list1 = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]	#"right"	"LRLLLRLLRRL"
list2 = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]	#"left"	"LRLLRRLLLRR"
list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]	#"right"	"LLRLLRLLRL"

print(solution(list1,"right" ))
print(solution(list2, "left"))
print(solution(list3,"right" ))

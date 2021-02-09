# 2020 kakao coding test 
# question 3 - Key and Lock 


def rotation(old):

  #print("old")
  #print(old)

  # make an empy 2D array
  length = len(old)
  # new = [[9]*length]*length - this method changes everything at the same time
  new = [[3, 3, 3], [3, 3, 3], [3, 3, 3]]
  #print("new") 
  #print(new)

  if length >= 3:
    for i in range(length) :
      for j in range(length):
        # xx = j
        # yy = length -1 -i
        # new[xx][yy] = old[i][j]
        # print("i: "+ "{}".format(i)  + " j: " + "{}".format(j) + " xx: " + "{}".format(xx) 
        # + " yy: "+ "{}".format(yy) + " old: " +"{}".format(old[i][j]) + " new: " +"{}".format(new[xx][yy]))
        new[j][length - 1 - i] = old[i][j]
        
    #print("rotated: \n")
    #print(new)
    #print("done")
    return new
  else:
    print("not rotate!")


def check(key, lock, x, X, y, Y):
    
  # 새로운 가로, 세로
  width = X-x+1
  length = Y-y+1

  lenk = len(key)
  lenl = len(lock)

  # cut array(lock) is equal or less than key
  if width <= lenk and length <= lenk:
    # check all the possible cases in key
    for i in range(lenk):
      for j in range(lenk):

        flag = True

        # counter for i and j iteration 
        xcomp,ycomp = 0, 0
        
        # check each elements in lock
        for a in range(x, X+1):
          ycomp = 0
          for b in range(y, Y+1):

            # debugging purpose
            print("i: " + "{}".format(i) + " j: " + "{}".format(j) + " a: " + "{}".format(a) + " b: " + "{}".format(b) + " xcomp: " + "{}".format(xcomp) + " ycomp: " + "{}".format(ycomp) )


            # if chase and bump do not match
            if (lock[a][b] + key[i+xcomp][j+ycomp]) != 1:
              print("i: " + "{}".format(i) + " j: " + "{}".format(j) + " a: " + "{}".format(a) + " b: " + "{}".format(b) + " FALSE!")
              print("lock[a][b]: " + "{}".format(lock[a][b]) + "  key[i+xcomp][j+ycomp]: " + "{}".format( key[i+xcomp][j+ycomp]))
              print("xcomp: " + "{}".format(xcomp) + " ycomp: " + "{}".format(ycomp))
              flag = False
              break
            ycomp += 1
          xcomp += 1

          if flag == False:
            break
        
        if flag:
          print("Flag is true")
          answer = True
          return answer
  else:
    print("Condition not match, Lock is bigger than key")
  return False



def solution(key, lock):
    answer = True

    lenk = len(key)
    lenl = len(lock)

    print("lenk: " + "{}".format(lenk) + " lenl: " + "{}".format(lenl) )

    #small letter is min value, capital one is max
    x, X, y, Y = -1, -1, -1, -1

    for i in range(lenk):
      for j in range(lenk):
                
        if lock[i][j] == 0:
          print("i: " + "{}".format(i) + " j: " + "{}".format(j))
          # If default value is 0 then how can I determine it is the first item or not.
          if x < 0:
            x = i
          if i < x:
            x = i
          if i > X:
            X = i
          
          if y < 0:
            y = j
          if j < y:
            y = j
          if j > Y:
            Y = j
          #print("i: " + "{}".format(i) + " j: " + "{}".format(j) + " x: " + "{}".format(x) + " X: " + "{}".format(X) )


    print("AFTER Loop \n x: " + "{}".format(x) + " X: " + "{}".format(X) + " y: " + "{}".format(y) + " Y: " + "{}".format(Y) )
    
    
    # if this is true
    if check(key, lock, x, X, y, Y):
      print("FIRST!")
      return answer
    else:
      key = rotation(key)
      if check(key, lock, x, X, y, Y):
        print("Second!")
        return answer
      else:
        key = rotation(key)
        if check(key, lock, x, X, y, Y):
          print("Third!")
          return answer
        else:
          key = rotation(key)
          if check(key, lock, x, X, y, Y):
            print("Last!")
            return answer
          else:
            print("Dang, cannot open!")
            answer = False
            return answer
    


        
    

    
    print("HO!")
    #return answer


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]




print(solution(key, lock))


"""
new = rotation(key)
print("new array \n")
print(new)
print(check(new, lock, 1, 2, 1, 2))
"""

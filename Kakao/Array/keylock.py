# 2020 kakao coding test 
# question 3 - Key and Lock 


def rotation(old):

  print("old")
print(old)

  # make an empy 2D array
  length = len(old)
  # new = [[9]*length]*length - this method changes everything at the same time
  new = [[3, 3, 3], [3, 3, 3], [3, 3, 3]]
  print("new") 
  print(new)

  if length >= 3:
    for i in range(length) :
      for j in range(length):
        # xx = j
        # yy = length -1 -i
        # new[xx][yy] = old[i][j]
        # print("i: "+ "{}".format(i)  + " j: " + "{}".format(j) + " xx: " + "{}".format(xx) 
        # + " yy: "+ "{}".format(yy) + " old: " +"{}".format(old[i][j]) + " new: " +"{}".format(new[xx][yy]))
        new[j][length - 1 - i] = old[i][j]
        
    print("rotated: \n")
    #print(new)
    print("done")


def solution(key, lock):
    answer = True

    lenk = len(key)
    lenl = len(lock)

    #small letter is min value, capital one is max
    x, X, y, Y = 0, 0, 0, 0

    for i in range(lenk):
      for j in range(lenk):
        if lock[i][j] == 1:
          if i < x:
            x = i
          if i > X:
            X = i
          if j < y:
            y = j
          if j > Y:
            Y = j

    # 새로운 가로
    width = X-x+1
    length = Y-y+1

    # cut array(lock) is equal or less than key
    if width <= lenk and length <= lenk:
      # check all the possible cases in key
      for i in range(lenk):
        for j in range(lenk):

          flag = True
          
          # check each elements in lock
          for a in range(x, X+1):
            for b in range(y, Y+1):
              # if chase and bump are not matched
              if (lock[a][b] + key[i][j]) != 1:
                flag = False
                break
            if flag == False:
              break
          if flag:
            answer = True
            return answer


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

rotation(key)

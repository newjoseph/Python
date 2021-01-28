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
    return answer


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

rotation(key)

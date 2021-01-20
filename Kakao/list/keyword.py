# Keyword and query
# kakao coding test 2020 Q4

def solution(words, queries):
    answer = []

    # count is # of "?", freq is the frequency of the word in words
    count, freq, pivot = 0, 0, 0
    # flag to determine the front and last char are "?"
    front, last = False, False

    for str in enumerate(queries):
      #check the first and last char
      if str[0] == "?":
        front = True
      if str[-1] == "?":
        last = True
      # the whole string consists of "?"
      if front and last:
        count = len(str)
      # not all is "?"
      else:
        #front is "?"
        if front:
          for i in range(len(str)):
            if str[i] == "?":
              count += 1
            else:
              break
        # last is "?"
        else:
          for i in range(-1, -1 * len(str)-1 ,-1):
            if str[i] == "?":
              count += 1
            else:
              break
      pivot = count

      for w in enumerate(words):
        
        #the length of two comparing words is different
        if len(str) != len(w):
          continue
        # the length is same
        else:
          # everything is "?"
          if front and last:
            freq += 1
          # front is "?"
          elif front:
            if str[pivot:] == w[pivot:]:
              freq += 1
          # last is "?"
          else:
            if str[:-1*pivot] == w[:-1*pivot]:
              freq += 1

      answer.append(freq)
      freq, count = 0, 0
      front, last = False, False

    return answer

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words, queries))

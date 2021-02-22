
# need to add a case if there are more than one link

# 2019 kakao recruting #6

def solution(word, pages):

  url, body, link = "", "", ""
  n_link, score = 0
  first, last = 0, 0
  word = word.lower()


  for x in pages:
    print("----------------")
    #print(x)

    first = x.find("content=\"https:") + 17
    print("index: " + "{}".format(first))
    second = x.find("\"/>",first)
    url = x[first:second]
    print("URL: " + url)

    first = x.find("<body>") + 6
    print("index: " + "{}".format(first))
    second = x.find("</body>",first)
    body = x[first:second]
    print("BODY: " + body)
    
    


    second = body.find("<a href=\"https://")
    body_content = body[:second]
    print(body_content)

    first = second + 17
    print("index: " + "{}".format(first))
    second = body.find("\">",first)
    link = body[first:second].strip()
    print("LINK: " + link)
    


  
  answer = 0
  return answer


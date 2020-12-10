import urllib.request
import json
import re

client_id = "wGoF75Qd3oO99XtiGEqn"
client_pw = "7gKeaYrW0i"
URL = "https://openapi.naver.com/v1/search/shop?query="


def find_low_price(keyword):
    searchList = []
    encText = urllib.parse.quote(keyword)
    url = URL + encText + "&sort=asc"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_pw)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()

    if (rescode == 200):
        response_body = response.read().decode("utf-8")
        response = json.loads(response_body)
        response = response['items']

        for i in range(len(response)):
            temp = {
                    'title' : re.sub('<.+?>', '', response[i]['title'], 0, re.I|re.S),
                    'price' : response[i]['lprice'],
                    'link' : response[i]['link']
                    }

            searchList.append(temp)

    else:
        print("Error Code:" + rescode)


    return searchList


# while(True):
#     print(find_low_price(input("input : ")))

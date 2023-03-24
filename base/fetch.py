import requests

def fetch(Category):
    # category = 'technology'
    result = requests.get("https://inshorts.deta.dev/news?category="+Category)
    if result.status_code == 200:
        try:
            values = result.json()
            data = values['data']
            if data is not None:
                return data
            # for limit in range(len(data)):
            #     print(data[limit]['author'])
            #     print(data[limit]['content'])
        except:
            print("No Data Avilable")
    else:
        print('Something wnt wrong')
        return ("Error while fetching news may be internet connection is low")



# import requests


# res = 'politics'

# result = requests.get("https://inshorts.deta.dev/news?category="+res)

# if result.status_code == 200:
#     try:
#         values = result.json()
#         data = values['data']
#         print(len(data))
#         for limit in range(len(data)):
#             print(data[limit]['author'])
#             print(data[limit]['content'])
#     except:
#         print("Something Error")
# else:
#     print(result.status_code)
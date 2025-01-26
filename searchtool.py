# import search module from googlesearch
from googlesearch import search

# welcome message(optional)
print("welcome to googlesearch tool")

# query the input
query = input("search here : ")

# loop the query  in search and use start and stop to denote the number of results you need
# print result

for i in search(query, start=0, stop=5):
    print(i)
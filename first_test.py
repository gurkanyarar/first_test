import json
from pprint import pprint
from jsonschema import validate
count = 0 

with open('/Users/gurkan/Desktop/gurkanyarar/book_data-2.json') as data_file:    
	data = json.load(data_file)



schema_books = {
     "type" : "object",
     "books" : {
         "author" : {"type" : "string"},
         "id" : {"type" : "string"},
         "name": {"type": "string"},
     }
}

schema_authors = {
 	"type" : "object",
     "authors": {
     	"id": {"type" : "string"},
     	"name": {"type": "string"},
     }
}

for i in data["books"]:
 	validate(i,schema_books)
print("books schema validated")

for i in data["authors"]:
	validate(i,schema_authors)
print("authors schema validated")

authorMap = {} 				
for i in data["authors"]:
	authorMap[i["id"]] = i
print("authors added to dict")

print("hatali veri------------------------------------>    id     ---------------------->    name")
print("deneme")
for i in data["books"]:
	if(i["author"] not in authorMap):
		print(i)

import pickle
import json
d = dict(name = 'Martian',age = 18 , score = 99)
# f = open(r'F:\python\file.txt','wb')
# pickle.dump(d,f)
# f.close()

# f = open(r'F:\python\file.txt','rb')
# c = pickle.load(f)
# f.close()
# print(c)

# print(json.dumps(d))
json_str = '{"name": "Martian", "age": 18, "score": 99}'
print(json.loads(json_str))

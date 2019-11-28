import json
leaders={
    "Montegue": 5,
    "Bread": 1,
    "Jeffery": 3,
    "Haroon": 4,
    "Aggie": 2
}   

for key, value in sorted(leaders.items(),key=lambda kv: kv[1], reverse=True):
    print("%s: %s" % (key, value))

for x in leaders:
   print(leaders[x], x)
    
f=open("leaders.json", "w")

jsdata=json.dumps(leaders)

f.write(jsdata)

f.close()

f=open("leaders.json", "r")
leaderboard=f.read()
#print(leaderboard)

#print(type(leaderboard))
newleaders=json.loads(leaderboard)
print(type(newleaders), newleaders)
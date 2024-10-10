movie = {
    "name":"Star Wars",
    "episode":4,
    "year":"1977",
    "villian":['Vader', 'Tarkin'],
    "heros":['luke','leia','han','obi-wan']
}

print(movie['episode'])
episode_num = movie['episode']
print([movie["villian"]['1']])

search = "villian"
print(movie[search])

if "ships" in movie:
    print(movie["ships"])
else:
    print("We need to add ships.")
if "ships" not in movie:
    print("We need to add ships")

movie("name") == movie["name"]+' - a New Hope'
print(movie["name"])

movie['ships'] = ['Falcon','Star Destoryer','Death Star']

movie["heros"].append('Chewbacca')

print(movie)

for key in movie:
    print(key)

for key in movie:
    print(f'{movie[key]}')
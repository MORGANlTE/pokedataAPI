import flask
from replit import db, web
import json
import random
from requests_html import HTMLSession
from data import namelist, numberlist, listoftypes, statslist, informationlist, weaknesslist

print("Starting up Scraper...")

app = flask.Flask(__name__)


def return_pokemon_details(name):
  name = name.capitalize()
  original_string = name
  find_token = "-"
  if find_token in original_string:
      listje = list(original_string)
      listje[original_string.index("-")+1] = listje[original_string.index("-")+1].capitalize()
      name = "".join(listje)
  if name in namelist:
    pokemonnumber = 0
    numberinlist = 0
    
    #determine the number from this pokemon:
    for nam in namelist:
      if name == nam:
        pokemonnumber = numberlist[int(namelist.index(nam))]
        numberinlist = int(namelist.index(nam))
    pokemon_number = int(pokemonnumber)
    if pokemon_number < 10:
      pokemon_number = f"00{pokemon_number}"
    elif pokemon_number < 100:
      pokemon_number = f"0{pokemon_number}"
    
    types = []
    #list the types:
    for typ in listoftypes[numberinlist]:
      types.append(typ)
    
    print("Request made for", namelist[numberinlist])
    intj = 0
    stats = statslist[numberinlist]
    




    #make the image for this pokemon:
    imgsrc = f'https://assets.pokemon.com/assets/cms2/img/pokedex/detail/{pokemon_number}.png'
    #returndata that will be turned into json
    r = {"name": f"{namelist[numberinlist]}", 'number':f'{int(pokemon_number)}', "type" : f"{types}","image" : f"{imgsrc}", "stats": f"{stats}"}
    r = json.dumps(r)
    return f"{r}"
  else:
	  return "pokmon not found?"

@app.route("/")
def index():
  random_nr = random.randrange(1, 898)
  return return_pokemon_details(namelist[random_nr])


total = 0
for n in numberlist:
  total+=1
total = 0

for n in namelist:
  total+=1
@app.route('/dex/<name>')
def get_product(name):
  details = return_pokemon_details(name)
  if (details == "pokmon not found?"):
    return json.dumps("errorcode : 5")
  else:
    return details

print("API reloaded")
web.run(app)
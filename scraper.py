from requests_html import HTMLSession

class Scraper():
    def scrapedata(self, tag):
        url = f'https://api.pokemon.com/us/pokedex/{tag}'
        s = HTMLSession()
        r = s.get(url)
        qlist = []

        # region Finding number & descriptions
        pokemon_number = r.html.find("span.pokemon-number")
        nr = pokemon_number[2]
        nr = nr.text[1:len(nr.text)]
        female_descr = r.html.find("p.version-y")[0].text
        male_descr = r.html.find("p.version-x")[0].text
        qlist.append(nr)
        list_descr = [male_descr,female_descr]
        qlist.append(list_descr)
        # endregion

        # region Finding evo's
        evos = r.html.find("ul.evolution-profile")[0]
        evos = evos.find("li")
        evoslist = []
        for evo in evos:
            if evo.find("h3.match") != []:
                listje = []
                name = evo.find("h3.match")[0].text
                name_without_index = name[0:len(name) - 5]
                evo_number = name[len(name) - 4:len(name)]
                listje.append(name_without_index)
                listje.append(evo_number)
                evoslist.append(listje)
        qlist.append(evoslist)
        # endregion

        # region Finding types
        types = r.html.find("div.dtm-type")[0]
        types = types.find("li")
        typeslist = []
        for typ in types:
            typeslist.append(typ.text)
        qlist.append(typeslist)
        # endregion

        # region Finding weaknesses
        weaknesses = r.html.find("div.dtm-weaknesses")[0]
        weaknesses = weaknesses.find("li")
        weaknesslist = []
        for weakness in weaknesses:
            weaknesslist.append(weakness.text)
        qlist.append(weaknesslist)
        # endregion

        return qlist




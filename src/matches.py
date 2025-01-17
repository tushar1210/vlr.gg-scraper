import requests
import pprint
from bs4 import BeautifulSoup

pp = pprint.PrettyPrinter()

class Matches:
    """
    Gets all matches from VLR
    """


    def upcoming_matches() :
        """
        Upcoming matches from VLR homepage
        """

        URL = 'https://www.vlr.gg/'
        page = requests.get(URL)

        soup = BeautifulSoup(page.content, 'html.parser')
        
        matches = soup.find_all('div', class_="js-home-matches-upcoming")[0]
        cards = matches.find_all('div', class_="wf-card")[0]
        matchesDict = []

        matchLink = cards.find_all('a', class_="mod-match")
        for matchItem in matchLink:
            match = {}
            team1 = matchItem.find_all('div', class_="h-match-team-name")[0].get_text().strip()
            team2 = matchItem.find_all('div', class_="h-match-team-name")[1].get_text().strip()
            score1 = matchItem.find_all('div', class_="h-match-team-score")[0].get_text().strip()
            score2 = matchItem.find_all('div', class_="h-match-team-score")[1].get_text().strip()
            status = matchItem.find_all('div', class_="h-match-eta")[0].get_text().strip()
            link = matchItem.get('href')
            id = link.split("/")[0]
            match["team1"] = team1
            match["team2"] = team2
            match["score1"] = score1
            match["score2"] = score2
            match["status"] = status
            match["link"] = link
            match["id"] = id
            matchesDict.append(match)
        pp.pprint(matchesDict)
        return matchesDict


    def recent_matches():
        """
        Recent matches from VLR homepage
        """

        URL = 'https://www.vlr.gg/'
        page = requests.get(URL)

        soup = BeautifulSoup(page.content, 'html.parser')

        matches = soup.find_all('div', class_="js-home-matches-completed")[0]
        cards = matches.find_all('div', class_="wf-card")[0]
        matchesDict = []

        matchLink = cards.find_all('a', class_="mod-match")
        for matchItem in matchLink:
            match = {}
            team1 = matchItem.find_all('div', class_="h-match-team-name")[0].get_text().strip()
            team2 = matchItem.find_all('div', class_="h-match-team-name")[1].get_text().strip()
            score1 = matchItem.find_all('div', class_="h-match-team-score")[0].get_text().strip()
            score2 = matchItem.find_all('div', class_="h-match-team-score")[1].get_text().strip()
            status = matchItem.find_all('div', class_="h-match-eta")[0].get_text().strip()
            link = matchItem.get('href')
            id = link.split("/")[0]
            match["team1"] = team1
            match["team2"] = team2
            match["score1"] = score1
            match["score2"] = score2
            match["status"] = status
            match["link"] = link
            match["id"] = id
            matchesDict.append(match)
        pp.pprint(matchesDict)
        return matchesDict

    def match_schedule():
        """
        Full schedule of matches from VLR Matches page
        """

        URL = 'https://www.vlr.gg/matches'
        page = requests.get(URL)

        soup = BeautifulSoup(page.content, 'html.parser')
        schedule = soup.find_all('div', class_="col mod-1")[0]
        dates = schedule.find_all('div', class_="wf-label")
        cards = schedule.find_all('div', class_="wf-card")
        matchesDict = []
        for key in dates:
            for value in cards:
                matchLink = value.find_all('a', class_="match-item")
                for matchItem in matchLink:
                    match = {}
                    time = matchItem.find_all('div', class_="match-item-time")[0].get_text().strip()
                    team1 = matchItem.find_all('div', class_="match-item-vs-team-name")[0].get_text().strip()
                    team2 = matchItem.find_all('div', class_="match-item-vs-team-name")[1].get_text().strip()
                    score1 = matchItem.find_all('div', class_="match-item-vs-team-score")[0].get_text().strip()
                    score2 = matchItem.find_all('div', class_="match-item-vs-team-score")[1].get_text().strip()
                    status = matchItem.find_all('div', class_="ml")[0].get_text().strip()
                    eventTitle = matchItem.find_all('div', class_="match-item-event")[0].get_text().strip().split("\t")[-1]
                    eventStage = matchItem.find_all('div', class_="match-item-event-series")[0].get_text().strip()
                    icon = matchItem.find_all('div', class_="match-item-icon")[0].find('img')['src']
                    link = matchItem.get('href')
                    id = link.split("/")[1].split("/")[0]
                    match["date"] = key.get_text().strip()
                    match["team1"] = team1
                    match["team2"] = team2
                    match["score1"] = score1
                    match["score2"] = score2
                    match["status"] = status
                    match["link"] = link
                    match["id"] = id
                    match["event"] = { "name" : eventTitle, "stage": eventStage, "icon" : icon }
                    matchesDict.append(match)
                cards.remove(value)
                break
        return matchesDict



    def match_results():
        """
        Results of recent matches from VLR homepage
        """
        URL = 'https://www.vlr.gg/matches/results'
        page = requests.get(URL)

        soup = BeautifulSoup(page.content, 'html.parser')
        schedule = soup.find_all('div', class_="col mod-1")[0]
        dates = schedule.find_all('div', class_="wf-label")
        cards = schedule.find_all('div', class_="wf-card")
        matchesDict = []
        for key in dates:
            for value in cards:
                matchLink = value.find_all('a', class_="match-item")
                for matchItem in matchLink:
                    match = {}
                    time = matchItem.find_all('div', class_="match-item-time")[0].get_text().strip()
                    team1 = matchItem.find_all('div', class_="match-item-vs-team-name")[0].get_text().strip()
                    team2 = matchItem.find_all('div', class_="match-item-vs-team-name")[1].get_text().strip()
                    score1 = matchItem.find_all('div', class_="match-item-vs-team-score")[0].get_text().strip()
                    score2 = matchItem.find_all('div', class_="match-item-vs-team-score")[1].get_text().strip()
                    status = matchItem.find_all('div', class_="ml")[0].get_text().strip()
                    eventTitle = matchItem.find_all('div', class_="match-item-event")[0].get_text().strip().split("\t")[-1]
                    eventStage = matchItem.find_all('div', class_="match-item-event-series")[0].get_text().strip()
                    icon = matchItem.find_all('div', class_="match-item-icon")[0].find('img')['src']
                    link = matchItem.get('href')
                    id = link.split("/")[1].split("/")[0]
                    match["date"] = key.get_text().strip()
                    match["team1"] = team1
                    match["team2"] = team2
                    match["score1"] = score1
                    match["score2"] = score2
                    match["status"] = status
                    match["link"] = link
                    match["id"] = id
                    match["event"] = { "name" : eventTitle, "stage": eventStage, "icon" : icon }
                    matchesDict.append(match)
                cards.remove(value)
                break
        return matchesDict



    def match(id) :
        """
        Details of a particular match from VLR
        """

        URL = 'https://www.vlr.gg/' + id
        page = requests.get(URL)

        soup = BeautifulSoup(page.content, 'html.parser')
        matchHeader = soup.find_all("div", class_="match-header-vs")[0]
        team1name = matchHeader.find_all("div", class_="wf-title-med")[0].get_text().strip()
        team1img = matchHeader.find_all("a", class_="match-header-link")[0].find('img')['src']
        team2name = matchHeader.find_all("div", class_="wf-title-med")[1].get_text().strip()
        team2img = matchHeader.find_all("a", class_="match-header-link")[1].find('img')['src']
        score = matchHeader.find_all("div", class_="match-header-vs-score")[0].find_all("div", class_="js-spoiler")[0].get_text().replace('\n', '').replace('\t', '')
        note = soup.find_all("div", class_="match-header-note")[0].get_text().strip()
        team1 = { 'name' : team1name, 'img' : "https:"+team1img }
        team2 = { 'name' : team2name, 'img' : "https:"+team2img}
        teams = [team1, team2]
        stats = soup.find_all("div", class_="vm-stats")[0]
        maps = []
        for map in stats.find_all("div", class_="vm-stats-gamesnav-item"):
            name = map.get_text().strip().replace('\n', '').replace('\t', '')
            name = ''.join(i for i in name if not i.isdigit())
            id = map['data-game-id']
            maps.append({'name': name, 'id': id})

        mapStats = stats.find_all("div", class_="vm-stats-game")
        mapName = ''
        team1Obj = {}
        team2Obj = {}
        mapData = []
        for map in mapStats:
            id = map['data-game-id']
            if id != 'all':
                score1 = map.find_all("div", class_="score")[0].get_text().strip()
                team1 =  map.find_all("div", class_="team-name")[0].get_text().strip()
                score2 = map.find_all("div", class_="score")[1].get_text().strip()
                team2 =  map.find_all("div", class_="team-name")[1].get_text().strip()
                print([map1['name'] for map1 in maps if map1['id'] == id][0])
                print(team1, score1)
                print(team2, score2)
                mapName = [map1['name'] for map1 in maps if map1['id'] == id][0]
                team1Obj = {'name': team1, 'score': score1 }
                team2Obj = {'name': team2, 'score': score2 }
                print('')
            else:
                print([map1['name'] for map1 in maps if map1['id'] == id][0])
                mapName = [map1['name'] for map1 in maps if map1['id'] == id][0]
                team1Obj = {}
                team2Obj = {}
                print('')
            scoreboard = map.find_all('tbody')
            members = []

            maprounds = map.find_all("div", class_="vlr-rounds-row-col")[1:]
            id = map['data-game-id']
            rounds = []
            if id != 'all':
                prev = [0,0]
                for round in maprounds:
                    current = []
                    roundWinner = ""
                    if len(round.find_all("div", class_="rnd-currscore")) > 0:
                        roundNum = round.find_all("div", class_="rnd-num")[0].get_text().strip()
                        roundScore = round.find_all("div", class_="rnd-currscore")[0].get_text().strip()
                        print(roundScore)
                        if roundScore != "":
                            current = [int(i) for i in roundScore.split("-")]
                            if prev[0] == current[0]:
                                roundWinner = "team2"
                            elif prev[1] == current[1]:
                                roundWinner = "team1"
                            prev = current
                        if len(round.find_all("div", class_="mod-win")) > 0:
                            raw = round.find_all("div", class_="mod-win")[0].find('img')['src']
                            if 'mod-t' in round.find_all("div", class_="mod-win")[0].get('class'):
                                side = "attack"
                            elif 'mod-ct' in round.find_all("div", class_="mod-win")[0].get('class'):
                                side = "defense"
                            winType = ''
                            if 'elim' in raw:
                                winType = 'Elimination'
                            elif 'time' in raw:
                                winType = 'Time out'
                            elif 'defuse' in raw:
                                winType = 'Defused'
                            elif 'boom' in raw:
                                winType = 'Spiked out'
                            else:
                                winType = 'Not Played'
                        else:
                            winType = 'Not Played'
                        print(roundNum, roundScore, winType)
                    rounds.append({ 'roundNum': roundNum, 'roundScore': roundScore, 'winner': roundWinner, 'side': side, 'winType': winType })
                        

            for row in scoreboard:
                for team in row.find_all('tr'):
                    name = team.find_all('td', class_='mod-player')[0].find_all('div', class_='text-of')[0].get_text().strip()
                    teamName = team.find_all('td', class_='mod-player')[0].find_all('div', class_='ge-text-light')[0].get_text().strip()
                    agents = []
                    ACS = team.find_all('td', class_='mod-stat')[0].find_all('span', class_='stats-sq')[0].get_text().strip()
                    kills = team.find_all('td', class_='mod-vlr-kills')[0].find_all('span', class_='stats-sq')[0].get_text().strip()
                    deaths = team.find_all('td', class_='mod-vlr-deaths')[0].find_all('span', class_='stats-sq')[0].get_text().strip().replace('/', '')
                    assists = team.find_all('td', class_='mod-vlr-assists')[0].find_all('span', class_='stats-sq')[0].get_text().strip()
                    hs = team.find_all('td', class_='mod-stat')[6].find_all('span', class_='stats-sq')[0].get_text().strip()
                    agentHTML = team.find_all('td', class_='mod-agents')[0].find_all('img')
                    for agent in agentHTML:
                        title = agent['title']
                        src = agent['src']
                        acs = ACS
                        agents.append({'name' : title, 'img': src})
                    member = {'name': name, 'team': teamName, 'agents': agents, 'acs': acs, 'kills' : kills, 'deaths': deaths, 'assists': assists, 'HSpercent': hs}
                    members.append(member)
                    print(name, teamName, agents)
                print('')
            mapData.append([{'map': mapName, 'teams': [team1Obj, team2Obj], 'members': members, 'rounds': rounds}])

        return {'teams': teams, 'score': score, 'note': note, 'data': mapData }

    

# match("16990")

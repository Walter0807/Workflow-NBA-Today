#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Author = Walter0108
import sys
from workflow import Workflow, ICON_WEB, web
import time
import datetime
import requests




def getMatch(wf):
    headers = {
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4,mt;q=0.2',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
    }
    Date_LA = (datetime.datetime.utcnow() - datetime.timedelta(hours = 7)).strftime("%m/%d/%Y")
    baseUrl = 'https://stats.nba.com/stats/scoreboard/'
    try:
        a = int(wf.args[0])
    except ValueError:
        a = 0
    params = dict(GameDate=Date_LA, LeagueID = "00", DayOffset=a )
    r = requests.get(baseUrl, headers=headers, params=params)
    r.raise_for_status()
    resultSets = r.json()['resultSets']
    GameHeader = resultSets[0]['rowSet']
    LineScore = resultSets[1]['rowSet']
    MatchesNum = len(GameHeader)
    for idx in range(MatchesNum):
        State = GameHeader[idx][4]  # 4th Qtr/Final
        Remain = GameHeader[idx][10]  # 7:24
        Begin = GameHeader[idx][9]
        Team1 = idx * 2
        Team2 = Team1 + 1
        Iconpath = "icons/" + LineScore[Team2][5] +".png"
        if (Begin!=0):
            title = LineScore[Team2][4] + '(' + LineScore[Team2][6] + ')  ' + str(LineScore[Team2][21]) + ':' + str(
                LineScore[Team1][21]) + " " + LineScore[Team1][4] + '  (' + LineScore[Team1][
                        6] + ')' + '  ' + State + Remain
            Pct11 = str(round(float(LineScore[Team1][22]) * 1000) / 10.0) + '%'
            Pct12 = str(round(float(LineScore[Team1][24]) * 1000) / 10.0) + '%'
            Pct13 = str(round(float(LineScore[Team1][23]) * 1000) / 10.0) + '%'
            Pct21 = str(round(float(LineScore[Team2][22]) * 1000) / 10.0) + '%'
            Pct22 = str(round(float(LineScore[Team2][24]) * 1000) / 10.0) + '%'
            Pct23 = str(round(float(LineScore[Team2][23]) * 1000) / 10.0) + '%'
            T1 = Pct11 + '+' + Pct12 + '+' + Pct13 + ' ' + str(LineScore[Team1][26]) + 'Reb ' + \
                 str(LineScore[Team1][25]) + 'Ast ' + str(LineScore[Team1][25]) + 'To'
            T2 = Pct21 + '+' + Pct22 + '+' + Pct23 + ' ' + str(LineScore[Team2][26]) + 'Reb ' + \
                 str(LineScore[Team2][25]) + 'Ast ' + str(LineScore[Team2][25]) + 'To'
            detail = T2 + ' | ' + T1
            wf.add_item(title, detail, icon = Iconpath, arg = GameHeader[idx][2], uid = GameHeader[idx][2], valid=True)
        else:
            title = LineScore[Team2][4] + '(' + LineScore[Team2][6] + ') VS ' + LineScore[Team1][4] + '  (' + LineScore[Team1][
                        6] + ')' + '  ' + State + Remain
            wf.add_item(title, icon = Iconpath)
    wf.send_feedback()

if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(getMatch))
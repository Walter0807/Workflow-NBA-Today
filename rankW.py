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
    params = dict(GameDate=Date_LA, LeagueID = "00", DayOffset=0)
    r = requests.get(baseUrl, headers=headers, params=params)
    r.raise_for_status()
    westrank = r.json()["resultSets"][5]["rowSet"]
    for i in range(15):
        title = str(i+1) + " " + westrank[i][5]
        Detail = str(westrank[i][7])+ "-" + str(westrank[i][8]) + " (" + str(westrank[i][9]) +")"
        Iconpath = "icons/" + westrank[i][5] + ".png"
        wf.add_item(title, Detail, icon = Iconpath)
    wf.send_feedback()

if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(getMatch))
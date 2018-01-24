# Workflow-NBA-Today

A Alfred workflow for quickly checking NBA schedules, game results and standings.

NBA新赛季开始了。
作为高频需求，希望能够将查看赛程赛果结合到效率神器Alfred的Workflow中。
## 功能
![](nbaalfredworkflow1.jpg)
主菜单。Watch Games直达企鹅TV英文原声和腾讯体育直播页面。
![](v2-82475c23792d6d62a35ad899da47258c_r.jpg)
加载当天赛程赛果
![](v2-ad0353d57948d86ad8bdc0bb0e338d57_r.jpg)
加载当天赛程赛果
![](v2-24b875d53a21c469242332d7e4215627_r.jpg)
往前滑动一天。比赛中/结束后可点进数据统计页面。
![](v2-ee7f9b6de984bd2409df99af55e6d0df_hd.jpg)
往后滑动一天。比赛未开始，显示比赛时间。
![](v2-75f1a58fbae09fcd20cf7eb1f40ecb9a_r.jpg)
东部排名
![](v2-6225bd3640778fcfd52a277c19e16845_r.jpg)
西部排名

## 实现
* API来自stats.nba.com
* 用了[workflow-alfred python库](https://github.com/deanishe/alfred-workflow)

## 关于时间
1. API以比赛当地日期为查询参数，拿当前日期减一是一个在国内可以用上的方法
2. 考虑到可能会在其他时区使用，我直接把当前时间转到美西（LA）时间算的日期
3. 所以在北京的夜晚，直接查询看到的是第二天的赛程。
4. 未开始的比赛默认的是美东时间（ET），对于北京时间只是把AM/PM换了一下

## 下载
* [Walter0807/Workflow-NBA-Today](https://github.com/Walter0807/Workflow-NBA-Today/blob/master/NBA%20today.alfredworkflow)
* 依赖requests库，可以用sudo pip2 install requests 指令安装

## 更新
1. 目前对于进行中的比赛没有直达直播间的操作（TX没给开API）。未来如果要做的话，可能会解析一下TX的页面代替官方的API。
2. 更新会在这里Update。
3. 2017.10.22 Minor bugs fixes

## References
* http://johnho.cn/2016/09/12/Alfredworkflow2/
* https://github.com/deanishe/alfred-workflow
* https://github.com/seemethere/nba_py/wiki/stats.nba.com-Endpoint-Documentation

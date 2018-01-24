# Workflow-NBA-Today

A Alfred workflow for quickly checking NBA schedules, game results and standings.<br><br>

NBA新赛季开始了。
作为高频需求，希望能够将查看赛程赛果结合到效率神器Alfred的Workflow中。

详细介绍http://39.107.114.234/nbaalfredworkflow/


![](https://pic4.zhimg.com/v2-f193ccea9ba7ab7f67872e52f8be56d0_r.jpg)

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

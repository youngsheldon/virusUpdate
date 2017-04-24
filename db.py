#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: anchen
# @Date:   2017-04-05 16:13:52
# @Last Modified by:   anchen
# @Last Modified time: 2017-04-24 11:51:36
import os 

def sql_exec(sql):
    sql_exe = ''
    if isinstance(sql,list):
        for v in sql:
            print(v)
            sql_exe += v + '\n'
        out = 'sqlplus smmchunan/A1234567@SMMC <<!\n' + sql_exe + 'exit;\n' + '!\n'
    else:
        out = 'sqlplus smmchunan/A1234567@SMMC <<!\n' + sql + '\n' + 'exit;\n' + '!\n'
    os.system(out)

# call sp_add_virus_list(20,0,0,'http://d1.apk8.com:8020/game/feiqinzoushoulaohuji.apk','','9877ee2c2ab777eb3457752ad7e30c96','由病毒库自动更新程序添加');
url1 = 'http://d1.apk8.com:8020/game/feizoushoulaohuji.apk'
md51 = '87f066f5d5f83480259e97d13dfec057'
url2 = 'http://a.gdown.du.com/data/wisegame/ba594e74e89f3f23/chewangzhiwang_1585.apk?from=a1101'
md52 = 'be6209b8363aa744b4daf50ef59c9025'
remark = '由病毒库自动更新程序添加'
sql1 = 'call sp_add_virus_list(20,0,0,\'%s\',\'%s\',\'%s\',\'%s\');' % (url1,' ',md51,remark)
sql2 = 'call sp_add_virus_list(20,0,0,\'%s\',\'%s\',\'%s\',\'%s\');' % (url2,' ',md52,remark)
sql = [sql1,sql2]
sql_exec(sql)
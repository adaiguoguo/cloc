# -*- coding:utf-8 -*-
import os
import config
import json
from db_utils import Utils
import clone
import time

if __name__ == "__main__":
    clone.git_clone(config.CLOC_LABEL)
    os.system("{0} {1} -json --out {2}".format(config.CLOC_RUN_PATH,config.CODE_EXPORT,config.JSON_REPORT))
    with open(config.JSON_REPORT) as data_file:
        data = json.load(data_file)
        u = Utils()
        c = u.cursor()
        for key, value in data.items():
            if key != "SUM" and key != "header":
                sql = """insert into code_cloc
                    (createdtime,lang,files,`lines`,label)
                  values ('%s','%s',%d,%d,'%s')""" % (time.strftime('%Y-%m-%d %H:%M:%S'),key,value["nFiles"],value["code"],config.CLOC_LABEL)
                print sql
                c.execute(sql)
        c.close()
        u.conn.commit()
    os.remove(config.CODE_EXPORT)


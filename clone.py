# -*- coding:utf-8 -*-
import os
import config
import glob
def git_clone(depository):
    os.rmdir(config.CODE_EXPORT)
    os.mkdir(config.CODE_EXPORT)
    if depository == "Github":
        newestfolder = max(glob.iglob("%s*"%(config.CODE_PATH)), key=os.path.getctime)
        os.chdir(config.CODE_EXPORT)
        os.system("find %s -maxdepth 1 -name *.git | xargs -n1 -P8 git clone --depth=1 --branch=master"%(newestfolder))
    elif depository == "Gitlab":
        os.mkdir(config.CODE_EXPORT)
        os.chdir(config.CODE_PATH)
        os.system("find . -maxdepth 2 -name '*.git' | xargs -P8 -n1 -I [] git clone --depth=1 --branch=master [] %s/[]"%(config.CODE_EXPORT))



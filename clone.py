# -*- coding:utf-8 -*-
import os
import config
import glob
import shutil
def git_clone(depository):
    if depository == "Github":
        newestfolder = max(glob.iglob("%s*"%(config.CODE_PATH)), key=os.path.getctime)
        os.chdir(config.CODE_EXPORT)
        os.system("find %s -maxdepth 1 -name *.git | xargs -n1 -P8 git clone --depth=1 --branch=master"%(newestfolder))
    elif depository == "Gitlab":
        os.mkdir(config.CODE_EXPORT)
        os.chdir(config.CODE_PATH)
        os.system("find . -maxdepth 2 -name '*.git' | xargs -P8 -n1 -I [] git clone --branch=master [] %s/[]"%(config.CODE_EXPORT))



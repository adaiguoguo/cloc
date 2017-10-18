# -*- coding:utf-8 -*-
CLOC_LABEL = "Gitlab"
CODE_PATH = "/data/gitlab/git-data/repositories"
CODE_EXPORT = "/data/code_export/"
JSON_REPORT = "{0}{1}.json".format(CODE_EXPORT,CLOC_LABEL)
CLOC_RUN_PATH = "/data/cloc-1.66.pl"

from deploy_config import *
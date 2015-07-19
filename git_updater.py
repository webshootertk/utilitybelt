#!/bin/python

import os
from git import Repo
from remote_model.github import GithubModel
from  local_settings import *


for org in organizations:
    current_org = "/orgs/" + org + "/repos"
    current_directory = base_directoy + org
    repos = GithubModel(current_org)

    for repo in repos:
        current_repo = os.path.join(current_directory, repo['name'])
        if os.path.isdir(current_repo):
            print 'fetching: ' + current_repo
            this_repo = Repo(current_repo)
            this_repo.git.fetch('--all')
        else:
            #clone repo
            print 'cloning: ' current_repo
           

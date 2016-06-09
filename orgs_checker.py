#!/usr/local/bin/python2.7

from github import Github
import argparse
import os

def repo_count(repo_list):
    count = 0
    for repo in repo_list:
        count += 1
    return count


def repo_print(repo_list):
    for repo in repo_list:
        print repo.name


def get_user(account):
    info_file = open(account)
    user = info_file.readlines()
    info_file.close()
    return user


def get_organizations(organizations):
    info_file = open(organizations)
    orgs = info_file.readlines()
    info_file.close()
    return orgs


def org_checker(account, organizations):
    user_info = get_user(account)
    user = user_info[0].strip()
    pw = user_info[1].strip()
    g = Github(user, pw)
    orgs_list = get_organizations(organizations)

    #I need it for organizations not users...
    #for orgs.strip() in orgs_list
    for org in orgs_list:
        repo_list = g.get_organization(org.strip()).get_repos();
        print "%s has %d repos" % (org.strip(), repo_count(repo_list))
        repo_print(repo_list)
        print ""

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="prints all repos")
    parser.add_argument("account", help="path to file with github username and password")
    parser.add_argument("organizations", help="path to file with list of organizations")

    args = parser.parse_args()

    if not os.path.exists(args.account):
        stderr.write("file %s not found." % args.account)
        exit()

    if not os.path.exists(args.organizations):
        stderr.write("file %s not found." % args.organizations)
        exit()

    if org_checker(args.account, args.organizations):
        print "Error"
    else:
        print "Done"



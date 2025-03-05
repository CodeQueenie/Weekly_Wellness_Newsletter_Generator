#!/bin/env powershell

# This script rewrites the Git history to change the author of all commits
# from "QueenieCoder" to "Nicole LeGuern"

git filter-branch --env-filter '
if [ "$GIT_COMMITTER_NAME" = "QueenieCoder" ]
then
    export GIT_COMMITTER_NAME="Nicole LeGuern"
    export GIT_COMMITTER_EMAIL="148448915+CodeQueenie@users.noreply.github.com"
fi
if [ "$GIT_AUTHOR_NAME" = "QueenieCoder" ]
then
    export GIT_AUTHOR_NAME="Nicole LeGuern"
    export GIT_AUTHOR_EMAIL="148448915+CodeQueenie@users.noreply.github.com"
fi
' --tag-name-filter cat -- --branches --tags

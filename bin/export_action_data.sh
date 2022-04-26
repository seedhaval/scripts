#!/bin/bash
cd /storage/internal/data/
rm Actions.tsv
sqlite3 actions.db <<eof
.headers on
.mode tabs
.output Actions.tsv 
select * from action_data;
eof

#!/bin/bash
cd /storage/internal/data/
rm actions.db
sqlite3 actions.db <<eof
.mode tabs
.import Actions.tsv action_data
eof

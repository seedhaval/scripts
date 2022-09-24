#!/bin/bash
cd /storage/internal/data/
sqlite3 actions.db <<eof
alter table action_data add "${1}" text;
update action_data set "${1}" = '01/04/2022';
.schema
eof

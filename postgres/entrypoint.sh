#!/bin/sh
export PGPASSWORD='postgres' 
# psql -h 'server name' -U 'user name' -d 'base name' -c 'command'
#su - postgres -c "export PGPASSWORD='postgres'; psql -h db -U postgres -p 5432 -d postgres -f /src/sql/dbcreate.sql --no-password ;"  
su - postgres -c "psql -d postgres -f /src/sql/dbcreate.sql --no-password ;"  
su - postgres -c "pg_restore -d wagtailmonsitedb /src/wagtailmonsitedump.db --no-password ;";  bash-5.0# 

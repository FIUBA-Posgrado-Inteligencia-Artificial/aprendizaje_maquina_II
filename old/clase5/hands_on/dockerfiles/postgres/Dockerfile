FROM postgres:latest

# The official recommendation for creating multiple databases is as follows:
# If you would like to do additional initialization in an image derived from this one, add one or more
# *.sql, *.sql.gz, or *.sh scripts under /docker-entrypoint-initdb.d (creating the directory if necessary).
# After the entrypoint calls initdb to create the default postgres user and database, it will run any *.sql files
# and source any *.sh scripts found in that directory to do further initialization before starting the service.
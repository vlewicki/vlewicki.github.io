```
docker exec -t <container_name> pg_dump -U <username> -d <database_name> | gzip > backup.sql.gz
rclone copy backup.sql.gz gdrive_encrypted:backups/
# Delete local file after upload
rm backup.sql.gz
```

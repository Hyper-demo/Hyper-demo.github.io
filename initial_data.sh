#!/usr/bin/env bash

## database create and migration
flask db init
flask db migrate
flask db upgrade

## initial records to database   
sqlite3 data-dev.sqlite -cmd ".mode csv" \
"delete from amazon_product" \
".import db/amazon_product.csv amazon_product" \
"delete from amazon_review" \
".import db/amazon_review.csv amazon_review" \


# username for log in is admin; password is 1234567
# "delete from system_user" \
# "insert into system_user values(1,'admin','pbkdf2:sha256:260000\$cWVvrPVgMXzn8I6E\$9cf23719edcb252f928ef52fe95fd6ca94beb5c50580e088e789cb01c1204d0b')" \


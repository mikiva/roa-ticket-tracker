#!/bin/bash
docker run -d --name mongo \
--rm \
-p 27017:27017 \
-e MONGO_INITDB_ROOT_USERNAME=roa \
-e MONGO_INITDB_ROOT_PASSWORD=roa \
-e MONGO_INITDB_DATABASE=roa \
-v $(pwd)/mongo-init.js:/docker-entrypoint-initdb.d/mongo-init.js:ro \
mongo
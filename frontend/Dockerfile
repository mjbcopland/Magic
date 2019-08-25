from node:10-alpine

workdir /app

copy package.json .

copy package-lock.json .

run npm ci

copy src .

cmd npm run build

entrypoint []

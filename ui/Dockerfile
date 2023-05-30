from node:latest as SPA_BUILDER
WORKDIR /app
COPY package*.json .
RUN CI=false npm install
COPY . .

RUN npm run build


FROM nginx

WORKDIR /app
COPY --from=SPA_BUILDER /app/dist /app


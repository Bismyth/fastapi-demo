FROM node:20.11.1 as NODE_BUILDER
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY tsconfig.app.json tsconfig.json tsconfig.node.json vite.config.ts index.html env.d.ts ./
COPY src ./src
COPY public ./public
RUN npm run build

FROM nginx:1
COPY --from=NODE_BUILDER /app/dist/ /usr/share/nginx/html
COPY ./nginx.conf /etc/nginx/conf.d/default.conf
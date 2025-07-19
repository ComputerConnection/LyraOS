# lyra-stack/Dockerfile  (DEV)
FROM node:18

WORKDIR /app

# Copy only package manifests first (leverages build cache)
COPY package*.json ./
RUN npm install --production

# Copy source
COPY . .

EXPOSE 8081
CMD ["node", "index.js"]

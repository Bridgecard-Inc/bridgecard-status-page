# base image
FROM node:18.17-alpine

# Create and change to the app directory.
WORKDIR /usr/app

# Copy application dependency manifests to the container image.
# A wildcard is used to ensure copying both package.json AND package-lock.json (when available).
# Copying this first prevents re-running npm install on every code change.
COPY frontend/ .

# Install production dependencies.
RUN yarn install --ignore-engines

# Copy local code to the container image.

ENV NEXT_PUBLIC_BRIDGECARD_STATUS_PAGE_BACKEND_HOST bridgecard-status-page-backend

ENV NEXT_PUBLIC_BRIDGECARD_STATUS_PAGE_BACKEND_PORT 8080

RUN yarn build

EXPOSE 8000

# Run the web service on container startup. 
CMD [ "yarn", "start", "-p", "8000"]


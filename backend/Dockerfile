# Use an official lightweight Node.js image.
FROM node:20-alpine

# Create and set the working directory.
WORKDIR /usr/src/app

# Copy package.json and package-lock.json (if available)
COPY package*.json ./

# Install backend dependencies.
RUN npm ci --omit=dev

# Copy the rest of your backend source code.
COPY . .

# Expose the port that your backend listens on (e.g., 5000)
EXPOSE 5000

# Start the backend server.
CMD ["node", "server.js"]

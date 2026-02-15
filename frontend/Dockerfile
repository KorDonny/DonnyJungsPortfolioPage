# ---------- deps ----------
FROM node:20-alpine AS deps
WORKDIR /app

# package-lock.json을 쓰면 npm ci가 가장 안정적
COPY package.json package-lock.json ./
RUN npm ci

# ---------- build ----------
FROM node:20-alpine AS builder
WORKDIR /app

COPY --from=deps /app/node_modules ./node_modules
COPY . .

# Next build
RUN npm run build

# ---------- run ----------
FROM node:20-alpine AS runner
WORKDIR /app

ENV NODE_ENV=production
ENV PORT=3000

# 필요하면 런타임에서 읽을 env는 App Runner에서 주입
# (예: API_BASE_URL)

# 실행에 필요한 파일만 복사
COPY --from=builder /app/.next ./.next
COPY --from=builder /app/public ./public
COPY --from=builder /app/package.json ./package.json
COPY --from=builder /app/node_modules ./node_modules

EXPOSE 3000
CMD ["npm", "run", "start"]

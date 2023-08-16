FROM denoland/deno:alpine-1.36.1

EXPOSE 8080

WORKDIR /app
USER deno

COPY src/deps.ts .
RUN deno cache deps.ts

COPY . .
RUN deno cache src/main.ts

CMD ["run", "--allow-all", "src/main.ts"]

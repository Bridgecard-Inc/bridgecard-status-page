# Build stage
FROM golang:1.19-alpine3.16 AS builder
WORKDIR /app
COPY monitor/ .
RUN go build -o main cmd/main.go

# Run stage
FROM alpine:3.16
WORKDIR /app
COPY --from=builder /app/main .

CMD [ "/app/main" ]

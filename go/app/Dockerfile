FROM golang:1.15.3-alpine

RUN apk update && apk upgrade && \
    apk add --no-cache bash git openssh

WORKDIR /app

COPY go.mod ./

RUN go mod download

RUN go get github.com/lib/pq
RUN go get -u github.com/gocarina/gocsv
RUN go get github.com/klassmann/cpfcnpj
RUN go get github.com/gin-gonic/gin github.com/jinzhu/gorm
COPY . .
RUN go build -o main .

# Expose port 8080 to the outside world
EXPOSE 80

# Run the executable
CMD ["./main"]
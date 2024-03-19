.DEFAULT_GOAL := clean

.PHONY:fmt vet build run clean
fmt:
	go fmt ./...

vet: fmt
	go vet ./...

build: vet
	go build

run: build
	./HelloWorld

clean: run
	go clean
.DEFAULT_GOAL := clean

.PHONY:fmt vet build run clean
fmt:
	go fmt ./...

vet: fmt
	go vet ./...

build: vet
	go build

run: build
	./Chapter3

clean: run
	go clean
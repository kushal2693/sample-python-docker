name: run-app

on: [push, pull_request]

jobs:
  run-app:
    runs-on: ubuntu-latest
    container:
      image: ubuntu:latest
    run: sh main.sh

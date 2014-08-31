@echo off
echo "Starting redis..."
start E:\apps\redis\redis64-2.8.9\redis-server.exe
echo "Redis Server launched"
start E:\apps\redis\redis64-2.8.9\redis-cli.exe
echo "Redis client started"
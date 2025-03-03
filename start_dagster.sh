#!/bin/bash

# Set Dagster home
export DAGSTER_HOME=~/dagster_home

# Activate virtual environment
source venv/bin/activate

# Kill any previous Dagster processes
echo "🛑 Killing old Dagster processes..."
pkill -f "dagster-daemon"
pkill -f "dagster-webserver"

# Start Dagster daemon
echo "🚀 Starting Dagster daemon..."
nohup dagster-daemon run > dagster-daemon.log 2>&1 &

# Start Dagster webserver
echo "🌐 Starting Dagster webserver on http://localhost:3000 ..."
nohup dagster-webserver -w workspace.yaml > dagster-webserver.log 2>&1 &

# Health check
sleep 5
echo "✅ Running health check..."
ps aux | grep dagster

echo "🎉 Dagster is up and running!"

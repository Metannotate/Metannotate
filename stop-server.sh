echo "Running this command kills all jobs that are currently running"

if [ -r "server.pid"  -a -s "server.pid" ]; then
    kill `cat server.pid`
fi

sudo rabbitmqctl stop


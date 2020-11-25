# rabbitmq
RabbitMQ tutorial artifacts

## Languages

There are remnants of both C# .NET Core and Python tutorials here.


## Python getting started

### Start RabbitMQ
```bash
./etc/start-rabbitmq.sh     # will occupy shell; runs in foreground
```

### Install dependencies
```bash
# new shell
python -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip wheel
pip install -r requirements.dev.txt
pip install -r requirements.txt
```

### Tutorials
* [Hello World](https://www.rabbitmq.com/tutorials/tutorial-one-python.html) - queues
* [Work Queues](https://www.rabbitmq.com/tutorials/tutorial-two-python.html) - tasks
* [Publish/Subscribe](https://www.rabbitmq.com/tutorials/tutorial-three-python.html) - logs
* [Routing](https://www.rabbitmq.com/tutorials/tutorial-four-python.html) - direct_logs
* [Topics](https://www.rabbitmq.com/tutorials/tutorial-five-python.html) - topic_logs
* [RPC](https://www.rabbitmq.com/tutorials/tutorial-six-python.html) - rpc

#!/usr/bin/env python
import json
import logging

import pika
import pika.spec as spec


def fib(n: int) -> int:
    '''VERY slow!'''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fib_gen(n: int) -> int:
    '''Better'''
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def on_request(ch: pika.channel.Channel,
               method: spec.Basic.Deliver,
               props: spec.BasicProperties,
               body: bytes) -> None:
    n_str = body.decode()
    logging.info(" [+] fib(%s)" % n_str)
    try:
        n = int(n_str, 0)

        logging.info("   [.] fib(%d)" % n)
        response = {'n_str': n_str, 'n': n, 'rc': fib_gen(n)}
    except ValueError:
        logging.error(f'{n_str} is an invalid int')
        response = {'err': f'{n_str} is an invalid int'}

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(
                         content_type="application/json",
                         correlation_id=props.correlation_id
                     ),
                     body=json.dumps(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)


if __name__ == "__main__":
    try:
        logging.basicConfig(level=logging.INFO)

        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

        channel = connection.channel()

        channel.queue_declare(queue='rpc_queue')

        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(queue='rpc_queue', on_message_callback=on_request)

        logging.info(" [x] Awaiting RPC requests")

        channel.start_consuming()
    except KeyboardInterrupt:
        logging.info('Shutting down')

#!/bin/bash

docker run --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.7-management-alpine

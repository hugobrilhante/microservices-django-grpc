# Microservices with Django and gRPC



## Setup

    git clone https://github.com/hugobrilhante/microservices_django_grpc.git
    cd microservices_django_grpc
    make

## Api

    GET products/
    GET orders/
    POST orders/

## Create Order

    curl --location --request POST 'http://127.0.0.1:8000/orders/' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "user_id": 1,
        "items": [
            {
                "quantity": 1,
                "product_id": 1
            },
            {
                "quantity": 2,
                "product_id": 2    
            }
        ]
    }'
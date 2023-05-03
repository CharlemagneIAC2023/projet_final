#!/bin/bash

scp -r carolus174/linear_regression_model ./models/

docker pull carolus174/fastapi_app

docker run -p 8000:8000 carolus174/fastapi_app

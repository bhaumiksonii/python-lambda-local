# python-lambda-local
>###### A way to test lambda locally without using AWS Console

## To begin, we will require a library to use.

```
pip install python-lambda-local
```

## Using this library and a lot of arguments will help you get run Lambda.

```
python-lambda-local -h
```

## For the time being, we'll be passing event.json while utilising the sample Lamda code. 
## To run the test lambda_handler
```
python-lambda-local -f handler -t 5 lambda_handler.py event.json
```
## Resource

https://pypi.org/project/python-lambda-local/

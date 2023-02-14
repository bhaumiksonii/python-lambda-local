# python-lambda-local
>###### A way to test lambda locally without using AWS Console

## First we will need the library to work with

```
pip install python-lambda-local
```

## you can pass many arguments with this library to get the details use this.

```
python-lambda-local -h
```

## For now we will be using the sample lamda code and will be passing even.json
>###### Make sure the 3rd party libraries used in the AWS Lambda function can be imported.

```
pip install rx==1.6.1
```

## Command to run this test
```
python-lambda-local -f handler -t 5 lambda_handler.py event.json
```

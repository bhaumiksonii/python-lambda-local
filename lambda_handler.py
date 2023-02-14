from __future__ import print_function



def handler(event, context):
    # Extract the input JSON from the event
    input_json = json.loads(event['body'])

    # Do some processing on the input
    output_json = {
        'message': 'Hello, ' + input_json['name'] + '!'
    }

    # Return the output as a JSON string
    return {
        'statusCode': 200,
        'body': json.dumps(output_json)
    }

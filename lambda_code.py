import os
import boto3
import json

runtime= boto3.client('runtime.sagemaker')


ENDPOINT_NAME = os.environ['ENDPOINT_NAME']

def lambda_handler(event, context):

    data = json.loads(json.dumps(event))
    
    
    payload_body = json.loads(data['body']) #cast it into dict
    house_area = payload_body['area'] 
    
    response = runtime.invoke_endpoint(EndpointName= ENDPOINT_NAME,
                                       ContentType='text/csv',
                                       Body= house_area)
    
    response = json.loads(response['Body'].read().decode())
    print(response)
    
    if int(response) == 0:
        final_resp = "beagle"
    elif int(response) == 1:
        final_resp = "german_shepard"
    
    
    return {
        'statusCode': 200,
        'body': json.dumps(final_resp)
    }
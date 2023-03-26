import json
import boto3

dynamodb=boto3.client('dynamodb')

response=dynamodb.put_item(TableName='player',Item={
        "id": {"S": "43"},
        "country": {"S": "ind"},
        "city":{"S": " try"}
    })
    
dynamodb_resource = boto3.resource("dynamodb")
users_table = dynamodb_resource.Table('player')
response = users_table.update_item(
        Key={"id": "43","country":"ind"},
         UpdateExpression="set city = :r",
        ExpressionAttributeValues={
            ':r': 'chennai',
        },
        ReturnValues="UPDATED_NEW",
    )

print(response)

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

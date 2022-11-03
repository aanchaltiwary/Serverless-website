import json
import boto3


def send_EMAIL(msge):
    sns= boto3.client('sns') 
    response = sns.publish( 
        TopicArn='arn:aws:sns:ap-south-1:610146248125:FormMessenger',
        Message=msge,
        Subject='Message from Personal site',
        MessageStructure='Raw'
        )
        
        
def send_SMS(msge):
    sns= boto3.client('sns') 
    response=sns.publish(
        PhoneNumber='+91xxxxxxxxxx',
        Message=msge
        )
        
def lambda_handler(event, context):
    # TODO implement
    
    if(event['httpMethod']=='POST'):
        
        message= event["body"]
        msg=json.loads(message)
        preparedMessage="Hi, This is "+msg['name']+"\n"+msg['message']+"\n"+" Here's my email: "+msg['email']
        
        send_EMAIL(preparedMessage)
        send_SMS(preparedMessage)
        
        print('message:',message)
        response='received your post req'
        
    return {
        'headers':{'Content-Type':'application/json','Access-Control-Allow-Origin':'*'},
        'statusCode': 200,
        'body': json.dumps(response)
    }


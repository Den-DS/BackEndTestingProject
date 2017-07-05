import boto3
from boto3.dynamodb.conditions import Key, Attr

class AWSClient:
    '''
    Describes AWS utilities to use
    '''

    def __init__(self):

        self.lambdaclient = boto3.client('lambda')


    def get_environment_variable(self):
        variables = self.get_function_parameters()['Environment']['Variables']
        return variables

    def get_function_parameters(self, function_name='effect_api_v10_effects_recommended_lambda_dev'):

        response = self.lambdaclient.get_function(FunctionName=function_name)
        return response['Configuration']

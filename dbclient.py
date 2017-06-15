import boto3
from boto3.dynamodb.conditions import Key, Attr


class DBClient:

    def __init__(self, table_name):
        self.dynamodb = boto3.resource('dynamodb')
        self.table = self.dynamodb.Table(table_name)

    def delete_key(self, key_id):
        self.table.delete_item(Key={"Id":key_id})

    def select_item(self, key_id):
        item = self.table.get_item(Key={"Id":key_id})['Item']
        return item

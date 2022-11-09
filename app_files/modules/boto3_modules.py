import boto3
from datetime import datetime
from pandas import Timestamp


def store_data(data, table_name):
    db = boto3.resource('dynamodb')
    table = db.Table(table_name)

    table.put_item(
        Item={
            'time': datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            'location': data['resolvedAddress'],
            "today's data": str(data['days'][0]),
            f"{Timestamp(data['days'][1]['datetime']).day_name()}": str(data['days'][1]),
            f"{Timestamp(data['days'][2]['datetime']).day_name()}": str(data['days'][2]),
            f"{Timestamp(data['days'][3]['datetime']).day_name()}": str(data['days'][3]),
            f"{Timestamp(data['days'][4]['datetime']).day_name()}": str(data['days'][4]),
            f"{Timestamp(data['days'][5]['datetime']).day_name()}": str(data['days'][5]),
            f"{Timestamp(data['days'][6]['datetime']).day_name()}": str(data['days'][6])
        }
    )

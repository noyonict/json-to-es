import os
import json
from elasticsearch import Elasticsearch

es_client = Elasticsearch(hosts=['https://search-vod-v2-1-twgz3ftkkn7bajtcfg7nkorx2e.eu-west-1.es.amazonaws.com'],
                          http_auth=('voduser', 'm2aVod1!'), scheme='https', port=80)


for file in os.listdir():
    if file.endswith('.json'):
        index_name = file.split('.')[0]
        count = 0
        with open(file) as files:
            for data in files.readlines():
                try:
                    doc = json.loads(data)
                    es_client.index(index=index_name, body=doc)
                    # print(doc['client_content_id'], ' created.')
                    count += 1
                except Exception as e:
                    print(e)
        print(count, 'documents created! on index', index_name)

curl_qury = '''
            curl -u voduser:m2aVod1! -XGET "https://n7bajtcfg7nkorx2e.eu-west-1.es.amazonaws.com/packaging*/_search?q=p05czmm5&pretty" -H 'Content-Type: application/json'
'''

import json
from elasticsearch import Elasticsearch

es_client = Elasticsearch(hosts=['https://search-vod-v2-1-twgz3ftkkn7bajtcfg7nkorx2e.eu-west-1.es.amazonaws.com'],
                          http_auth=('voduser', 'm2aVod1!'), scheme='https', port=80)

# mapping = {
#     "mappings": {
#         "properties": {
#             "status": {
#                 "type": "text"  # formerly "string"
#             },
#             "suppress_media_delivery": {
#                 "type": "boolean"
#             },
#             "job_id": {
#                 "type": "text"
#             },
#             "asset_api_url": {
#                 "type": "text"
#             },
#             "client_content_id": {
#                 "type": "text"
#             },
#             "created_at": {
#                 "type": "date"
#             },
#             "updated_at": {
#                 "type": "date"
#             },
#             "payload": {
#                 "type": "nested"
#             },
#             "affiliation_key": {
#                 "type": "text"
#             },
#             "packaging_type": {
#                 "type": "text"
#             },
#             "organization_label": {
#                 "type": "text"
#             },
#             "region": {
#                 "type": "text"
#             },
#             "day": {
#                 "type": "date"
#             }
#         }
#     }
# }
# response = es_client.indices.create(index='packaging_jobs', body=mapping)
# print(response)

with open('m2a-prod-pv2-api-packaging-jobs.json') as packaging_jobs:
    for data in packaging_jobs.readlines():
        try:
            doc = json.loads(data)
            es_client.index(index='packaging_jobs', body=doc)
            print(doc['client_content_id'], ' created.')
        except Exception as e:
            print(e)
        # print(data)
        # break



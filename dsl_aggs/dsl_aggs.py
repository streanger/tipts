from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search

client = Elasticsearch()

s = Search(using=client, index="my-index") \
    .filter("term", category="search") \
    .query("match", title="python")   \
    .exclude("match", description="beta")

# s.aggs.bucket('per_tag', 'terms', field='tags') \
    # .metric('max_lines', 'max', field='lines')

aggs = s.aggs
items = [
    ('bucket', 'per_tag', 'terms', {'field': 'tags1'}),
    ('metric', 'min_lines', 'min', {'field': 'lines1'}),
    ('metric', 'max_lines', 'max', {'field': 'lines2'}),
]
for method, *args, kwargs in items:
    aggs = getattr(aggs, method)(*args, **kwargs)
    
as_dict = aggs.to_dict()
print(as_dict)

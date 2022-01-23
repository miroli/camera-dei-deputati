This repo is for setting standard qualifiers to Italian politicians' P39 statements, using the official API.


## Notes
```
cat camera_data.json | 
    jq --slurpfile w data_wikidata.json \
    '.results.bindings[] | { code: (.persona.value | split("/")[-1][1:]), start: (.startMandato.value  | strptime("%Y%m%d") | strftime("%Y-%m-%d")), end: (.fineMandato.value | strptime("%Y%m%d") | strftime("%Y-%m-%d")) }'
```
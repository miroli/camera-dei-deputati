download:
	poetry run python download.py
	wd sparql get_statements.rq | jq '[.[] | {item, code, st}]' > data_wikidata.json

merge:
	poetry run python merge.py

upload:
	cat merged_data.json | jq -c '.[] | [.st, "P580", .start], [.st, "P582", .end]' | wd aq --batch
	cat merged_data.json | jq -c '.[] | [.st, "P1341", .code]' | wd ar --batch

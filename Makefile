test:
	pytest .

fmt:
	black . --exclude=cloudquery

fmt-check:
	black --check . --exclude=cloudquery

clone-proto:
	git clone https://github.com/cloudquery/plugin-pb

gen-proto:
	cd plugin-pb && git pull && cd ..

	mkdir -p ./protos/cloudquery/plugin_v3
	cp ./plugin-pb/plugin/v3/*.proto ./protos/cloudquery/plugin_v3/.
	python -m grpc_tools.protoc -I./protos --python_out=. --pyi_out=. --grpc_python_out=. ./protos/cloudquery/plugin_v3/*.proto

	mkdir -p ./protos/cloudquery/discovery_v1
	cp ./plugin-pb/discovery/v1/*.proto ./protos/cloudquery/discovery_v1/.
	python -m grpc_tools.protoc -I./protos --python_out=. --pyi_out=. --grpc_python_out=. ./protos/cloudquery/discovery_v1/*.proto

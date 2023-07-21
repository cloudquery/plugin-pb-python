
clone-proto:
	git clone https://github.com/cloudquery/plugin-pb

gen:
	cd plugin-pb && git pull && cd ..
	cp ./plugin-pb/plugin/v3/*.proto ./protos/cloudquery/plugin_v3/.
	python -m grpc_tools.protoc -I./protos --python_out=. --pyi_out=. --grpc_python_out=. ./protos/cloudquery/plugin_v3/*.proto
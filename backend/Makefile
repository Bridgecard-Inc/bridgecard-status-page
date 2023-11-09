

proto:
	rm -f ./src/protos/*.py
	python3 -m grpc_tools.protoc -I ./src/protos --python_out=./src/protos --grpc_python_out=./src/protos ./src/protos/billing_details.proto


cert:
	cd cert; ./gen.sh; cd ..

server:
	python src/main.py

.PHONY : proto cert server
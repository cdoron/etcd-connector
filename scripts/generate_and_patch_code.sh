export ETCD_CONNECTOR_DIR=$PWD

git clone https://github.com/fybrik/fybrik
cd fybrik
# git checkout v0.6.6
cd ..

docker run --rm \
   -v $ETCD_CONNECTOR_DIR:/local \
   -u "$(id -u):$(id -g)" \
   openapitools/openapi-generator-cli generate -g python-flask \
   -o /local/swagger-datacatalog \
   -i /local/fybrik/connectors/api/datacatalog.spec.yaml

cp patch/requirements.txt swagger-datacatalog/requirements.txt
cp patch/Dockerfile swagger-datacatalog/Dockerfile
cp patch/__main__.py swagger-datacatalog/openapi_server/__main__.py
cp patch/util.py swagger-datacatalog/openapi_server/util.py
cp patch/default_controller.py swagger-datacatalog/openapi_server/controllers/default_controller.py

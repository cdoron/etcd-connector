export ETCD_CONNECTOR_DIR=$PWD

cd swagger-datacatalog/
pip install -r requirements.txt

python3 -m openapi_server --config $ETCD_CONNECTOR_DIR/conf/conf.yaml

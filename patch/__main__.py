#!/usr/bin/env python3

import connexion
import argparse

from openapi_server import encoder
from openapi_server.util import init

def main():
    parser = argparse.ArgumentParser(description='ETCD Fybrik Connector')
    parser.add_argument(
        '-p', '--port', type=int, default=8080, help='Listening port')
    parser.add_argument(
        '-c', '--config', type=str, default='/etc/conf/conf.yaml', help='Path to config file')
    parser.add_argument(
        '-l', '--loglevel', type=str, default='warning', help='logging level', 
        choices=['trace', 'info', 'debug', 'warning', 'error', 'critical'])
    args = parser.parse_args()

    init(args.config, args.loglevel.upper())

    app = connexion.App(__name__, specification_dir='./openapi/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml',
                arguments={'title': 'Data Catalog Service - Asset Details'},
                pythonic_params=True)

    app.run(port=args.port)


if __name__ == '__main__':
    main()

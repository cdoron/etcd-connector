import connexion
import six
import json

from openapi_server.models.create_asset_request import CreateAssetRequest  # noqa: E501
from openapi_server.models.create_asset_response import CreateAssetResponse  # noqa: E501
from openapi_server.models.delete_asset_request import DeleteAssetRequest  # noqa: E501
from openapi_server.models.delete_asset_response import DeleteAssetResponse  # noqa: E501
from openapi_server.models.get_asset_request import GetAssetRequest  # noqa: E501
from openapi_server.models.get_asset_response import GetAssetResponse  # noqa: E501
from openapi_server import util
from openapi_server.util import get_client
from fybrik_python_logging import logger


def create_asset():  # noqa: E501
    """This REST API writes data asset information to the data catalog configured in fybrik

     # noqa: E501

    :param x_request_datacatalog_write_cred: This header carries credential information related to accessing the relevant destination catalog.
    :type x_request_datacatalog_write_cred: str
    :param create_asset_request: Write Asset Request
    :type create_asset_request: dict | bytes

    :rtype: CreateAssetResponse
    """

    logger.trace('create_asset')
    if connexion.request.is_json:
        create_asset_request = CreateAssetRequest.from_dict(connexion.request.get_json())  # noqa: E501
        asset_id = create_asset_request.destination_catalog_id + "/" + create_asset_request.destination_asset_id
        etcd_client = get_client()
        etcd_client.put(asset_id, connexion.request.get_data())
        etcd_client.close()
        return CreateAssetResponse(asset_id)
    else:
        return 'invalid JSON format', 400


def delete_asset():  # noqa: E501
    """This REST API deletes data asset

     # noqa: E501

    :param x_request_datacatalog_cred: This header carries credential information related to relevant catalog from which the asset information needs to be retrieved.
    :type x_request_datacatalog_cred: str
    :param delete_asset_request: Delete Asset Request
    :type delete_asset_request: dict | bytes

    :rtype: DeleteAssetResponse
    """
    if connexion.request.is_json:
        delete_asset_request = DeleteAssetRequest.from_dict(connexion.request.get_json())  # noqa: E501
        etcd_client = get_client()
        success = etcd_client.delete(delete_asset_request.asset_id)
        etcd_client.close()
        if success:
            return DeleteAssetResponse('Deletion Successful')
        else:
            return 'asset_id not found', 404
    else:
        return 'invalid JSON format', 400


def get_asset_info():  # noqa: E501
    """This REST API gets data asset information from the data catalog configured in fybrik for the data sets indicated in FybrikApplication yaml

     # noqa: E501

    :param x_request_datacatalog_cred: This header carries credential information related to relevant catalog from which the asset information needs to be retrieved.
    :type x_request_datacatalog_cred: str
    :param get_asset_request: Data Catalog Request Object.
    :type get_asset_request: dict | bytes

    :rtype: GetAssetResponse
    """
    if connexion.request.is_json:
        get_asset_request = GetAssetRequest.from_dict(connexion.request.get_json())  # noqa: E501
        etcd_client = get_client()
        value, _ = etcd_client.get(get_asset_request.asset_id)
        etcd_client.close()
        if value:
            return json.loads(value)
        else:
            return 'asset_id not found', 404

    else:
        return 'invalid JSON format', 400

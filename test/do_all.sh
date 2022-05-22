curl -X POST localhost:8080/createAsset -d @asset.json -H "Content-Type: application/json" -H "X-Request-Datacatalog-Write-Cred: 12345678"

curl -X POST localhost:8080/getAssetInfo -d '{"assetID": "destinationCatalogID/destinationAssetID", "operationType": "read"}' -H "Content-Type: application/json" -H "X-Request-Datacatalog-Cred: 12345678"

curl -X DELETE localhost:8080/deleteAsset -d '{"assetID": "destinationCatalogID/destinationAssetID"}' -H "Content-Type: application/json" -H "X-Request-Datacatalog-Cred: 12345678"

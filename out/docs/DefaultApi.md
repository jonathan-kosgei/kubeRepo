# kube_repo.DefaultApi

All URIs are relative to *https://kubernetes.default.svc*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apis_fqdn_v1_namespaces_namespace_resource_name_get**](DefaultApi.md#apis_fqdn_v1_namespaces_namespace_resource_name_get) | **GET** /apis/{fqdn}/v1/namespaces/{namespace}/{resource}/{name} | Gets a specific Repo
[**apis_fqdn_v1_resource_get**](DefaultApi.md#apis_fqdn_v1_resource_get) | **GET** /apis/{fqdn}/v1/{resource} | Gets Repos


# **apis_fqdn_v1_namespaces_namespace_resource_name_get**
> Repo apis_fqdn_v1_namespaces_namespace_resource_name_get(namespace, name, resource, fqdn)

Gets a specific Repo

Returns a specific repo in a namespace

### Example 
```python
from __future__ import print_statement
import time
import kube_repo
from kube_repo.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
kube_repo.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kube_repo.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kube_repo.DefaultApi()
namespace = 'namespace_example' # str | The Repo's namespace
name = 'name_example' # str | The Repo's name
resource = 'resource_example' # str | The Repo's name
fqdn = 'fqdn_example' # str | The Repo's name

try: 
    # Gets a specific Repo
    api_response = api_instance.apis_fqdn_v1_namespaces_namespace_resource_name_get(namespace, name, resource, fqdn)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->apis_fqdn_v1_namespaces_namespace_resource_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| The Repo&#39;s namespace | 
 **name** | **str**| The Repo&#39;s name | 
 **resource** | **str**| The Repo&#39;s name | 
 **fqdn** | **str**| The Repo&#39;s name | 

### Return type

[**Repo**](Repo.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apis_fqdn_v1_resource_get**
> object apis_fqdn_v1_resource_get(watch, resource, fqdn)

Gets Repos

Returns a list of repos

### Example 
```python
from __future__ import print_statement
import time
import kube_repo
from kube_repo.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
kube_repo.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kube_repo.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kube_repo.DefaultApi()
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
resource = 'resource_example' # str | The Repo's name
fqdn = 'fqdn_example' # str | The Repo's name

try: 
    # Gets Repos
    api_response = api_instance.apis_fqdn_v1_resource_get(watch, resource, fqdn)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->apis_fqdn_v1_resource_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | 
 **resource** | **str**| The Repo&#39;s name | 
 **fqdn** | **str**| The Repo&#39;s name | 

### Return type

**object**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


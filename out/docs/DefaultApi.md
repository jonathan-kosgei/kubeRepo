# kube_repo.DefaultApi

All URIs are relative to *https://kubernetes.default.svc*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apis_fqdn_v1_namespaces_namespace_resource_name_get**](DefaultApi.md#apis_fqdn_v1_namespaces_namespace_resource_name_get) | **GET** /apis/{fqdn}/v1/namespaces/{namespace}/{resource}/{name} | Gets a specific Resource
[**apis_fqdn_v1_resource_get**](DefaultApi.md#apis_fqdn_v1_resource_get) | **GET** /apis/{fqdn}/v1/{resource} | Get resources
[**apis_fqdn_v1_watch_resource_get**](DefaultApi.md#apis_fqdn_v1_watch_resource_get) | **GET** /apis/{fqdn}/v1/watch/{resource} | Watch Resources


# **apis_fqdn_v1_namespaces_namespace_resource_name_get**
> object apis_fqdn_v1_namespaces_namespace_resource_name_get(namespace, name, resource, fqdn)

Gets a specific Resource

Returns a specific Resource in a namespace

### Example 
```python
from __future__ import print_statement
import time
import kube_repo
from kube_repo.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kube_repo.DefaultApi()
namespace = 'namespace_example' # str | The Resource's namespace
name = 'name_example' # str | The Resource's name
resource = 'resource_example' # str | The Resource's name
fqdn = 'fqdn_example' # str | The Resource's name

try: 
    # Gets a specific Resource
    api_response = api_instance.apis_fqdn_v1_namespaces_namespace_resource_name_get(namespace, name, resource, fqdn)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->apis_fqdn_v1_namespaces_namespace_resource_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| The Resource&#39;s namespace | 
 **name** | **str**| The Resource&#39;s name | 
 **resource** | **str**| The Resource&#39;s name | 
 **fqdn** | **str**| The Resource&#39;s name | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apis_fqdn_v1_resource_get**
> apis_fqdn_v1_resource_get(resource, fqdn, watch=watch)

Get resources

Returns a list of resources of kind

### Example 
```python
from __future__ import print_statement
import time
import kube_repo
from kube_repo.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kube_repo.DefaultApi()
resource = 'resource_example' # str | The Resource's name
fqdn = 'fqdn_example' # str | The Resource's name
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    # Get resources
    api_instance.apis_fqdn_v1_resource_get(resource, fqdn, watch=watch)
except ApiException as e:
    print("Exception when calling DefaultApi->apis_fqdn_v1_resource_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | **str**| The Resource&#39;s name | 
 **fqdn** | **str**| The Resource&#39;s name | 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apis_fqdn_v1_watch_resource_get**
> object apis_fqdn_v1_watch_resource_get(resource, fqdn)

Watch Resources

Listen to events about Resources

### Example 
```python
from __future__ import print_statement
import time
import kube_repo
from kube_repo.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kube_repo.DefaultApi()
resource = 'resource_example' # str | The Resource's name
fqdn = 'fqdn_example' # str | The Resource's name

try: 
    # Watch Resources
    api_response = api_instance.apis_fqdn_v1_watch_resource_get(resource, fqdn)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->apis_fqdn_v1_watch_resource_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | **str**| The Resource&#39;s name | 
 **fqdn** | **str**| The Resource&#39;s name | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


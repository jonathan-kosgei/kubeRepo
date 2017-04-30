# kube_repo.DefaultApi

All URIs are relative to *https://kubernetes.default.svc*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apis_git_k8s_com_v1_namespaces_namespace_repos_name_get**](DefaultApi.md#apis_git_k8s_com_v1_namespaces_namespace_repos_name_get) | **GET** /apis/git.k8s.com/v1/namespaces/{namespace}/repos/{name} | Gets a specific Repo
[**apis_git_k8s_com_v1_repos_get**](DefaultApi.md#apis_git_k8s_com_v1_repos_get) | **GET** /apis/git.k8s.com/v1/repos | Gets Repos


# **apis_git_k8s_com_v1_namespaces_namespace_repos_name_get**
> Repo apis_git_k8s_com_v1_namespaces_namespace_repos_name_get(namespace, name)

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

try: 
    # Gets a specific Repo
    api_response = api_instance.apis_git_k8s_com_v1_namespaces_namespace_repos_name_get(namespace, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->apis_git_k8s_com_v1_namespaces_namespace_repos_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| The Repo&#39;s namespace | 
 **name** | **str**| The Repo&#39;s name | 

### Return type

[**Repo**](Repo.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apis_git_k8s_com_v1_repos_get**
> Event apis_git_k8s_com_v1_repos_get(watch)

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

try: 
    # Gets Repos
    api_response = api_instance.apis_git_k8s_com_v1_repos_get(watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->apis_git_k8s_com_v1_repos_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | 

### Return type

[**Event**](Event.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


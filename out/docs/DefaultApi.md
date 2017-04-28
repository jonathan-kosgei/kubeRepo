# kube_repo.DefaultApi

All URIs are relative to *https://kubernetes.default.svc/apis/git.k8s.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**namespaces_namespace_repos_name_get**](DefaultApi.md#namespaces_namespace_repos_name_get) | **GET** /namespaces/{namespace}/repos/{name} | Gets a specific Repo
[**repos_get**](DefaultApi.md#repos_get) | **GET** /repos | Gets Repos
[**watch_repos_get**](DefaultApi.md#watch_repos_get) | **GET** /watch/repos | Watch Repos


# **namespaces_namespace_repos_name_get**
> Repo namespaces_namespace_repos_name_get(namespace, name)

Gets a specific Repo

Returns a specific repo in a namespace

### Example 
```python
from __future__ import print_statement
import time
import kube_repo
from kube_repo.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kube_repo.DefaultApi()
namespace = 'namespace_example' # str | The Repo's namespace
name = 'name_example' # str | The Repo's name

try: 
    # Gets a specific Repo
    api_response = api_instance.namespaces_namespace_repos_name_get(namespace, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->namespaces_namespace_repos_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| The Repo&#39;s namespace | 
 **name** | **str**| The Repo&#39;s name | 

### Return type

[**Repo**](Repo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_get**
> Repos repos_get(watch=watch)

Gets Repos

Returns a list of repos

### Example 
```python
from __future__ import print_statement
import time
import kube_repo
from kube_repo.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kube_repo.DefaultApi()
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    # Gets Repos
    api_response = api_instance.repos_get(watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->repos_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**Repos**](Repos.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_repos_get**
> Event watch_repos_get()

Watch Repos

Listen to events about repos

### Example 
```python
from __future__ import print_statement
import time
import kube_repo
from kube_repo.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kube_repo.DefaultApi()

try: 
    # Watch Repos
    api_response = api_instance.watch_repos_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->watch_repos_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Event**](Event.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


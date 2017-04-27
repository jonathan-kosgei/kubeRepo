# swagger_client.DefaultApi

All URIs are relative to *https://kubernetes.default.svc/apis/git.k8s.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**namespaces_namespace_repos_repo_name_get**](DefaultApi.md#namespaces_namespace_repos_repo_name_get) | **GET** /namespaces/{namespace}/repos/{repoName} | Gets a Repo in a Namespace
[**repos_get**](DefaultApi.md#repos_get) | **GET** /repos | Gets Repos


# **namespaces_namespace_repos_repo_name_get**
> Repo namespaces_namespace_repos_repo_name_get(namespace, repo_name)

Gets a Repo in a Namespace

Returns a specific repo in a namespace

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
namespace = 'namespace_example' # str | The Repo's namespace
repo_name = 'repo_name_example' # str | The Repo's name

try: 
    # Gets a Repo in a Namespace
    api_response = api_instance.namespaces_namespace_repos_repo_name_get(namespace, repo_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->namespaces_namespace_repos_repo_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| The Repo&#39;s namespace | 
 **repo_name** | **str**| The Repo&#39;s name | 

### Return type

[**Repo**](Repo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_get**
> Repos repos_get()

Gets Repos

Returns a list of repos

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try: 
    # Gets Repos
    api_response = api_instance.repos_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->repos_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Repos**](Repos.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


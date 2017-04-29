# coding: utf-8

"""
    kubeRepo

    Manage Repos from k8s

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Repo(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, branch=None, image=None, key=None, oauth=None, path=None, repo=None, then=None, pvc=None, metadata=None):
        """
        Repo - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'branch': 'str',
            'image': 'str',
            'key': 'str',
            'oauth': 'str',
            'path': 'str',
            'repo': 'str',
            'then': 'str',
            'pvc': 'str',
            'metadata': 'Metadata'
        }

        self.attribute_map = {
            'branch': 'branch',
            'image': 'image',
            'key': 'key',
            'oauth': 'oauth',
            'path': 'path',
            'repo': 'repo',
            'then': 'then',
            'pvc': 'pvc',
            'metadata': 'metadata'
        }

        self._branch = None
        self._image = None
        self._key = None
        self._oauth = None
        self._path = None
        self._repo = None
        self._then = None
        self._pvc = None
        self._metadata = None

        # TODO: let required properties as mandatory parameter in the constructor.
        #       - to check if required property is not None (e.g. by calling setter)
        #       - ApiClient.__deserialize_model has to be adapted as well
        if branch is not None:
          self.branch = branch
        if image is not None:
          self.image = image
        if key is not None:
          self.key = key
        if oauth is not None:
          self.oauth = oauth
        if path is not None:
          self.path = path
        if repo is not None:
          self.repo = repo
        if then is not None:
          self.then = then
        if pvc is not None:
          self.pvc = pvc
        if metadata is not None:
          self.metadata = metadata

    @property
    def branch(self):
        """
        Gets the branch of this Repo.

        :return: The branch of this Repo.
        :rtype: str
        """
        return self._branch

    @branch.setter
    def branch(self, branch):
        """
        Sets the branch of this Repo.

        :param branch: The branch of this Repo.
        :type: str
        """

        self._branch = branch

    @property
    def image(self):
        """
        Gets the image of this Repo.

        :return: The image of this Repo.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """
        Sets the image of this Repo.

        :param image: The image of this Repo.
        :type: str
        """

        self._image = image

    @property
    def key(self):
        """
        Gets the key of this Repo.

        :return: The key of this Repo.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this Repo.

        :param key: The key of this Repo.
        :type: str
        """

        self._key = key

    @property
    def oauth(self):
        """
        Gets the oauth of this Repo.

        :return: The oauth of this Repo.
        :rtype: str
        """
        return self._oauth

    @oauth.setter
    def oauth(self, oauth):
        """
        Sets the oauth of this Repo.

        :param oauth: The oauth of this Repo.
        :type: str
        """

        self._oauth = oauth

    @property
    def path(self):
        """
        Gets the path of this Repo.

        :return: The path of this Repo.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this Repo.

        :param path: The path of this Repo.
        :type: str
        """

        self._path = path

    @property
    def repo(self):
        """
        Gets the repo of this Repo.

        :return: The repo of this Repo.
        :rtype: str
        """
        return self._repo

    @repo.setter
    def repo(self, repo):
        """
        Sets the repo of this Repo.

        :param repo: The repo of this Repo.
        :type: str
        """

        self._repo = repo

    @property
    def then(self):
        """
        Gets the then of this Repo.

        :return: The then of this Repo.
        :rtype: str
        """
        return self._then

    @then.setter
    def then(self, then):
        """
        Sets the then of this Repo.

        :param then: The then of this Repo.
        :type: str
        """

        self._then = then

    @property
    def pvc(self):
        """
        Gets the pvc of this Repo.

        :return: The pvc of this Repo.
        :rtype: str
        """
        return self._pvc

    @pvc.setter
    def pvc(self, pvc):
        """
        Sets the pvc of this Repo.

        :param pvc: The pvc of this Repo.
        :type: str
        """

        self._pvc = pvc

    @property
    def metadata(self):
        """
        Gets the metadata of this Repo.

        :return: The metadata of this Repo.
        :rtype: Metadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this Repo.

        :param metadata: The metadata of this Repo.
        :type: Metadata
        """

        self._metadata = metadata

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, Repo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

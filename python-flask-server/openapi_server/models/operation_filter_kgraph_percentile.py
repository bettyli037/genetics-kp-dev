# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.operation_annotate_runner_parameters import OperationAnnotateRunnerParameters
from openapi_server.models.operation_filter_kgraph_percentile_parameters import OperationFilterKgraphPercentileParameters
from openapi_server import util

from openapi_server.models.operation_annotate_runner_parameters import OperationAnnotateRunnerParameters  # noqa: E501
from openapi_server.models.operation_filter_kgraph_percentile_parameters import OperationFilterKgraphPercentileParameters  # noqa: E501

class OperationFilterKgraphPercentile(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, parameters=None, runner_parameters=None):  # noqa: E501
        """OperationFilterKgraphPercentile - a model defined in OpenAPI

        :param id: The id of this OperationFilterKgraphPercentile.  # noqa: E501
        :type id: str
        :param parameters: The parameters of this OperationFilterKgraphPercentile.  # noqa: E501
        :type parameters: OperationFilterKgraphPercentileParameters
        :param runner_parameters: The runner_parameters of this OperationFilterKgraphPercentile.  # noqa: E501
        :type runner_parameters: OperationAnnotateRunnerParameters
        """
        self.openapi_types = {
            'id': str,
            'parameters': OperationFilterKgraphPercentileParameters,
            'runner_parameters': OperationAnnotateRunnerParameters
        }

        self.attribute_map = {
            'id': 'id',
            'parameters': 'parameters',
            'runner_parameters': 'runner_parameters'
        }

        self._id = id
        self._parameters = parameters
        self._runner_parameters = runner_parameters

    @classmethod
    def from_dict(cls, dikt) -> 'OperationFilterKgraphPercentile':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The OperationFilterKgraphPercentile of this OperationFilterKgraphPercentile.  # noqa: E501
        :rtype: OperationFilterKgraphPercentile
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this OperationFilterKgraphPercentile.


        :return: The id of this OperationFilterKgraphPercentile.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OperationFilterKgraphPercentile.


        :param id: The id of this OperationFilterKgraphPercentile.
        :type id: str
        """
        allowed_values = ["filter_kgraph_percentile"]  # noqa: E501
        if id not in allowed_values:
            raise ValueError(
                "Invalid value for `id` ({0}), must be one of {1}"
                .format(id, allowed_values)
            )

        self._id = id

    @property
    def parameters(self):
        """Gets the parameters of this OperationFilterKgraphPercentile.


        :return: The parameters of this OperationFilterKgraphPercentile.
        :rtype: OperationFilterKgraphPercentileParameters
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this OperationFilterKgraphPercentile.


        :param parameters: The parameters of this OperationFilterKgraphPercentile.
        :type parameters: OperationFilterKgraphPercentileParameters
        """
        if parameters is None:
            raise ValueError("Invalid value for `parameters`, must not be `None`")  # noqa: E501

        self._parameters = parameters

    @property
    def runner_parameters(self):
        """Gets the runner_parameters of this OperationFilterKgraphPercentile.


        :return: The runner_parameters of this OperationFilterKgraphPercentile.
        :rtype: OperationAnnotateRunnerParameters
        """
        return self._runner_parameters

    @runner_parameters.setter
    def runner_parameters(self, runner_parameters):
        """Sets the runner_parameters of this OperationFilterKgraphPercentile.


        :param runner_parameters: The runner_parameters of this OperationFilterKgraphPercentile.
        :type runner_parameters: OperationAnnotateRunnerParameters
        """

        self._runner_parameters = runner_parameters

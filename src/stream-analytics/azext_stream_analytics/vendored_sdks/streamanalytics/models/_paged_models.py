# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.paging import Paged


class OperationPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Operation <azure.mgmt.streamanalytics.models.Operation>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Operation]'}
    }

    def __init__(self, *args, **kwargs):

        super(OperationPaged, self).__init__(*args, **kwargs)
class StreamingJobPaged(Paged):
    """
    A paging container for iterating over a list of :class:`StreamingJob <azure.mgmt.streamanalytics.models.StreamingJob>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[StreamingJob]'}
    }

    def __init__(self, *args, **kwargs):

        super(StreamingJobPaged, self).__init__(*args, **kwargs)
class InputPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Input <azure.mgmt.streamanalytics.models.Input>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Input]'}
    }

    def __init__(self, *args, **kwargs):

        super(InputPaged, self).__init__(*args, **kwargs)
class OutputPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Output <azure.mgmt.streamanalytics.models.Output>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Output]'}
    }

    def __init__(self, *args, **kwargs):

        super(OutputPaged, self).__init__(*args, **kwargs)
class FunctionPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Function <azure.mgmt.streamanalytics.models.Function>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Function]'}
    }

    def __init__(self, *args, **kwargs):

        super(FunctionPaged, self).__init__(*args, **kwargs)

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

from .proxy_resource import ProxyResource


class VirtualNetworkRule(ProxyResource):
    """A virtual network rule.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource ID
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param virtual_network_subnet_id: Required. The ARM resource id of the
     virtual network subnet.
    :type virtual_network_subnet_id: str
    :param ignore_missing_vnet_service_endpoint: Create firewall rule before
     the virtual network has vnet service endpoint enabled.
    :type ignore_missing_vnet_service_endpoint: bool
    :ivar state: Virtual Network Rule State. Possible values include:
     'Initializing', 'InProgress', 'Ready', 'Deleting', 'Unknown'
    :vartype state: str or
     ~azure.mgmt.rdbms.mysql.models.VirtualNetworkRuleState
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'virtual_network_subnet_id': {'required': True},
        'state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'virtual_network_subnet_id': {'key': 'properties.virtualNetworkSubnetId', 'type': 'str'},
        'ignore_missing_vnet_service_endpoint': {'key': 'properties.ignoreMissingVnetServiceEndpoint', 'type': 'bool'},
        'state': {'key': 'properties.state', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(VirtualNetworkRule, self).__init__(**kwargs)
        self.virtual_network_subnet_id = kwargs.get('virtual_network_subnet_id', None)
        self.ignore_missing_vnet_service_endpoint = kwargs.get('ignore_missing_vnet_service_endpoint', None)
        self.state = None

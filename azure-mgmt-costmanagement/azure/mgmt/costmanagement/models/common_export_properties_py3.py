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

from msrest.serialization import Model


class CommonExportProperties(Model):
    """The common properties of the export.

    All required parameters must be populated in order to send to Azure.

    :param format: The format of the export being delivered. Possible values
     include: 'Csv'
    :type format: str or ~azure.mgmt.costmanagement.models.FormatType
    :param delivery_info: Required. Has delivery information for the export.
    :type delivery_info: ~azure.mgmt.costmanagement.models.ExportDeliveryInfo
    :param definition: Required. Has definition for the export.
    :type definition: ~azure.mgmt.costmanagement.models.QueryDefinition
    """

    _validation = {
        'delivery_info': {'required': True},
        'definition': {'required': True},
    }

    _attribute_map = {
        'format': {'key': 'format', 'type': 'str'},
        'delivery_info': {'key': 'deliveryInfo', 'type': 'ExportDeliveryInfo'},
        'definition': {'key': 'definition', 'type': 'QueryDefinition'},
    }

    def __init__(self, *, delivery_info, definition, format=None, **kwargs) -> None:
        super(CommonExportProperties, self).__init__(**kwargs)
        self.format = format
        self.delivery_info = delivery_info
        self.definition = definition

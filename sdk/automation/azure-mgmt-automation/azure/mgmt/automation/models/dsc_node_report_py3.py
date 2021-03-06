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


class DscNodeReport(Model):
    """Definition of the dsc node report type.

    :param end_time: Gets or sets the end time of the node report.
    :type end_time: datetime
    :param last_modified_time: Gets or sets the lastModifiedTime of the node
     report.
    :type last_modified_time: datetime
    :param start_time: Gets or sets the start time of the node report.
    :type start_time: datetime
    :param type: Gets or sets the type of the node report.
    :type type: str
    :param report_id: Gets or sets the id of the node report.
    :type report_id: str
    :param status: Gets or sets the status of the node report.
    :type status: str
    :param refresh_mode: Gets or sets the refreshMode of the node report.
    :type refresh_mode: str
    :param reboot_requested: Gets or sets the rebootRequested of the node
     report.
    :type reboot_requested: str
    :param report_format_version: Gets or sets the reportFormatVersion of the
     node report.
    :type report_format_version: str
    :param configuration_version: Gets or sets the configurationVersion of the
     node report.
    :type configuration_version: str
    :param id: Gets or sets the id.
    :type id: str
    :param errors: Gets or sets the errors for the node report.
    :type errors: list[~azure.mgmt.automation.models.DscReportError]
    :param resources: Gets or sets the resource for the node report.
    :type resources: list[~azure.mgmt.automation.models.DscReportResource]
    :param meta_configuration: Gets or sets the metaConfiguration of the node
     at the time of the report.
    :type meta_configuration:
     ~azure.mgmt.automation.models.DscMetaConfiguration
    :param host_name: Gets or sets the hostname of the node that sent the
     report.
    :type host_name: str
    :param i_pv4_addresses: Gets or sets the IPv4 address of the node that
     sent the report.
    :type i_pv4_addresses: list[str]
    :param i_pv6_addresses: Gets or sets the IPv6 address of the node that
     sent the report.
    :type i_pv6_addresses: list[str]
    :param number_of_resources: Gets or sets the number of resource in the
     node report.
    :type number_of_resources: int
    :param raw_errors: Gets or sets the unparsed errors for the node report.
    :type raw_errors: str
    """

    _attribute_map = {
        'end_time': {'key': 'endTime', 'type': 'iso-8601'},
        'last_modified_time': {'key': 'lastModifiedTime', 'type': 'iso-8601'},
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'type': {'key': 'type', 'type': 'str'},
        'report_id': {'key': 'reportId', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
        'refresh_mode': {'key': 'refreshMode', 'type': 'str'},
        'reboot_requested': {'key': 'rebootRequested', 'type': 'str'},
        'report_format_version': {'key': 'reportFormatVersion', 'type': 'str'},
        'configuration_version': {'key': 'configurationVersion', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'errors': {'key': 'errors', 'type': '[DscReportError]'},
        'resources': {'key': 'resources', 'type': '[DscReportResource]'},
        'meta_configuration': {'key': 'metaConfiguration', 'type': 'DscMetaConfiguration'},
        'host_name': {'key': 'hostName', 'type': 'str'},
        'i_pv4_addresses': {'key': 'iPV4Addresses', 'type': '[str]'},
        'i_pv6_addresses': {'key': 'iPV6Addresses', 'type': '[str]'},
        'number_of_resources': {'key': 'numberOfResources', 'type': 'int'},
        'raw_errors': {'key': 'rawErrors', 'type': 'str'},
    }

    def __init__(self, *, end_time=None, last_modified_time=None, start_time=None, type: str=None, report_id: str=None, status: str=None, refresh_mode: str=None, reboot_requested: str=None, report_format_version: str=None, configuration_version: str=None, id: str=None, errors=None, resources=None, meta_configuration=None, host_name: str=None, i_pv4_addresses=None, i_pv6_addresses=None, number_of_resources: int=None, raw_errors: str=None, **kwargs) -> None:
        super(DscNodeReport, self).__init__(**kwargs)
        self.end_time = end_time
        self.last_modified_time = last_modified_time
        self.start_time = start_time
        self.type = type
        self.report_id = report_id
        self.status = status
        self.refresh_mode = refresh_mode
        self.reboot_requested = reboot_requested
        self.report_format_version = report_format_version
        self.configuration_version = configuration_version
        self.id = id
        self.errors = errors
        self.resources = resources
        self.meta_configuration = meta_configuration
        self.host_name = host_name
        self.i_pv4_addresses = i_pv4_addresses
        self.i_pv6_addresses = i_pv6_addresses
        self.number_of_resources = number_of_resources
        self.raw_errors = raw_errors

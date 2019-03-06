# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long

from knack.log import get_logger
from .util import get_id_from_azure_resource, get_query_targets, get_timespan, get_linked_properties

logger = get_logger(__name__)


def execute_query(cmd, client, application, analytics_query, start_time=None, end_time=None, offset='1h', resource_group_name=None):
    """Executes a query against the provided Application Insights application."""
    from .vendored_sdks.applicationinsights.models import QueryBody
    targets = get_query_targets(cmd.cli_ctx, application, resource_group_name)
    return client.query.execute(targets[0], QueryBody(query=analytics_query, timespan=get_timespan(cmd.cli_ctx, start_time, end_time, offset), applications=targets[1:]))


def get_events(cmd, client, application, event_type, event=None, start_time=None, end_time=None, offset='1h', resource_group_name=None):
    timespan = get_timespan(cmd.cli_ctx, start_time, end_time, offset)
    if event:
        return client.events.get(get_id_from_azure_resource(cmd.cli_ctx, application, resource_group=resource_group_name), event_type, event, timespan=timespan)
    return client.events.get_by_type(get_id_from_azure_resource(cmd.cli_ctx, application, resource_group=resource_group_name), event_type, timespan=get_timespan(cmd.cli_ctx, start_time, end_time, offset))


def get_metric(cmd, client, application, metric, start_time=None, end_time=None, offset='1h', interval=None, aggregation=None, segment=None, top=None, orderby=None, filter_arg=None, resource_group_name=None):
    return client.metrics.get(get_id_from_azure_resource(cmd.cli_ctx, application, resource_group=resource_group_name), metric, timespan=get_timespan(cmd.cli_ctx, start_time, end_time, offset), interval=interval, aggregation=aggregation, segment=segment, top=top, orderby=orderby, filter_arg=filter_arg)


def get_metrics_metadata(cmd, client, application, resource_group_name=None):
    return client.metrics.get_metadata(get_id_from_azure_resource(cmd.cli_ctx, application, resource_group=resource_group_name))


def create_or_update_component(cmd, client, application, resource_group_name, location, tags=None, kind="web", application_type='web'):
    from .vendored_sdks.mgmt_applicationinsights.models import ApplicationInsightsComponent
    component = ApplicationInsightsComponent(location, kind, application_type=application_type, tags=tags)
    return client.create_or_update(resource_group_name, application, component)


def get_component(cmd, client, application, resource_group_name):
    return client.get(resource_group_name, application)


def list_components(cmd, client, resource_group_name=None):
    if resource_group_name:
        return client.list_by_resource_group(resource_group_name)
    return client.list()


def create_api_key(cmd, client, application, resource_group_name, api_key_name, read_properties=[], write_properties=[]):
    from .vendored_sdks.mgmt_applicationinsights.models import APIKeyRequest
    linked_read_properties, linked_write_properties = get_linked_properties(cmd.cli_ctx, application, resource_group_name, read_properties, write_properties)
    api_key_request = APIKeyRequest(api_key_name, linked_read_properties, linked_write_properties)
    return client.create(resource_group_name, application, api_key_request)


def list_api_keys(cmd, client, application, resource_group_name):
    return client.list(resource_group_name, application)


def get_api_key(cmd, client, application, resource_group_name, api_key_id):
    return client.get(resource_group_name, application, api_key_id)

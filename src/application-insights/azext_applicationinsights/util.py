# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from datetime import datetime
import dateutil.parser  # pylint: disable=import-error
from msrestazure.tools import is_valid_resource_id, parse_resource_id
from azext_applicationinsights._client_factory import cf_components


def get_id_from_azure_resource(cli_ctx, app, resource_group=None):
    if is_valid_resource_id(app):
        parsed = parse_resource_id(app)
        resource_group, name, subscription = parsed["resource_group"], parsed["name"], parsed["subscription"]
        return cf_components(cli_ctx, None, subscription=subscription).get(resource_group, name).app_id
    if resource_group:
        return cf_components(cli_ctx, None).get(resource_group, app).app_id
    return app


def get_query_targets(cli_ctx, apps, resource_group):
    """Produces a list of uniform GUIDs representing applications to query."""
    if isinstance(apps, list):
        if resource_group:
            return [get_id_from_azure_resource(cli_ctx, apps[0], resource_group)]
        return list(map(lambda x: get_id_from_azure_resource(cli_ctx, x), apps))
    else:
        if resource_group:
            return [get_id_from_azure_resource(cli_ctx, apps, resource_group)]
        return apps


# pyline: disable=dangerous-default-value
def get_linked_properties(cli_ctx, app, resource_group, read_properties=[], write_properties=[]):
    """Maps user-facing role names to strings used to identify them on resources."""
    roles = {
        "ReadTelemetry": "api",
        "WriteAnnotations": "annotations",
        "AuthenticateSDKControlChannel": "agentconfig"
    }

    sub_id = get_subscription_id(cli_ctx)
    tmpl = '/subscriptions/{}/resourceGroups/{}/providers/microsoft.insights/components/{}'.format(sub_id, resource_group, app)
    linked_read_properties, linked_write_properties = [], []

    if isinstance(read_properties, list):
        propLen = len(read_properties)
        linked_read_properties = ['{}/{}'.format(tmpl, roles[read_properties[i]]) for i in range(propLen)]
    else:
        propLen = len(read_properties)
        linked_read_properties = ['{}/{}'.format(tmpl, roles[read_properties])]
    if isinstance(write_properties, list):
        linked_write_properties = ['{}/{}'.format(tmpl, roles[write_properties[i]]) for i in range(propLen)]
    else: 
        linked_write_properties = ['{}/{}'.format(tmpl, roles[write_properties])]
    return linked_read_properties, linked_write_properties


def get_subscription_id(cli_ctx):
    from azure.cli.core._profile import Profile
    _, sub_id, _ = Profile(cli_ctx=cli_ctx).get_login_credentials(subscription_id=None)
    return sub_id


def get_timespan(_, start_time=None, end_time=None, offset=None):
    if not start_time and not end_time:
        # if neither value provided, end_time is now
        end_time = datetime.utcnow().isoformat()
    if not start_time:
        # if no start_time, apply offset backwards from end_time
        start_time = (dateutil.parser.parse(end_time) - offset).isoformat()
    elif not end_time:
        # if no end_time, apply offset fowards from start_time
        end_time = (dateutil.parser.parse(start_time) + offset).isoformat()
    timespan = '{}/{}'.format(start_time, end_time)
    return timespan

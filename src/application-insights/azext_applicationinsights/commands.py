# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long

from azext_applicationinsights._client_factory import (
    cf_events,
    cf_metrics,
    cf_query,
    cf_components
)

from azure.cli.core.commands import CliCommandType


def load_command_table(self, _):

    metrics_sdk = CliCommandType(
        operations_tmpl='azext_applicationinsights.vendored_sdks.applicationinsights.operations.metrics_operations#MetricsOperations.{}',
        client_factory=cf_metrics
    )

    events_sdk = CliCommandType(
        operations_tmpl='azext_applicationinsights.vendored_sdks.applicationinsights.operations.events_operations#EventsOperations.{}',
        client_factory=cf_events
    )

    query_sdk = CliCommandType(
        operations_tmpl='azext_applicationinsights.vendored_sdks.applicationinsights.operations.query_operations#QueryOperations.{}',
        client_factory=cf_query
    )

    components_sdk = CliCommandType(
        operations_tmpl='azext_applicationinsights.vendored_sdks.mgmt_applicationinsights.operations.components_operations#ComponentsOperations.{}',
        client_factory=cf_components
    )

    components_custom_sdk = CliCommandType(
        operations_tmpl='azext_applicationinsights.custom#{}',
        client_factory=cf_components
    )

    with self.command_group('monitor app-insights component', components_sdk) as g:
        g.custom_command('create', 'create_or_update_component', custom_command_type=components_custom_sdk)

    with self.command_group('monitor app-insights metrics', metrics_sdk) as g:
        g.custom_command('show', 'get_metric')
        g.custom_command('get-metadata', 'get_metrics_metadata')

    with self.command_group('monitor app-insights events', events_sdk) as g:
        g.custom_command('show', 'get_events')

    with self.command_group('monitor app-insights', query_sdk) as g:
        g.custom_command('query', 'execute_query')

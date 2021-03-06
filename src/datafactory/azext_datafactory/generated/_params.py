# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines
# pylint: disable=too-many-statements

from azure.cli.core.commands.parameters import (
    tags_type,
    get_three_state_flag,
    get_enum_type,
    resource_group_name_type,
    get_location_type
)
from azure.cli.core.commands.validators import (
    get_default_location_from_resource_group,
    validate_file_or_dict
)
from azext_datafactory.action import (
    AddFactoryVstsConfiguration,
    AddFactoryGitHubConfiguration,
    AddFilters,
    AddOrderBy
)


def load_arguments(self, _):

    with self.argument_context('datafactory factory list') as c:
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('datafactory factory show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', options_list=['--name', '-n'], help='The factory name.', id_part='name')
        c.argument('if_none_match', help='ETag of the factory entity. Should only be specified for get. If the ETag '
                   'matches the existing entity tag, or if * was provided, then no content will be returned.')

    with self.argument_context('datafactory factory create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', options_list=['--name', '-n'], help='The factory name.')
        c.argument('if_match', help='ETag of the factory entity. Should only be specified for update, for which it '
                   'should match existing entity or can be * for unconditional update.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx),
                   validator=get_default_location_from_resource_group)
        c.argument('tags', tags_type)
        c.argument('factory_vsts_configuration', action=AddFactoryVstsConfiguration, nargs='*', help='Factory\'s VSTS '
                   'repo information.', arg_group='RepoConfiguration')
        c.argument('factory_git_hub_configuration', action=AddFactoryGitHubConfiguration, nargs='*', help='Factory\'s '
                   'GitHub repo information.', arg_group='RepoConfiguration')
        c.argument('global_parameters', type=validate_file_or_dict, help='List of parameters for factory. Expected '
                   'value: json-string/@json-file.')

    with self.argument_context('datafactory factory update') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', options_list=['--name', '-n'], help='The factory name.', id_part='name')
        c.argument('tags', tags_type)

    with self.argument_context('datafactory factory delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', options_list=['--name', '-n'], help='The factory name.', id_part='name')

    with self.argument_context('datafactory factory configure-factory-repo') as c:
        c.argument('location', arg_type=get_location_type(self.cli_ctx), id_part='name')
        c.argument('factory_resource_id', help='The factory resource id.')
        c.argument('factory_vsts_configuration', action=AddFactoryVstsConfiguration, nargs='*', help='Factory\'s VSTS '
                   'repo information.', arg_group='RepoConfiguration')
        c.argument('factory_git_hub_configuration', action=AddFactoryGitHubConfiguration, nargs='*', help='Factory\'s '
                   'GitHub repo information.', arg_group='RepoConfiguration')

    with self.argument_context('datafactory factory get-data-plane-access') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', options_list=['--name', '-n'], help='The factory name.', id_part='name')
        c.argument('permissions', help='The string with permissions for Data Plane access. Currently only \'r\' is '
                   'supported which grants read only access.')
        c.argument('access_resource_path', help='The resource path to get access relative to factory. Currently only '
                   'empty string is supported which corresponds to the factory resource.')
        c.argument('profile_name', help='The name of the profile. Currently only the default is supported. The default '
                   'value is DefaultProfile.')
        c.argument('start_time', help='Start time for the token. If not specified the current time will be used.')
        c.argument('expire_time', help='Expiration time for the token. Maximum duration for the token is eight hours '
                   'and by default the token will expire in eight hours.')

    with self.argument_context('datafactory factory get-git-hub-access-token') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', options_list=['--name', '-n'], help='The factory name.', id_part='name')
        c.argument('git_hub_access_code', help='GitHub access code.')
        c.argument('git_hub_client_id', help='GitHub application client ID.')
        c.argument('git_hub_access_token_base_url', help='GitHub access token base URL.')

    with self.argument_context('datafactory integration-runtime list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.')

    with self.argument_context('datafactory integration-runtime show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.', id_part='name')
        c.argument('integration_runtime_name', options_list=['--name', '-n'], help='The integration runtime name.',
                   id_part='child_name_1')
        c.argument('if_none_match', help='ETag of the integration runtime entity. Should only be specified for get. If '
                   'the ETag matches the existing entity tag, or if * was provided, then no content will be returned.')

    with self.argument_context('datafactory integration-runtime linked-integration-runtime create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.')
        c.argument('integration_runtime_name', help='The integration runtime name.')
        c.argument('name', help='The name of the linked integration runtime.')
        c.argument('subscription_id',
                   help='The ID of the subscription that the linked integration runtime belongs to.')
        c.argument('data_factory_name', help='The name of the data factory that the linked integration runtime belongs '
                   'to.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx),
                   validator=get_default_location_from_resource_group)

    with self.argument_context('datafactory integration-runtime managed create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.')
        c.argument('integration_runtime_name', options_list=['--name', '-n'], help='The integration runtime name.')
        c.argument('if_match', help='ETag of the integration runtime entity. Should only be specified for update, for '
                   'which it should match existing entity or can be * for unconditional update.')
        c.argument('description', help='Integration runtime description.')
        c.argument('type_properties_compute_properties', type=validate_file_or_dict, help='The compute resource for '
                   'managed integration runtime. Expected value: json-string/@json-file.')
        c.argument('type_properties_ssis_properties', type=validate_file_or_dict, help='SSIS properties for managed '
                   'integration runtime. Expected value: json-string/@json-file.')

    with self.argument_context('datafactory integration-runtime self-hosted create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.')
        c.argument('integration_runtime_name', options_list=['--name', '-n'], help='The integration runtime name.')
        c.argument('if_match', help='ETag of the integration runtime entity. Should only be specified for update, for '
                   'which it should match existing entity or can be * for unconditional update.')
        c.argument('description', help='Integration runtime description.')
        c.argument('type_properties_linked_info', type=validate_file_or_dict, help='The base definition of a linked '
                   'integration runtime. Expected value: json-string/@json-file.')

    with self.argument_context('datafactory integration-runtime update') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.', id_part='name')
        c.argument('integration_runtime_name', options_list=['--name', '-n'], help='The integration runtime name.',
                   id_part='child_name_1')
        c.argument('auto_update', arg_type=get_enum_type(['On', 'Off']), help='Enables or disables the auto-update '
                   'feature of the self-hosted integration runtime. See https://go.microsoft.com/fwlink/?linkid=854189.'
                   '')
        c.argument('update_delay_offset', help='The time offset (in hours) in the day, e.g., PT03H is 3 hours. The '
                   'integration runtime auto update will happen on that time.')

    with self.argument_context('datafactory integration-runtime delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.', id_part='name')
        c.argument('integration_runtime_name', options_list=['--name', '-n'], help='The integration runtime name.',
                   id_part='child_name_1')

    with self.argument_context('datafactory integration-runtime get-connection-info') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.', id_part='name')
        c.argument('integration_runtime_name', options_list=['--name', '-n'], help='The integration runtime name.',
                   id_part='child_name_1')

    with self.argument_context('datafactory integration-runtime get-monitoring-data') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.', id_part='name')
        c.argument('integration_runtime_name', options_list=['--name', '-n'], help='The integration runtime name.',
                   id_part='child_name_1')

    with self.argument_context('datafactory integration-runtime get-status') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.', id_part='name')
        c.argument('integration_runtime_name', options_list=['--name', '-n'], help='The integration runtime name.',
                   id_part='child_name_1')

    with self.argument_context('datafactory integration-runtime list-auth-key') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.')
        c.argument('integration_runtime_name', options_list=['--name', '-n'], help='The integration runtime name.')

    with self.argument_context('datafactory integration-runtime regenerate-auth-key') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.', id_part='name')
        c.argument('integration_runtime_name', options_list=['--name', '-n'], help='The integration runtime name.',
                   id_part='child_name_1')
        c.argument('key_name', arg_type=get_enum_type(['authKey1', 'authKey2']), help='The name of the authentication '
                   'key to regenerate.')

    with self.argument_context('datafactory integration-runtime remove-link') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.', id_part='name')
        c.argument('integration_runtime_name', options_list=['--name', '-n'], help='The integration runtime name.',
                   id_part='child_name_1')
        c.argument('linked_factory_name', help='The data factory name for linked integration runtime.')

    with self.argument_context('datafactory integration-runtime start') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.', id_part='name')
        c.argument('integration_runtime_name', options_list=['--name', '-n'], help='The integration runtime name.',
                   id_part='child_name_1')

    with self.argument_context('datafactory integration-runtime stop') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.', id_part='name')
        c.argument('integration_runtime_name', options_list=['--name', '-n'], help='The integration runtime name.',
                   id_part='child_name_1')

    with self.argument_context('datafactory integration-runtime sync-credentials') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.', id_part='name')
        c.argument('integration_runtime_name', options_list=['--name', '-n'], help='The integration runtime name.',
                   id_part='child_name_1')

    with self.argument_context('datafactory integration-runtime upgrade') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.', id_part='name')
        c.argument('integration_runtime_name', options_list=['--name', '-n'], help='The integration runtime name.',
                   id_part='child_name_1')

    with self.argument_context('datafactory integration-runtime wait') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.', id_part='name')
        c.argument('integration_runtime_name', options_list=['--name', '-n'], help='The integration runtime name.',
                   id_part='child_name_1')
        c.argument('if_none_match', help='ETag of the integration runtime entity. Should only be specified for get. If '
                   'the ETag matches the existing entity tag, or if * was provided, then no content will be returned.')

    with self.argument_context('datafactory integration-runtime-node show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.', id_part='name')
        c.argument('integration_runtime_name', help='The integration runtime name.', id_part='child_name_1')
        c.argument('node_name', help='The integration runtime node name.', id_part='child_name_2')

    with self.argument_context('datafactory integration-runtime-node update') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.', id_part='name')
        c.argument('integration_runtime_name', help='The integration runtime name.', id_part='child_name_1')
        c.argument('node_name', help='The integration runtime node name.', id_part='child_name_2')
        c.argument('concurrent_jobs_limit', help='The number of concurrent jobs permitted to run on the integration '
                   'runtime node. Values between 1 and maxConcurrentJobs(inclusive) are allowed.')

    with self.argument_context('datafactory integration-runtime-node delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.', id_part='name')
        c.argument('integration_runtime_name', help='The integration runtime name.', id_part='child_name_1')
        c.argument('node_name', help='The integration runtime node name.', id_part='child_name_2')

    with self.argument_context('datafactory integration-runtime-node get-ip-address') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.', id_part='name')
        c.argument('integration_runtime_name', help='The integration runtime name.', id_part='child_name_1')
        c.argument('node_name', help='The integration runtime node name.', id_part='child_name_2')

    with self.argument_context('datafactory linked-service list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.')

    with self.argument_context('datafactory linked-service show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.', id_part='name')
        c.argument('linked_service_name', options_list=['--name', '-n'], help='The linked service name.', id_part=''
                   'child_name_1')
        c.argument('if_none_match', help='ETag of the linked service entity. Should only be specified for get. If the '
                   'ETag matches the existing entity tag, or if * was provided, then no content will be returned.')

    with self.argument_context('datafactory linked-service create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.')
        c.argument('linked_service_name', options_list=['--name', '-n'], help='The linked service name.')
        c.argument('if_match', help='ETag of the linkedService entity.  Should only be specified for update, for which '
                   'it should match existing entity or can be * for unconditional update.')
        c.argument('properties', type=validate_file_or_dict, help='Properties of linked service. Expected value: '
                   'json-string/@json-file.')

    with self.argument_context('datafactory linked-service delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.', id_part='name')
        c.argument('linked_service_name', options_list=['--name', '-n'], help='The linked service name.', id_part=''
                   'child_name_1')

    with self.argument_context('datafactory dataset list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.')

    with self.argument_context('datafactory dataset show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.', id_part='name')
        c.argument('dataset_name', options_list=['--name', '-n'], help='The dataset name.', id_part='child_name_1')
        c.argument('if_none_match', help='ETag of the dataset entity. Should only be specified for get. If the ETag '
                   'matches the existing entity tag, or if * was provided, then no content will be returned.')

    with self.argument_context('datafactory dataset create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.')
        c.argument('dataset_name', options_list=['--name', '-n'], help='The dataset name.')
        c.argument('if_match', help='ETag of the dataset entity.  Should only be specified for update, for which it '
                   'should match existing entity or can be * for unconditional update.')
        c.argument('properties', type=validate_file_or_dict, help='Dataset properties. Expected value: '
                   'json-string/@json-file.')

    with self.argument_context('datafactory dataset delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.', id_part='name')
        c.argument('dataset_name', options_list=['--name', '-n'], help='The dataset name.', id_part='child_name_1')

    with self.argument_context('datafactory pipeline list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.')

    with self.argument_context('datafactory pipeline show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.', id_part='name')
        c.argument('pipeline_name', options_list=['--name', '-n'], help='The pipeline name.', id_part='child_name_1')
        c.argument('if_none_match', help='ETag of the pipeline entity. Should only be specified for get. If the ETag '
                   'matches the existing entity tag, or if * was provided, then no content will be returned.')

    with self.argument_context('datafactory pipeline create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.')
        c.argument('pipeline_name', options_list=['--name', '-n'], help='The pipeline name.')
        c.argument('if_match', help='ETag of the pipeline entity.  Should only be specified for update, for which it '
                   'should match existing entity or can be * for unconditional update.')
        c.argument('pipeline', type=validate_file_or_dict, help='Pipeline resource definition. Expected value: '
                   'json-string/@json-file.')

    with self.argument_context('datafactory pipeline update') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.', id_part='name')
        c.argument('pipeline_name', options_list=['--name', '-n'], help='The pipeline name.', id_part='child_name_1')
        c.argument('if_match', help='ETag of the pipeline entity.  Should only be specified for update, for which it '
                   'should match existing entity or can be * for unconditional update.')
        c.argument('description', help='The description of the pipeline.')
        c.argument('activities', type=validate_file_or_dict, help='List of activities in pipeline. Expected value: '
                   'json-string/@json-file.')
        c.argument('parameters', type=validate_file_or_dict, help='List of parameters for pipeline. Expected value: '
                   'json-string/@json-file.')
        c.argument('variables', type=validate_file_or_dict, help='List of variables for pipeline. Expected value: '
                   'json-string/@json-file.')
        c.argument('concurrency', help='The max number of concurrent runs for the pipeline.')
        c.argument('annotations', type=validate_file_or_dict, help='List of tags that can be used for describing the '
                   'Pipeline. Expected value: json-string/@json-file.')
        c.argument('run_dimensions', type=validate_file_or_dict, help='Dimensions emitted by Pipeline. Expected value: '
                   'json-string/@json-file.')
        c.argument('folder_name', help='The name of the folder that this Pipeline is in.')
        c.ignore('pipeline')

    with self.argument_context('datafactory pipeline delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.', id_part='name')
        c.argument('pipeline_name', options_list=['--name', '-n'], help='The pipeline name.', id_part='child_name_1')

    with self.argument_context('datafactory pipeline create-run') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.')
        c.argument('pipeline_name', options_list=['--name', '-n'], help='The pipeline name.')
        c.argument('reference_pipeline_run_id', help='The pipeline run identifier. If run ID is specified the '
                   'parameters of the specified run will be used to create a new run.')
        c.argument('is_recovery', arg_type=get_three_state_flag(), help='Recovery mode flag. If recovery mode is set '
                   'to true, the specified referenced pipeline run and the new run will be grouped under the same '
                   'groupId.')
        c.argument('start_activity_name', help='In recovery mode, the rerun will start from this activity. If not '
                   'specified, all activities will run.')
        c.argument('start_from_failure', arg_type=get_three_state_flag(), help='In recovery mode, if set to true, the '
                   'rerun will start from failed activities. The property will be used only if startActivityName is '
                   'not specified.')
        c.argument('parameters', type=validate_file_or_dict, help='Parameters of the pipeline run. These parameters '
                   'will be used only if the runId is not specified. Expected value: json-string/@json-file.')

    with self.argument_context('datafactory pipeline-run show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.', id_part='name')
        c.argument('run_id', help='The pipeline run identifier.', id_part='child_name_1')

    with self.argument_context('datafactory pipeline-run cancel') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.', id_part='name')
        c.argument('run_id', help='The pipeline run identifier.', id_part='child_name_1')
        c.argument('is_recursive', arg_type=get_three_state_flag(), help='If true, cancel all the Child pipelines that '
                   'are triggered by the current pipeline.')

    with self.argument_context('datafactory pipeline-run query-by-factory') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.', id_part='name')
        c.argument('continuation_token', help='The continuation token for getting the next page of results. Null for '
                   'first page.')
        c.argument('last_updated_after', help='The time at or after which the run event was updated in \'ISO 8601\' '
                   'format.')
        c.argument('last_updated_before', help='The time at or before which the run event was updated in \'ISO 8601\' '
                   'format.')
        c.argument('filters', action=AddFilters, nargs='*', help='List of filters.')
        c.argument('order_by', action=AddOrderBy, nargs='*', help='List of OrderBy option.')

    with self.argument_context('datafactory activity-run query-by-pipeline-run') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.', id_part='name')
        c.argument('run_id', help='The pipeline run identifier.', id_part='child_name_1')
        c.argument('continuation_token', help='The continuation token for getting the next page of results. Null for '
                   'first page.')
        c.argument('last_updated_after', help='The time at or after which the run event was updated in \'ISO 8601\' '
                   'format.')
        c.argument('last_updated_before', help='The time at or before which the run event was updated in \'ISO 8601\' '
                   'format.')
        c.argument('filters', action=AddFilters, nargs='*', help='List of filters.')
        c.argument('order_by', action=AddOrderBy, nargs='*', help='List of OrderBy option.')

    with self.argument_context('datafactory trigger list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.')

    with self.argument_context('datafactory trigger show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.', id_part='name')
        c.argument('trigger_name', options_list=['--name', '-n'], help='The trigger name.', id_part='child_name_1')
        c.argument('if_none_match', help='ETag of the trigger entity. Should only be specified for get. If the ETag '
                   'matches the existing entity tag, or if * was provided, then no content will be returned.')

    with self.argument_context('datafactory trigger create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.')
        c.argument('trigger_name', options_list=['--name', '-n'], help='The trigger name.')
        c.argument('if_match', help='ETag of the trigger entity.  Should only be specified for update, for which it '
                   'should match existing entity or can be * for unconditional update.')
        c.argument('properties', type=validate_file_or_dict, help='Properties of the trigger. Expected value: '
                   'json-string/@json-file.')

    with self.argument_context('datafactory trigger delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.', id_part='name')
        c.argument('trigger_name', options_list=['--name', '-n'], help='The trigger name.', id_part='child_name_1')

    with self.argument_context('datafactory trigger get-event-subscription-status') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.', id_part='name')
        c.argument('trigger_name', options_list=['--name', '-n'], help='The trigger name.', id_part='child_name_1')

    with self.argument_context('datafactory trigger query-by-factory') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.', id_part='name')
        c.argument('continuation_token', help='The continuation token for getting the next page of results. Null for '
                   'first page.')
        c.argument('parent_trigger_name', help='The name of the parent TumblingWindowTrigger to get the child rerun '
                   'triggers')

    with self.argument_context('datafactory trigger start') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.', id_part='name')
        c.argument('trigger_name', options_list=['--name', '-n'], help='The trigger name.', id_part='child_name_1')

    with self.argument_context('datafactory trigger stop') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.', id_part='name')
        c.argument('trigger_name', options_list=['--name', '-n'], help='The trigger name.', id_part='child_name_1')

    with self.argument_context('datafactory trigger subscribe-to-event') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.', id_part='name')
        c.argument('trigger_name', options_list=['--name', '-n'], help='The trigger name.', id_part='child_name_1')

    with self.argument_context('datafactory trigger unsubscribe-from-event') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.', id_part='name')
        c.argument('trigger_name', options_list=['--name', '-n'], help='The trigger name.', id_part='child_name_1')

    with self.argument_context('datafactory trigger wait') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.', id_part='name')
        c.argument('trigger_name', options_list=['--name', '-n'], help='The trigger name.', id_part='child_name_1')
        c.argument('if_none_match', help='ETag of the trigger entity. Should only be specified for get. If the ETag '
                   'matches the existing entity tag, or if * was provided, then no content will be returned.')

    with self.argument_context('datafactory trigger-run query-by-factory') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.', id_part='name')
        c.argument('continuation_token', help='The continuation token for getting the next page of results. Null for '
                   'first page.')
        c.argument('last_updated_after', help='The time at or after which the run event was updated in \'ISO 8601\' '
                   'format.')
        c.argument('last_updated_before', help='The time at or before which the run event was updated in \'ISO 8601\' '
                   'format.')
        c.argument('filters', action=AddFilters, nargs='*', help='List of filters.')
        c.argument('order_by', action=AddOrderBy, nargs='*', help='List of OrderBy option.')

    with self.argument_context('datafactory trigger-run rerun') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.', id_part='name')
        c.argument('trigger_name', help='The trigger name.', id_part='child_name_1')
        c.argument('run_id', help='The pipeline run identifier.', id_part='child_name_2')

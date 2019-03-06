# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps

# pylint: disable=line-too-long

helps['monitor app-insights'] = """
    type: group
    short-summary: Commands for interacting with Application Insights applications and their data.
"""

helps['monitor app-insights component'] = """
    type: group
    short-summary: Manage an Application Insights component or its subcomponents.
"""

helps['monitor app-insights component create'] = """
    type: command
    short-summary: Create a new Application Insights resource.
    examples:
      - name: Create a component with kind web and location.
        text: |
          az monitor app-insights component create --app demoApp --location westus2 --kind web -g demoRg
"""

helps['monitor app-insights component show'] = """
    type: command
    short-summary: Get an Application Insights resource.
    examples:
      - name: Get a component by name.
        text: |
          az monitor app-insights component show --app demoApp -g demoRg
"""

helps['monitor app-insights component list'] = """
    type: command
    short-summary: List all Application Insights resources in a resource group.
    examples:
      - name: List components in a resource group.
        text: |
          az monitor app-insights component list -g demoRg
"""

helps['monitor app-insights component api-key'] = """
    type: group
    short-summary: Operations on API keys associated with an Application Insights component.
"""

helps['monitor app-insights component api-key list'] = """
    type: command
    short-summary: List API keys associated with an Application Insights resource.
    examples:
      - name: Fetch API Keys.
        text: |
          az monitor app-insights component api-key list --app demoApp -g demoRg
"""

helps['monitor app-insights component api-key show'] = """
    type: command
    short-summary: Get a specific API key associated with an Application Insights resource.
    parameters:
      - name: --api-key-id
        type: string
        short-summary: ID of the API key to fetch. Can be found using `api-keys list`.
    examples:
      - name: Fetch API Key.
        text: |
          az monitor app-insights component api-key show --app demoApp -g demoRg --api-key-id f7231867-6c63-4354-8d80-27776f237ea0
"""

helps['monitor app-insights component api-key create'] = """
    type: command
    short-summary: Create a new API key for use with an Application Insights resource.
    parameters:
      - name: --api-key-name
        type: string
        short-summary: Name for the API key to create.
      - name: --read-properties
        type: list
        short-summary: A space seperated list of names of read Roles for this API key to inherit. Possible values include ReadTelemetry and AuthenticateSDKControlChannel.
      - name: --write-properties
        type: list  
        short-summary: A space seperated list of names of write Roles for this API key to inherit. Possible values include WriteAnnotations.
    examples:
      - name: Create a component with kind web and location.
        text: |
          az monitor app-insights component api-key create --api-key-name cli-demo --read-properties ReadTelemetry -g demoRg
"""

helps['monitor app-insights metrics'] = """
    type: group
    short-summary: Retrieve metrics from an application.
"""

helps['monitor app-insights events'] = """
    type: group
    short-summary: Retrieve events from an application.
"""

helps['monitor app-insights query'] = """
    type: command
    short-summary: Execute a query over data in your application.
    parameters:
      - name: --offset
        short-summary: >
          Time offset of the query range, in ##d##h format.
        long-summary: >
          Can be used with either --start-time or --end-time. If used with --start-time, then
          the end time will be calculated by adding the offset. If used with --end-time (default), then
          the start time will be calculated by subtracting the offset. If --start-time and --end-time are
          provided, then --offset will be ignored.
    examples:
      - name: Execute a simple query over past 3.5 days.
        text: |
          az monitor app-insights query --app e292531c-eb03-4079-9bb0-fe6b56b99f8b --analytics-query 'requests | summarize count() by bin(timestamp, 1h)' --offset P3DT12H
"""

helps['monitor app-insights metrics show'] = """
    type: command
    short-summary: View the value of a single metric.
    parameters:
      - name: --interval
        short-summary: >
          The interval over which to aggregate metrics, in ##h##m format.
      - name: --offset
        short-summary: >
          Time offset of the query range, in ##d##h format.
        long-summary: >
          Can be used with either --start-time or --end-time. If used with --start-time, then
          the end time will be calculated by adding the offset. If used with --end-time (default), then
          the start time will be calculated by subtracting the offset. If --start-time and --end-time are
          provided, then --offset will be ignored.
    examples:
      - name: View the count of availabilityResults events.
        text: |
          az monitor app-insights metrics show --app e292531c-eb03-4079-9bb0-fe6b56b99f8b --metric availabilityResults/count
"""

helps['monitor app-insights metrics get-metadata'] = """
    type: command
    short-summary: Get the metadata for metrics on a particular application.
    examples:
      - name: Views the metadata for the provided app.
        text: |
          az monitor app-insights metrics get-metadata --app e292531c-eb03-4079-9bb0-fe6b56b99f8b
"""

helps['monitor app-insights events show'] = """
    type: command
    short-summary: List events by type or view a single event from an application, specified by type and ID.
    parameters:
      - name: --offset
        short-summary: >
          Time offset of the query range, in ##d##h format.
        long-summary: >
          Can be used with either --start-time or --end-time. If used with --start-time, then
          the end time will be calculated by adding the offset. If used with --end-time (default), then
          the start time will be calculated by subtracting the offset. If --start-time and --end-time are
          provided, then --offset will be ignored.
    examples:
      - name: Get an availability result by ID.
        text: |
          az monitor app-insights events show --app 578f0e27-12e9-4631-bc02-50b965da2633 --type availabilityResults --event b2cf08df-bf42-4278-8d2c-5b55f85901fe
      - name: List availability results from the last 24 hours.
        text: |
          az monitor app-insights events show --app 578f0e27-12e9-4631-bc02-50b965da2633 --type availabilityResults --offset 24h
"""

# this will initialize the workplace
# to access the workspace create a workspace object from config.json file which can be downloded from the azure ml studio.

from azureml.core import Workspace

ws = Workspace.from_config()
print('workspace name: ' + ws.name,
       'Azure region: ' + ws.location,
       'Subscription id: ' + ws.subscription_id,
       'Resource group: ' + ws.resource_group, sep = '\n')


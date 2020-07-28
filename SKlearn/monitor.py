from azureml.widgets import RunDetails
RunDetails(run).show()

run.wait_for_completion(show_output=True)
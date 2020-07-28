from azureml.core import Experiment

experiment_name = 'train_iris'
experiment = Experiment(ws, name=experiment_name)

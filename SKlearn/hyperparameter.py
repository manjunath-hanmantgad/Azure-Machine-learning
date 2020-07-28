# tuning , ssampling of hyperparameters.

from azureml.train.hyperdrive.runconfig import HyperDriveRunConfig
from azureml.train.hyperdrive.sampling import RandomParameterSampling
from azureml.train.hyperdrive.run import PrimaryMetricGoal
from azureml.train.hyperdrive.parameter_expressions import choice

param_sampling = RandomParameterSampling( { 
    "--kernel": choice('linear','rbf','poly','sigmoid'),
    "--penalty": choice(0.5, 1, 1.5)
    }
)

hyperdrive_run_config = HyperDriveRunConfig(estimator=estimator,
                                            hyperparameter_sampling=param_sampling,
                                            primary_metric_name='Accuracy',
                                            primary_metric_goal=PrimaryMetricGoal.MAXIMIZE,
                                            max_total_runs=12,
                                            max_concurrent_runs=4)


# launch the hyperparameter tuning job.

hyperdrive_run = experiment.submit(hyperdrive_run_config)

# monitor hyperdrive runs 

RunDetails(hyperdrive_run).show()
hyperdrive_run.wait_for_Completion(show_output=True)
assert(hyperdrive_run.get_status() == "Completed")
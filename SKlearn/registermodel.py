best_run = hyperdrive_run.get_best_run_by_primary_metric()
print(best_run.get_details()['runDefinition']['arguments'])

# list the models uploadded during run 

print(best_run.get_file_names())

model = best_run.register_model(model_name='sklearn-iris', model_path='outputs/model.joblib')
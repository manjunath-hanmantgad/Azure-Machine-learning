# 1. create a configuration
#2. create the cluster
#3. provision the VM 

from azureml.core.compute import ComputeTarget, AmlCompute
from azureml.core.compute_target import ComputeTargetException

# here my cluster name 
cluster_name = "manjunathcluster1"

# write the exception block to check if compute target exists 
# if not then create new compute target

try:
    compute_target = ComputeTarget(workspace=ws, name=cluster_name)
    print('Found existing compute target')
except ComputeTargetException:
    print('Creating new compute target...')
    compute_config = AmlCompute.provisioning_configuration(vm_size='Standard_D2_V2',max_nodes=4)

# now create the cluster

compute_target = ComputeTarget.create(ws, cluster_name, compute_config)

compute_target.wait_for_completion(show_output=True, min_node_count=None, timeout_in_minutes=20)

print(compute_target.get_status().serialize())
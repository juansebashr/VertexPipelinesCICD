from kfp.v2.components.executor import Executor
from kfp.v2.dsl import Metrics, Model, Dataset
from utils import get_value
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument("--executor-input", type=str, required=True)
args = parser.parse_args()

print(args.executor_input)

# Uploads executor arguments
executor_input = json.loads(args.executor_input)
executor = Executor(executor_input, lambda x: x)

# Inputs and outputs

data: Dataset = executor._input_artifacts['input_dataset']
metrics: Metrics = executor._output_artifacts['metrics']
model: Model = executor._output_artifacts['model']
param: str = get_value(executor._input['inputs']['parameters']['param1'])

# Metrics logs
metrics.log_metric("accuracy", 0.9)

with open(data.path + '.txt', "r") as input_file:
    dataset_two_contents = input_file.read()

print(dataset_two_contents)
print(param)

# Model saving
with open(model.path + '.txt', "w") as f:
    f.write("data")

# Write output
executor._write_executor_output()
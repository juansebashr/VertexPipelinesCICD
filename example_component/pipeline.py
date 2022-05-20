from kfp.v2 import dsl, compiler
from kfp.components import load_component_from_file
from google.cloud import aiplatform


script = load_component_from_file("component.yaml")


@dsl.pipeline(name="kfp-component")
def pipeline():
    script_op = script()

"""
Compile and Run
"""
compiler.Compiler().compile(
    pipeline_func=pipeline,
    package_path="kfp-component.json"
)

aiplatform.PipelineJob(
    display_name="kfp-component",
    template_path="kfp-component.json",
    pipeline_root="gs://<your-bucket>"
).submit()

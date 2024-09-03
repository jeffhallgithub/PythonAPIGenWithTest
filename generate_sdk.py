#!/usr/bin/env python3

import subprocess

GEN_OUTPUT_DIR="./gen_eligibility_api"

def main():

    # Generate the Python SDK, based on our OpenAPI Spec 
    subprocess.run(
        ["openapi-python-client", "generate", "--overwrite", "--path", "./eligibility_api.yaml", "--output-path", GEN_OUTPUT_DIR]
    )
    subprocess.run(
        ["touch", "{dir}/__init__.py".format(dir=GEN_OUTPUT_DIR)]
    )
    print("Done!")


if __name__ == "__main__":
    main()

# Assumptions
Since this is a quick challenge, I am making some assumptions based on the given instructions.
1. The instructions don't say what operating systems need to be supported, so I'm assuming to support Linux only. 
2. The instructions say `The SCRIPT should include commands to install the dependencies, generate the SDK, and run the tests.`, and while installing python and other dependencies from within a python script is possible, it seemed confusing and messy. Therefore, I'm guessing this meant to say that the README should include commands to install dependencies and then launch the python script to generate the SDK, run the tests, etc. 
3. The instructions say `You should generate the SDK using your logic or a suitable generator that supports OpenAPI Specification.`, so I'm choosing to use this tool: [OpenApi-Python-Client](https://github.com/openapi-generators/openapi-python-client)
4. The instructions say `The SDK should include a Python class that encapsulates the API interactions, making it easy for other developers to use.` For me, that class is `EligibilityApiClient.py`

## Install Dependencies
First, we must install our Python Dependencies
```
$ pip install -r requirements.txt
```

Next, It's helpful to have a mock server that fulfills the API described in the OpenAPI Spec, against which we can develop and test client-side SDK code! A tool I really like for this is [Prism](https://github.com/stoplightio/prism) which can be installed be running the following command:
```
$ curl -L https://raw.githack.com/stoplightio/prism/master/install | sh
```
Or for convenience, I've downloaded the binary and have made it available in the root directory if this repo! See `./prism-linux`!

## Generate the SDK
Included in this repo is a python script `generate_sdk.py` which will generate a Python Client SDK for interacting with the Eligibility API.
```
$ python generate_sdk.py
```

## Start the Mock Server
It's difficult to test the generated client-side SDK without a real server or mock fulfilling the API spec. Let's use Prism to start a mock server based on the given spec. In one terminal, run the following:
```
$ ./prism-linux mock ./eligibility_api.yaml
```
(To exit Prism, press `Ctrl + C`)

## Run the tests
In another terminal, let's run the tests for our Eligibility API SDK!
```
$ pytest
```
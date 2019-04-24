# Serverless Session

Steps for installing serverless and setting up basic serverless function

* Installing serverless globally
```bash
npm i -g serverless
```
* Creating folder for function
```bash
mkdir serverless-service
cd serverless-service
```
* Setting up project template according to specific cloud provider.
```bash
sls create --template aws-python3
```
* Edit `serverless.yml` according to your specific deployment
* Adding credentials of cloud provider for deployment
```bash
sls config credentials --provider aws --key <user-key> --secret <user-secret>
```
* Deploy function
```bash
sls deploy -v
```

In case you want to remove function from your account, you can simply do `sls remove`. It will remove the function automatically which is specified in your `serverless.yml` file ⚠️ .
# Serverless Session

Steps for installing and serverless and setting up basic serverless function

* Installing serverless globally
```bash
npm i -g serverless
```
* Creating folder for function, else all the template will be in `cwd`
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
# meal-plan

A toy project that generates a random meal plan by querying a OurGroceries.com account for recipes via a python lambda on AWS.

## Configuration

### AWS Lambda Environment Variables
Configure the lambda with the following environment variables

| Key | Description |
| --- | ---   |
| OUR_GROCERIES_EMAIL | the account email address |
| OUR_GROCERIES_PASSWORD | the account password |
| OUR_GROCERIES_TEAM_ID | the account team ID (use dev tools to find after logging in) |

> To Do: move these values to GitHub secrets and deploy them to the lambda from Github

### Github Secrets
In order for the GitHub action to successfully deploy to AWS, the following GitHub secrets must be configured

| Key | Description |
| --- | ---   |
| AWS_ACCESS_KEY_ID | The AWS Access Key ID |
| AWS_SECRET_ACCESS_KEY | The AWS Secret Access Key |
| AWS_REGION | The AWS Region (e.g. us-east-2) |

import http.cookiejar, urllib.request, json, os

# CONSTANTS
emailAddress = os.environ.get('OUR_GROCERIES_EMAIL','me@example.com')
password = os.environ.get('OUR_GROCERIES_PASSWORD', 'super.duper.secret')
teamId = os.environ.get('OUR_GROCERIES_TEAM_ID', 'ekdie123Gave9483pameny')
signInUrl = 'https://www.ourgroceries.com/sign-in'
signInData = f'emailAddress={emailAddress}&action=sign-me-in&password={password}'
recipeUrl = 'https://www.ourgroceries.com/your-lists/'

def createOpener():
  return urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))

def login(opener):
  opener.open(signInUrl) # get initial cookies from sign in page
  opener.open(signInUrl, signInData.encode('utf-8')) # get authentication cookies

def getRecipes(opener):
  request = getJsonRequest(recipeUrl, {'command': 'getOverview',  'teamId': teamId})
  response = opener.open(request)
  return readJsonResponse(response)

def getJsonRequest(url, data):
  body = json.dumps(data).encode('utf8')
  headers = {'Content-type': 'application/json'}
  return urllib.request.Request(recipeUrl, body, headers)

def readJsonResponse(jsonResponse):
  return json.loads(jsonResponse.read())

def lambda_handler(event, context):
    opener = createOpener()
    login(opener)
    return {
        'statusCode': 200,
        'headers': {
          'Content-Type': 'application/json',
          'Access-Control-Allow-Origin': '*'
        },
        'body': getRecipes(opener)
    }

# Run program
response = lambda_handler(None, None)
print(response)

SOCIAL_AUTH_TWITTER_KEY = 'z7oFYK8Na5302RE1Osls65tif'
SOCIAL_AUTH_TWITTER_SECRET = 'AVp4JhpBiM8zvBZm2YMfLZHXCWTuK8bUqVcIRCivEgqk4ZQDrD'

SOCIAL_AUTH_FACEBOOK_KEY = '271670986628571'
SOCIAL_AUTH_FACEBOOK_SECRET = 'fd915b5e449f8c53c062dc4e27071f0d'
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email', 'read_custom_friendlists', 'user_photos', 'user_friends', 'user_posts']
# http://localhost:8000/login/facebook/
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
  'locale': 'ru_RU',
  'fields': 'id, name, email, age_range'
}

# SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '471309040227-kmcknd9seeuscd6da7mooqb1h8e5de9l.apps.googleusercontent.com'
# SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '9WKv0UbGS-2TKWZn-D3QKIqI'
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY =  '829107062441-pvbpml61og2balmjd8dh3uttbapfcm6c.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'PEWMFVUIlHFLVAbyv8wr2xJb'

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/home/'
SOCIAL_AUTH_LOGIN_URL = '/'

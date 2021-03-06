# User Object
# <class 'tweepy.models.User'>

# id : The ID of the user.
# id_str : The ID of the user as a string.
# name : The name of the user.
# screen_name : The screen name of the user
# location : The location of the user.
# profile_location : The location of the the profile.
# description : The description of the user account.
# url : The URL of the user account.
# entities : A dictionary containing URLs.
# protected : Indicates if the user profile is protected or not.
# followers_count : The number of followers the account has.
# friends_count : The number of friends the account has.
# listed_count : The number of public lists the account has been added to.
# created_at : The time at which the account was created.
# favourites_count : The number of statuses the account has favourited.
# utc_offset : The UTC offset of the profile.
# geo_enabled : Indicates whether the account is geo enabled or not.
# verified : Indicates whether the user is verified or not.
# statuses_count : The number of statuses updated by the user.
# lang : The language of the account.
# status : Fetches the latest status updated by the user.
# contributors_enabled : Indicates whether the contributors are enabled or not.
# is_translator : Indicates whether there is a translator or not.
# is_translation_enabled : Indicates whether the translation is available or not.
# profile_background_color : The background color of the profile.
# profile_background_image_url : The URL of the background image of the profile.
# profile_background_image_url_https : The secure URL of the background image of the profile.
# profile_background_tile : The title of the background profile.
# profile_image_url : The URL of the profile image.
# profile_image_url_https : The secure URL of the profile image.
# profile_banner_url : The URL of the profile banner.
# profile_link_color : The color of the profile link.
# profile_sidebar_border_color : The color of the profile sidebar border.
# profile_sidebar_fill_color : The color of the profile sidebar.
# profile_text_color : The color of the profile text.
# profile_use_background_image : Indicates whether the profile is to use a background image or not.
# has_extended_profile : Indicates whether the profile is extended or not.
# default_profile : The default profile.
# default_profile_image : The image of the default profile.
# following : Indicates whether the authenticated user is following the user or not.
# follow_request_sent : Indicates whether the authenticated user has requested to follow the user or not.
# notifications: Indicates whether the authenticated user has turned on the notifications for the user or not.


# calling the api
api = tweepy.API(auth)

# the screen name of the user
screen_name = "pbragamiranda"

# fetching the user
user = api.get_user(screen_name)

# printing the information
print("The id is : " + str(user.id))
print("The id_str is : " + user.id_str)
print("The name is : " + user.name)
print("The screen_name is : " + user.screen_name)
print("The location is : " + str(user.location))
print("The profile_location is : " + str(user.profile_location))
print("The description is : " + user.description)

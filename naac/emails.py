from naac import naac_settings as config
import uuid


from_email = "exodis@zoho.eu"

reg_topic = "You have registered on %s" % config.site_name
reg_message = """Welcome! \n\n
    Your username: {username} \n\n
We hope you have great fun playing on %s
See you in game! \n
%s Team""" % (config.site_name, config.site_name)

res_topic = "Password Recovery"
res_message = "Hello, you have requested a password reset on %s" % config.site_name
res_message += "\n\n We got you. Click the link below to set a new password:"
res_message += "\n\n http://localhost:8000/accounts/reset/{hash}"
res_message += "\n\n %s Team" % config.site_name

def generateHash():
    return uuid.uuid4().hex[:32].upper()

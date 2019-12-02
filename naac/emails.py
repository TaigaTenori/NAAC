from naac import naac_settings as config

from_email = "exodis@zoho.eu"
reg_topic = "You have registered on %s" % config.site_name
reg_message = """Welcome! \n\n
    Your username: {username} \n\n
We hope you have great fun playing on %s
See you in game! \n
%s Team""" % (config.site_name, config.site_name)

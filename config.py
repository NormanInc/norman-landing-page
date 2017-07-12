class GoogleConfig:
    SAFEBROWSINGAPIKEY = 'AIzaSyARGechcnls1l2O80mA8Fh3q3_67JTb7Fg'


class UIConfig:
    MAIN_UI_TEXT = 'State of the art range of products for health data collation, management and patient monitoring.'
    SECTION_TWO_TITLE = 'Conveniently upload, store, collate and analyze medical data using our range of products.'
    SECTION_TWO_INFO = '''Norman provides Machine Learning powered range of tools to help collate, manage and analyze patient data.
                              It abstracts the tedious task of medical data management and lets you focus on the
                              absolutely important things.
                            '''
    SECTION_THREE_TITLE = 'Intuitively designed interfaces for efficient medical collaboration'
    SECTION_THREE_INFO = '''Collaborate, manage data and provide optimum care to your patients with our
                            user friendly platforms across all your devices
                            '''
    SECTION_FOUR_TITLE = 'Designed for medical facilities.'
    SECTION_FOUR_INFO = '''The Norman Team has over time studied the medical sector which had a great impact in how the interface
                            has been designed.'''
    COMPANY_EMAIL = "bot.normanai@gmail.com"
    COMPANY_PHONE = "9036671876"
    COMPANY_ADDRESS = "Ilab, Department of Electronics Electrical Engineering, Obafemi Awolowo University, " \
                      "Ile-Ife, Osun State"

    NORMAN_FEATURES_LEFT = {"Your Data In Cloud": {"description": "Norman seamlessly stores and syncs your data\
                                        and makes it available on all platforms.It also syncs your patient health data from their social media account and your hospital portal.",
                                                   'icon': 'soundcloud'},
                            "Security": {"description": "The core Norman philosophy is security.\
                                            Norman keeps your data secured using standard security protocols making it only accessible to you. Read our security policies here.",
                                         'icon': 'lock-locked'},
                            "Modern Design": {"description": "Norman was designed using core modern AI principles.\
                                                          It has been designed to use the best and most convenient approaches at saving,\
                                                          analyzing and managing your patient data.",
                                              "icon": "computer-imac"}
                            }
    NORMAN_FEATURES_RIGHT = {"Human Readable Data Format": {"description": "Every data collected by Norman "
                                                                           "is formatted in a well structured human readable table.",
                                                            "icon": "grid"},

                             "Excellent Performance": {"description": "Norman Analytics and Norman Bot have a 99% uptime and response rate.\
                                       <br> As such your data is always available and the companion is always there for your patients..",
                                                       "icon": "layers-image"},
                             "Machine Learning": {"description": "Norman uses machine learning to continuously learn from each\
                                                          conversation it has with your patient. "
                                                                 "As such, it provides better, faster help everytime.",
                                                  "icon": "refresh"}
                             }


class Config(UIConfig):
    APP_NAME = "Norman"


class DevConfig(Config):
    ENV = 'dev'
    REDIS_URL = "redis://:password@localhost:6379/0"
    BASE_URL = "http://localhost:5000"


class ProdConfig(Config):
    ENV = 'prod'
    REDIS_URL = "redis://:password@localhost:6379/0"
    BASE_URL = "https://www.norman-ml.herokuapp.com"



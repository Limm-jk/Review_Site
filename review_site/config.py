# /**
#  * @author [Limm-jk]
#  * @email [201602057@cs-cnu.org]
#  * @create date 2020-12-06 20:16:14
#  * @modify date 2020-12-06 20:16:14
#  * @desc [DB와 연동하기 위한 정보들을 저장]
#  */


import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'review_site.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "chananbabo"

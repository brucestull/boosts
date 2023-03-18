from django.test import TestCase
from django.urls import reverse

from boosts.models import Inspirational
from accounts.models import CustomUser

SERVER_ROOT = "http://localhost:8000"

A_CUSTOM_USER_USERNAME = 'ACustomUser'

INSPIRATIONAL_LIST_URL = "/boosts/inspirationals/"
INSPIRATIONAL_LIST_VIEW_NAME = "boosts:inspirational-list"
INSPIRATIONAL_LIST_TEMPLATE = "boosts/inspirational_list.html"

PAGE_TITLE_INSPIRATIONAL_LIST = "Inspirational List"

NUMBER_OF_INSPIRATIONALS = 13

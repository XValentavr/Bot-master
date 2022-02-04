"""
This module use amoCRM api to enter data
"""

from amocrm_api import AmoLegacyClient
from amocrm_api import AmoOAuthClient

client = AmoLegacyClient(
    "olga.ivanova@genealogy.boutique", "vanilla0655", "https://www.amocrm.ru/"
)
print(client)

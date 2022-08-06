"""
This module send letter to email using info from registration form
"""
import os

import requests


class CreateRequest:
    def __init__(self):
        self.url = os.getenv("url")
        self.__form_indetifier = os.getenv("form")

    @property
    def form_indetifier(self):
        return self.__form_indetifier


def send_request(user_dict: dict):
    """
    This funsction sends request to salesdrive CRM
    :param: user_dict: dict of user information entered in chat
    :return: None
    """

    salesdrivereq = CreateRequest()
    json = {
        "form": salesdrivereq.form_indetifier,
        "getResultData": 1,
        "products": [
            {
                "id": "",
                "name": "",
                "costPerItem": "",
                "amount": "",
                "description": "",
                "discount": "",
                "sku": "",
            }
        ],
        "comment": "",
        "fName": user_dict["name"],
        "lName": "",
        "mName": "",
        "phone": user_dict["phone"],
        "email": user_dict["email"],
        "con_comment": user_dict["info"],
        "sajt": "Бот КМК",
        "con_telegram": "",
        "organizationId": "",
        "prodex24source_full": "",
        "prodex24source": "",
        "prodex24medium": "",
        "prodex24campaign": "",
        "prodex24content": "",
        "prodex24term": "",
        "prodex24page": "",
    }
    requests.post(
        salesdrivereq.url, json=json, headers={"Content-type": "application/json"}
    )

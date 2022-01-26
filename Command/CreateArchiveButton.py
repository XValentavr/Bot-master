"""
This module create archive buttons to show contact and adress
"""


def create_info_about_archive() -> (list, list, list):
    """
    This module initialize archive name list, site list and coordinates to find in a map
    :return: lists of archives inforamtion
    """
    archive = [
        "Державна архівна служба України\n",
        "\nУкраїнський науково-дослідний інститут архівної справи та документознавства\n",
        "\nЦентральний державний архів вищих органів влади та управління України\n",
        "\nЦентральний державний архів громадських об’єднань України\n",
        "\nЦентральний державний історичний архів України м. Київ\n",
        "\nЦентральний державний історичний архів України м. Львів\n",
        "\nЦентральний державний кінофотофоноархів України ім. Г. С. Пшеничного\n",
        "\nЦентральний державний науково-технічний архів України\n",
        "\nЦентральний державний архів-музей літератури і мистецтва України\n",
        "\nЦентральний державний архів зарубіжної україніки\n",
        "\nЦентральний державний електронний архів України\n",
        "\nДержавний архів в Автономній Республіці Крим",
        "\nДержавний архів Вінницької області\n",
        "\nДержавний архів Волинської області\n",
        "\nДержавний архів Дніпропетровської області\n",
        "\nДержавний архів Донецької області\n",
        "\nДержавний архів Житомирської області\n",
        "\nДержавний архів Закарпатської області\n",
        "\nДержавний архів Запорізької області\n",
        "\nДержавний архів Івано-Франківської області\n",
        "\nДержавний архів Київської області\n",
        "\nДержавний архів Кіровоградської області\n",
        "\nДержавний архів Луганської області\n",
        "\nДержавний архів Львівської області\n",
        "\nДержавний архів Миколаївської області\n",
        "\nДержавний архів Одеської області\n",
        "\nДержавний архів Полтавської області\n",
        "\nДержавний архів Сумської області\n",
        "\nДержавний архів Тернопільської області\n",
        "\nДержавний архів Харківської області\n",
        "\nДержавний архів Херсонської області\n",
        "\nДержавний архів Хмельницької області\n",
        "\nДержавний архів Черкаської області\n",
        "\nДержавний архів Чернівецької області\n",
        "\nДержавний архів Чернігівської області\n",
        "\nДержавний архів міста Києва\n",
        "\nДержавний архів міста Севастополя\n",
    ]

    site = [
        "http://www.archives.gov.ua",
        "http://undiasd.archives.gov.ua/",
        "http://tsdavo.gov.ua/",
        "http://cdago.gov.ua/",
        "http://cdiak.archives.gov.ua/",
        "http://tsdial.archives.gov.ua/",
        "http://tsdkffa.archives.gov.ua/",
        "http://www.archive.gov.ua/",
        "http://csam.archives.gov.ua/",
        "http://tsdazu.gov.ua/",
        "http://tsdea.archives.gov.ua/",
        "http://krymgosarchiv.ru/",
        "http://davio.gov.ua/",
        "http://volyn.archives.gov.ua/",
        "http://dp.archives.gov.ua/",
        "http://dn.archives.gov.ua/",
        "http://archive.zt.gov.ua/",
        "http://dazo.gov.ua/",
        "http://www.archivzp.gov.ua/",
        "http://if.archives.gov.ua/",
        "http://dako.gov.ua/",
        "http://dakiro.kr-admin.gov.ua/",
        "http://lg.archives.gov.ua/",
        "http://archivelviv.gov.ua/",
        "http://mk.archives.gov.ua/",
        "http://archive.odessa.gov.ua/",
        "http://poltava.archives.gov.ua/",
        "http://rv.archives.gov.ua/",
        "http://daso.sumy.ua/",
        "https://te.archives.gov.ua/",
        "http://archives.kh.gov.ua/",
        "http://kherson.archives.gov.ua/",
        "http://www.dahmo.gov.ua/",
        "http://ck.archives.gov.ua/",
        "http://cv.archives.gov.ua/",
        "http://cn.archives.gov.ua/",
        "http://www.kiev-arhiv.gov.ua/",
        "http://sev.archives.gov.ua/",
    ]

    coodrinates = [
        "https://goo.gl/maps/urMGqJ74oHZMDaJD9",
        "https://goo.gl/maps/y4UjLSSpgkzjBYKe8",
        "https://goo.gl/maps/r4qoMp7VjTcHXo9q8",
        "https://goo.gl/maps/WUevrFcTvF59nUt96",
        "https://goo.gl/maps/S4cB6pjqnwuzJght6",
        "https://goo.gl/maps/2tzg9BuzySsfLmes8",
        "https://goo.gl/maps/yWnjtDErhZzU1hQc8",
        "https://goo.gl/maps/ypCn5KeZ8Vh5j5ZK8",
        "https://g.page/CSAMLA_of_Ukraine?share",
        "https://goo.gl/maps/TuUgqPaJ6Q8fFCQRA",
        "https://goo.gl/maps/8JDtyCPkTm8mQeSJ9",
        "https://goo.gl/maps/CTvacpyuCrpw4Dsb8",
        "https://goo.gl/maps/8cr1GZazJY8pVKpw9",
        "https://goo.gl/maps/2wBAoxR93zhxaSrQ9",
        "https://goo.gl/maps/y1DTtg1ByWUGr6QU6",
        "https://goo.gl/maps/iHopkFSAmLeHkHUx5",
        "https://goo.gl/maps/PjSKH9wiijzjmc3M8",
        "https://goo.gl/maps/V9Yp9dodrd9bwnXNA",
        "https://goo.gl/maps/FjBVqCcb5cKkCy6AA",
        "https://goo.gl/maps/hAWeDqmTvDbWtH21A",
        "https://goo.gl/maps/AzSuFHYVeiiNNmVD9",
        "https://goo.gl/maps/43GSisSa8aHWhkQ5A",
        "https://goo.gl/maps/SgWA42KUV6TP6EFc6",
        "https://goo.gl/maps/VsPJpkj97FbiPaZX8",
        "https://goo.gl/maps/64CKTcF1oHreoU969",
        "https://goo.gl/maps/tf2oE8e5PozGR3Fn8,\n https://goo.gl/maps/ZAmiPSrE2LwtJDwM6",
        "https://goo.gl/maps/hZ1cfuZmem63Coe1A,\n https://goo.gl/maps/fN36V3a1LfRADt2m6",
        "https://goo.gl/maps/6DDJrB627dYg2xbh7",
        "https://goo.gl/maps/oCUsokZpWN868ecd8",
        "https://goo.gl/maps/4tDYqzjbAc6YhjzH8",
        "https://goo.gl/maps/m2AWfEXndPi91vNk8",
        "https://goo.gl/maps/2Ljjj1iySJs3RnTr5",
        "https://goo.gl/maps/NjWbJkeCADvs35Yj8",
        "https://goo.gl/maps/RhGb7v9jqt84KYm37",
        "https://goo.gl/maps/rmM8XFj9dBBv8Hj17",
        "https://goo.gl/maps/1vZneGyKjMWJexn26",
        "",
    ]
    return archive, site, coodrinates


def show_archive(bot, call):
    """
    This module set archive information to bot chat
    :param bot: telegram bot api
    :param call: message chat id
    :return: None
    """
    archive, site, coordinates = create_info_about_archive()
    message = " ".join([str(elem) for elem in generate_mes(archive, site, coordinates)])
    if len(message) > 4096:
        for x in range(0, len(message), 4096):
            bot.send_message(
                call.chat.id,
                message[x: x + 4096],
                parse_mode="Markdown",
                disable_web_page_preview=True,
            )
    else:
        bot.send_message(
            call.chat.id, message, parse_mode="Markdown", disable_web_page_preview=True
        )


def generate_mes(archive: list, site: list, coordinates: list) -> list:
    """
    Creates messange to send to chat
    :param archive: list of archive name
    :param site: site of each archive
    :param coordinates: map coordinates in google
    :return: new combine list
    """
    message = []
    for index in range(len(archive)):
        message.append(
            "\n"
            + archive[index]
            + " *Официальный сайт\n*"
            + site[index].strip()
            + "\t"
            + "*Месторасположение*\n"
            + coordinates[index]
        )
    return message

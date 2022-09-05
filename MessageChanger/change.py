from MessageChanger.kyiv_archive import kyiv
from MessageChanger.not_kyiv_archive import not_kyiv
import shlex


def changer(message: dict) -> str:
    return table_blueprint(
        message.get("archive"),
        message.get("village"),
        message.get("county"),
        message.get("province"),
        message.get("church"),
        message.get("birth"),
        message.get("death"),
        message.get("wedding"),
        message.get("additional"),
        message.get("testament"),
    )


def table_blueprint(
        archive,
        village,
        county,
        province,
        church,
        birth,
        death,
        wedding,
        additional,
        testament,
) -> str:
    """
    This module creates table blueprint
    :return: blueprint of table
    """
    p_lambda = lambda prvnc: prvnc.split(",")[0].strip()

    last_td = td = "".join([" " for _ in range(2)])
    table = (
        f"{f'*{archive.strip().upper()}'}*\n"
        f"{f'{village.strip()}'}\n"
        f"{f'{county.strip()}, {p_lambda(province.strip())}'}\n"
        f"{f'{church.strip()}'}\n"
        f"\n"
        f"*{metric_title(birth.upper()) if metric_title(birth) else None}*\n\n"
        f"`|Фонд|{td}|Опис|{td}|Справа|{last_td}|Рік|`\n\n"
    )
    year, fund, description, case = metrics_changer(birth, archive)

    table = generator_of_message(
        table,
        year,
        fund,
        description,
        case,
    )

    # for death metrics
    table += f"\n\n*{metric_title(death.upper()) if metric_title(death) else None}*\n\n"
    table += f"`|Фонд|{td}|Опис|{td}|Справа|{last_td}|Рік|`\n\n"
    year, fund, description, case = metrics_changer(death, archive)
    table = generator_of_message(table, year, fund, description, case)

    # for wedding metrics
    table += (
        f"\n\n*{metric_title(wedding.upper()) if metric_title(wedding) else None}*\n\n"
    )
    table += f"`|Фонд|{td}|Опис|{td}|Справа|{last_td}|Рік|`\n\n"
    year, fund, description, case = metrics_changer(wedding, archive)
    table = generator_of_message(table, year, fund, description, case)

    # for additional metrics
    if additional.strip() != "" or testament.strip() != "":
        table += f"\n\n*СПОВІДНІ ВІДОМОСТІ*\n\n"
        table += f"`|Фонд|{td}|Опис|{td}|Справа|{last_td}|Рік|`\n\n"
        year, fund, description, case = metrics_changer(additional, archive)
        table = generator_of_message(table, year, fund, description, case)

        year, fund, description, case = metrics_changer(testament, archive)
        table = generator_of_message(
            table,
            year,
            fund,
            description,
            case,
        )

    return table


def metric_title(metric: str) -> str | None:
    """
    This function gets metric title
    :param metric:  metric to get title
    :return: title
    """
    if metric is not None:
        return metric.split("\n")[0].replace("*", "")
    return None


def metrics_changer(metric: str, archive: str) -> [list, list, list, list]:
    """
    This module change metric string to table
    :param metric: string to change
    :return:  new string to enter into table
    """
    if metric is None:
        return None
    data = metric.split("\n")
    del data[0]
    for i, d in enumerate(data):
        if data[i] == "" or data[i] == " ":
            del data[i]
    if "історичний архів в м. Київ" not in archive:
        return not_kyiv(data)
    else:
        return kyiv(data)


def generator_of_message(
        table: str,
        year: list,
        fund: list,
        description: list,
        case: list,
) -> str:
    """
    This function generate full message
    :param table: string to add new info
    :param year: list of years
    :param fund: list of funds
    :param description: list of descriptions
    :param case: list of cases
    :return: final message
    """
    td = "".join([" " for _ in range(2)])
    for data in range(len(year)):
        fund_1 = count_tabs(fund[data], "fund")
        description_1 = count_tabs(description[data], "description")
        case_1 = count_tabs(case[data], "case")
        table += f"`{fund_1}{td}{description_1}{td}{case_1}{td}{year[data]}`\n"
    return table


def count_tabs(data, where):
    if where == "fund":
        if data is not None:
            while len(data) <= len("Фонд") - 1:
                data += " "
            data = "|" + data + "|"
            return data
        return None
    if where == "description":
        if data is not None:
            while len(data) <= len("Опис") - 1:
                data += " "
            data = "|" + data + "|"
            return data
        return None
    if where == "case":
        if data is not None:
            while len(data) <= len("Справа") - 1:
                data += " "
            data = "|" + data + "|"
            return data
        return None

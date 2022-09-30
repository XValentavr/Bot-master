def checker_date(fund, case, year, description):
    """
    This module check if data is in diapazone
    :param fund: fund data
    :param case: case data
    :param year: year to check
    :param description: description data
    :return: if true then changed list of data else do nothing
    """
    new_year = []
    new_case = []
    new_fund = []
    new_description = []
    for i, _ in enumerate(year):
        if year[i] is not None:
            if ',' in year[i]:
                list_of_years = year[i].split(',')
                range_ = None
                for yrs in list_of_years:
                    if '-' in yrs:
                        range_ = yrs.replace('|', '').split('-')
                    elif '–' in yrs:
                        range_ = yrs.replace('|', '').split('–')
                    if range_:
                        if not range_[0].strip().startswith('1'):
                            range_[0] = '1' + range_[0]
                        print(yrs)
                        for index in range(int(range_[0].strip()), int(range_[1].strip()) + 1):
                            new_year.append("|" + str(index) + "|")
                            new_description.append(description[i])
                            new_fund.append(fund[i])
                            new_case.append(case[i])
            else:
                if '.' not in year[i]:
                    range_ = None
                    if '-' in year[i]:
                        range_ = year[i].replace('|', '').split('-')
                    elif '–' in year[i]:
                        range_ = year[i].replace('|', '').split('–')
                    if range_:
                        if not range_[0].strip().startswith('1'):
                            range_[0] = '1' + range_[0]
                        for index in range(int(range_[0].strip()), int(range_[1].strip()) + 1):
                            new_year.append("|" + str(index) + "|")
                            new_description.append(description[i])
                            new_fund.append(fund[i])
                            new_case.append(case[i])

                    else:
                        new_year.append(year[i])
                        new_description.append(description[i])
                        new_fund.append(fund[i])
                        new_case.append(case[i])
                else:
                    new_year.append(year[i])
                    new_description.append(description[i])
                    new_fund.append(fund[i])
                    new_case.append(case[i])
    return new_year, new_fund, new_description, new_case


def checker_case(fund, case, year, description):
    """
        This module check if case is multiple
    :param fund: fund data
    :param case: case data
    :param year: year to check
    :param description: description data
    :return: if true then changed list of data else do nothing
    """
    new_year = []
    new_case = []
    new_fund = []
    new_description = []
    for i, _ in enumerate(case):
        if case[i] is not None:
            if ',' in case[i]:
                list_of_cases = case[i].split(',')
                for cs in list_of_cases:
                    if 'арк.' in cs:
                        continue
                    range_ = None
                    if '-' in cs:
                        range_ = cs.replace('|', '').split('-')
                    elif '–' in cs:
                        range_ = cs.replace('|', '').split('–')
                    if range_:
                        for index in range(int(range_[0].strip()), int(range_[1].strip()) + 1):
                            new_year.append(year[i])
                            new_description.append(description[i])
                            new_fund.append(fund[i])
                            new_case.append(str(index).strip())
                    else:
                        new_year.append(year[i])
                        new_description.append(description[i])
                        new_fund.append(fund[i])
                        new_case.append(cs.strip())
            else:
                new_year.append(year[i])
                new_description.append(description[i])
                new_fund.append(fund[i])
                new_case.append(case[i])
    return new_year, new_fund, new_description, new_case

def del_if_64(text, counter):
    """
    This module trim church if encode length more than 64.
    :param text: list of church
    :param counter: length of church
    :return: new trunc list
    """
    index = counter - 1
    final_global_counties = [None for _ in range(len(text))]
    for i in text:
        new_county = str(i)
        if '(Харківське військове поселення)' in new_county:
            new_county = new_county.replace('(Харківське військове поселення)', '')
        while (len(new_county.encode("utf-8"))) > 64:
            new_county = new_county.split()
            new_county.pop()
            new_county = " ".join(map(str, new_county))
        final_global_counties[index] = new_county.strip()
        index -= 1
    return list(set(final_global_counties))

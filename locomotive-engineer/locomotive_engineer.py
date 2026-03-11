"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args) -> list:
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return list(args)


def fix_list_of_wagons(each_wagons_id, missing_wagons) -> list:
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    first, second, one, *tail = each_wagons_id
    *result, = one, *missing_wagons, *tail, first, second
    return result
     


def add_missing_stops(from_to_dict, **stops_dict) -> dict:
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    stops_list = list(stops_dict.values())
    stops =dict(stops = stops_list)
    result = {**from_to_dict, **stops}
    return result


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    return {**route, **more_route_information}


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    result = [list(x) for x in zip(*wagons_rows)]
    return result

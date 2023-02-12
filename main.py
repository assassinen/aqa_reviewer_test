def get_distance_surcharge(distance):
    """
    *расстояния до пункта назначения:*

    - более 30 км: +300 рублей к доставке;
    - до 30 км: +200 рублей к доставке;
    - до 10 км: +100 рублей к доставке;
    - до 2 км: +50 рублей к доставке;
    """
    if distance < 2:
        return 50
    elif distance >= 2 and distance < 10:
        return 100
    elif distance >= 10 and distance < 30:
        return 200
    elif distance >= 30:
        return 300


def get_cargo_size_surcharge(big_size):
    """
    *габаритов груза:*
    - большие габариты: +200 рублей к доставке;
    - маленькие габариты: +100 рублей к доставке;
    """
    return 200 if big_size else 100


def get_fragility_of_cargo_surcharge(is_fragile):
    """
    Если груз хрупкий — +300 рублей к доставке
    """
    return 300 if is_fragile else 0


def get_workload_surcharge(workload='normal'):
    """
    Стоимость умножается на коэффициент доставки:
    - очень высокая загруженность — 1.6;
    - высокая загруженность — 1.4;
    - повышенная загруженность — 1.2;
    - во всех остальных случаях коэффициент равен 1.
    """
    workloads = {'normal': 1,
                 'high': 1.2,
                 'very_high': 1.4,
                 'extra_high': 1.6,
                 }
    workload = workload if workload in workloads else 'normal'
    return workloads[workload]


def is_possibility_delivery(distance, is_big_size, is_fragile, workload):
    """
    проверяем тип входных параметров и то, что xрупкие грузы нельзя возить на расстояние более 30 км;
    """
    return isinstance(is_big_size, bool) \
           and isinstance(is_fragile, bool) \
           and isinstance(workload, str) \
           and (isinstance(distance, float) or isinstance(distance, int))\
           and not(is_fragile and distance > 30)


def get_delivery_price(distance, is_big_size, is_fragile, workload):
    """

    :param distance: float or int
    :param is_big_size: bool
    :param is_fragile: bool
    :param workload: str -> [normal, high, very_high, extra_high]
    :return: delivery_price: float
    """
    min_price = 400
    price = 0

    if is_possibility_delivery(distance, is_big_size, is_fragile, workload):
        price += get_distance_surcharge(distance)
        price += get_cargo_size_surcharge(is_big_size)
        price += get_fragility_of_cargo_surcharge(is_fragile)
        price *= get_workload_surcharge(workload)
        return max(price, min_price)
    else:
        return -1

print(get_delivery_price(distance=31,
                         is_big_size=True,
                         is_fragile=True,
                         workload='very_high')
      )

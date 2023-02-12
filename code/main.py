def get_distance_surcharge(distance):
    """
    *расстояния до пункта назначения:*

    - более 30 км: +300 рублей к доставке;
    - до 30 км: +200 рублей к доставке;
    - до 10 км: +100 рублей к доставке;
    - до 2 км: +50 рублей к доставке;
    """
    if not (isinstance(distance, int) or isinstance(distance, float)):
        return -1

    if distance > 0 and distance < 2:
        return 50
    elif distance >= 2 and distance < 10:
        return 100
    elif distance >= 10 and distance < 30:
        return 200
    elif distance >= 30:
        return 300
    else:
        return -1


def get_cargo_size_surcharge(length, width, height):
    """
    *габаритов груза:*

    - большие габариты (>= 150 см в сумме трёх измерений): +200 рублей к доставке;
    - маленькие габариты (< 150 см в сумме трёх измерений): +100 рублей к доставке;
    """
    if not (isinstance(length, int) and isinstance(width, int) and isinstance(height, int)) \
            or length <= 0 or width <= 0 or height <= 0:
        return -1

    is_big_size = sum((length, width, height)) >= 150
    return 200 if is_big_size else 100


def get_fragility_of_cargo_surcharge(is_fragile):
    """
    Если груз хрупкий — +300 рублей к доставке
    """
    if not isinstance(is_fragile, bool):
        return -1

    return 300 if is_fragile else 0


def get_workload_surcharge(workload='normal'):
    """
    Стоимость умножается на коэффициент доставки:
    - очень высокая загруженность — 1.6;
    - высокая загруженность — 1.4;
    - повышенная загруженность — 1.2;
    - во всех остальных случаях коэффициент равен 1.
    """
    if not isinstance(workload, str):
        return -1

    workloads = {'normal': 1,
                 'high': 1.2,
                 'very_high': 1.4,
                 'extra_high': 1.6,
                 }
    workload = workload if workload in workloads else 'normal'
    return workloads[workload]


def is_possibility_delivery(distance, is_fragile):
    """
    проверяем тип входных параметров и то, что xрупкие грузы нельзя возить на расстояние более 30 км;
    """
    return not(is_fragile and distance > 30)


def get_delivery_price(distance, length, width, height, is_fragile, workload):
    """

    :param distance: float or int
    :param length: int
    :param width: int
    :param height: int
    :param is_fragile: bool
    :param workload: str -> [normal, high, very_high, extra_high]
    :return: delivery_price: float
    """
    min_price = 400
    price = 0

    distance_surcharge = get_distance_surcharge(distance)
    cargo_size_surcharge = get_cargo_size_surcharge(length, width, height)
    fragility_of_cargo_surcharg = get_fragility_of_cargo_surcharge(is_fragile)
    workload_surcharg = get_workload_surcharge(workload)

    if is_possibility_delivery(distance, is_fragile) \
            and distance_surcharge != -1 \
            and cargo_size_surcharge != -1 \
            and fragility_of_cargo_surcharg != -1 \
            and workload_surcharg != -1:
        price += sum((distance_surcharge, cargo_size_surcharge, fragility_of_cargo_surcharg))
        price *= get_workload_surcharge(workload)
        return max(round(price, 2), min_price)
    else:
        return -1

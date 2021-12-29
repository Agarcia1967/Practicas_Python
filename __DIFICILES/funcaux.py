from datetime import datetime

def hms(segundos:int)->str:
    """
    Devuelve un string en formato hh:mm:ss a partir de un tiempo en segundos
    """
    h : int = segundos // 3600
    m : int = (segundos -  h * 3600) // 60
    s : int = (segundos - h * 3600 - m * 60)
    return "%02d:%02d:%02d"%(h,m,s)

def datetime_to_float(fecha:datetime)->float:
    """
    Devuelve el numero de segundos de una fecha desde las 00 del dia
    """
    epoch = fecha.utcfromtimestamp(0)
    total_seconds =  (fecha - epoch).total_seconds()
    return total_seconds

def test_hms():
    assert hms(0)=="00:00:00"
    assert hms(86400)=="24:00:00"

def test_datetime_to_floar():
    d  =  datetime.strptime('2021-10-09T12:00:00Z','%Y-%m-%dT%H:%M:%SZ')
    assert datetime_to_float(d) == 1633780800.0
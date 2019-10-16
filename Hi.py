def calcularHeatIndex(tc, rh):
    t = (1.8*tc) + 32 
    firstHeatIndex = (1.1*t) - 10.3 + (0.047*rh)

    if (firstHeatIndex < 80):
        result = firstHeatIndex
    else:
        firstHeatIndex = -42.379 + (2.04901523 * t) + (10.14333127 * rh) - (0.22475541 * t * rh) - (6.83783 * (10**-3) * (t**2)) - (5.481717 * (10**-2) * (rh**2)) + (1.22874 * (10**-3) * (t**2) * rh) + (8.5282 * (10**-4) * t * (rh**2)) - (1.99 * (10**-6) * (t**2) * (rh**2))
        if ( ((t >= 80) and (t <= 112)) and (rh<=13)):
            result = firstHeatIndex - (3.25 - (0.25 * rh)) * (( (17 - abs(t-95))/17) ** 0.5)
        elif ( ((t >= 80) and (t <= 87)) and (rh > 85)):
            result = firstHeatIndex + (0.02 * (rh - 85) * (87 - 5))
        else:
            result = firstHeatIndex

    return (result-32)/1.8

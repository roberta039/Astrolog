import swisseph as swe
import math
from datetime import datetime

def calculate_chart(year, month, day, hour, minute, latitude, longitude):
    try:
        # Convert local time to UTC Julian Day
        jd = swe.julday(year, month, day, hour + minute / 60.0)
        swe.set_topo(longitude, latitude, 0)

        # --- PLANETS ---
        planet_list = [
            (swe.SUN, "Sun"),
            (swe.MOON, "Moon"),
            (swe.MERCURY, "Mercury"),
            (swe.VENUS, "Venus"),
            (swe.MARS, "Mars"),
            (swe.JUPITER, "Jupiter"),
            (swe.SATURN, "Saturn"),
            (swe.URANUS, "Uranus"),
            (swe.NEPTUNE, "Neptune"),
            (swe.PLUTO, "Pluto")
        ]

        planets = {}
        for pid, name in planet_list:
            result = swe.calc_ut(jd, pid)
            # Extract longitude safely
            lon = result[0][0] if isinstance(result[0], (list, tuple)) else result[0]
            planets[name] = round(float(lon), 2)

        # --- HOUSES (Placidus system) ---
        houses, ascmc = swe.houses(jd, latitude, longitude)
        houses_data = {str(i + 1): round(houses[i], 2) for i in range(12)}

        # --- ASPECTS ---
        aspect_angles = {
            "Conjunction": 0,
            "Sextile": 60,
            "Square": 90,
            "Trine": 120,
            "Opposition": 180
        }
        aspect_orb = 6.0  # degrees tolerance
        aspects = []

        planet_names = list(planets.keys())
        for i in range(len(planet_names)):
            for j in range(i + 1, len(planet_names)):
                p1, p2 = planet_names[i], planet_names[j]
                lon1, lon2 = planets[p1], planets[p2]
                diff = abs(lon1 - lon2)
                if diff > 180:
                    diff = 360 - diff
                for name, angle in aspect_angles.items():
                    if abs(diff - angle) <= aspect_orb:
                        aspects.append(f"{p1} {name} {p2} ({round(diff, 2)}°)")

        return {
            "julian_day": jd,
            "planets": planets,
            "houses": houses_data,
            "aspects": aspects
        }

    except Exception as e:
        return {"error": str(e)}

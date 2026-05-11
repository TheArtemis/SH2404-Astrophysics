from __future__ import annotations
from datetime import datetime
from enum import Enum

class Declination:
    def __init__(self, degree: int, arcminute: int = 0):
        if not 0 <= arcminute < 60:
            raise ValueError("arcminute must be between 0 and 59")

        sign = -1 if degree < 0 else 1
        total_arcminutes = sign * ((abs(degree) * 60) + arcminute)
        if not -(90 * 60) <= total_arcminutes <= 90 * 60:
            raise ValueError("declination must be between -90° and 90°")

        self.total_arcminutes = total_arcminutes

    @property
    def degree(self) -> int:
        sign = -1 if self.total_arcminutes < 0 else 1
        return sign * (abs(self.total_arcminutes) // 60)

    @property
    def arcminute(self) -> int:
        return abs(self.total_arcminutes) % 60

    @property
    def decimal_degrees(self) -> float:
        return self.total_arcminutes / 60

    def __str__(self) -> str:
        sign = "-" if self.total_arcminutes < 0 else ""
        return f"{sign}{abs(self.degree)}° {self.arcminute:02d}'"


class Direction(Enum):
    NORTH = "north"
    SOUTH = "south"
    EAST = "east"
    WEST = "west"
    NORTHEAST = "northeast"
    NORTHWEST = "northwest"
    SOUTHEAST = "southeast"
    SOUTHWEST = "southwest"

class SiderealTime:
    def __init__(self, hour: int, minute: int, second: int):
        total_seconds = (hour * 60 * 60) + (minute * 60) + second
        total_seconds %= 24 * 60 * 60

        self.hour = total_seconds // (60 * 60)
        self.minute = (total_seconds % (60 * 60)) // 60
        self.second = total_seconds % 60

    @property
    def total_seconds(self) -> int:
        return (self.hour * 60 * 60) + (self.minute * 60) + self.second

    def __add__(self, other: SiderealTime) -> SiderealTime:
        if not isinstance(other, SiderealTime):
            return NotImplemented

        return SiderealTime(0, 0, self.total_seconds + other.total_seconds)

    def __sub__(self, other: SiderealTime) -> SiderealTime:
        if not isinstance(other, SiderealTime):
            return NotImplemented

        return SiderealTime(0, 0, self.total_seconds - other.total_seconds)

    def __str__(self) -> str:
        return f"{self.hour:02d}h {self.minute:02d}m {self.second:02d}s"

    

    # March 20 at 12:00:00 UTC
    @staticmethod
    def vernal_equinox(year: int) -> datetime:
        return datetime(year, 3, 20, 12, 0, 0)

# We reuse the SiderealTime class to represent the right ascension
RightAscension = SiderealTime

def get_sidereal_time(observation_time: datetime) -> SiderealTime:
    # The vernal equinox is on March 20 at 12:00:00 UTC
    # The 0th hour moves 4 minutes per day since the vernal equinox

    vernal_equinox = SiderealTime.vernal_equinox(observation_time.year)
    if observation_time < vernal_equinox:
        vernal_equinox = SiderealTime.vernal_equinox(observation_time.year - 1)

    elapsed_seconds = (observation_time - vernal_equinox).total_seconds()
    days_since_vernal_equinox = elapsed_seconds / (24 * 60 * 60)

    # Calculate the sidereal time
    extra_seconds = round(days_since_vernal_equinox * 4 * 60)
    return SiderealTime(0, 0, round(elapsed_seconds) + extra_seconds)

def get_hour_angle(sidereal_time: SiderealTime, right_ascension: RightAscension) -> SiderealTime:
    return sidereal_time - right_ascension

def get_direction(sidereal_time: SiderealTime, right_ascension: RightAscension) -> Direction:
    hour_angle = get_hour_angle(sidereal_time, right_ascension)
    # 0h=South,	6h=West, 12h=North and	18h=East
    if hour_angle.total_seconds == 0:
        return Direction.SOUTH

    if hour_angle.total_seconds < 6 * 60 * 60:
        return Direction.SOUTHWEST

    if hour_angle.total_seconds == 6 * 60 * 60:
        return Direction.WEST

    if hour_angle.total_seconds < 12 * 60 * 60:
        return Direction.NORTHWEST

    if hour_angle.total_seconds == 12 * 60 * 60:
        return Direction.NORTH

    if hour_angle.total_seconds < 18 * 60 * 60:
        return Direction.NORTHEAST

    if hour_angle.total_seconds == 18 * 60 * 60:
        return Direction.EAST

    return Direction.SOUTHEAST

def get_maximum_altitude(declination: Declination, latitude: Declination) -> float:
    return declination.decimal_degrees + 90 - latitude.decimal_degrees

def get_minimum_altitude(declination: Declination, latitude: Declination) -> float:
    return 90 - latitude.decimal_degrees - declination.decimal_degrees

if __name__ == "__main__":
    # Vernal equinox
    print(get_sidereal_time(datetime(2026, 3, 20, 12, 0, 0)))

    # 14th of February 2026 at 12:00:00 UTC
    print(get_sidereal_time(datetime(2026, 2, 14, 12, 0, 0)))
    # Answer: 22h 04m 00s

    # 14th of February 2026 at 18:00:00 UTC
    print(get_sidereal_time(datetime(2026, 2, 14, 18, 0, 0)))
    # Answer: 04h 05m 00s

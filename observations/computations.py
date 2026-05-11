from __future__ import annotations
from datetime import datetime


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


if __name__ == "__main__":
    # Vernal equinox
    print(get_sidereal_time(datetime(2026, 3, 20, 12, 0, 0)))

    # 14th of February 2026 at 12:00:00 UTC
    print(get_sidereal_time(datetime(2026, 2, 14, 12, 0, 0)))
    # Answer: 22h 04m 00s

    # 14th of February 2026 at 18:00:00 UTC
    print(get_sidereal_time(datetime(2026, 2, 14, 18, 0, 0)))
    # Answer: 04h 05m 00s

"""
    This file is part of GCA Analysis Tool.

    Copyright (C) 2020 Oscar Franzén <oscarfranzen@protonmail.com>

    GCA Analysis Tool is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    GCA Analysis Tool is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with GCA Analysis Tool. If not, see <https://www.gnu.org/licenses/>.

"""

import datetime as dt

def to_datetime(qdate, qtime):
    year = qdate.year()
    month = qdate.month()
    day = qdate.day()
    hour = qtime.hour()
    minute = qtime.minute()
    second = qtime.second()
    return dt.datetime(year, month, day, hour, minute, second)



def partition(datetimes):
    current_partition = []
    partitioned_datetimes = []
    previous_datetime = None

    for datetime in datetimes:

        if previous_datetime == None:

            previous_datetime = datetime

            current_partition.append(datetime)

        else:

            if datetime < previous_datetime:

                datetime += dt.timedelta(days=1)

            elif (datetime - previous_datetime) < dt.timedelta(seconds=5000):

                current_partition.append(datetime)
                
            else:

                partitioned_datetimes.append(current_partition)

                current_partition = []
                    
                current_partition.append(datetime)

        previous_datetime = datetime

    if len(current_partition) > 0:

        partitioned_datetimes.append(current_partition)

    return partitioned_datetimes
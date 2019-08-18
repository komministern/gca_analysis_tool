
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
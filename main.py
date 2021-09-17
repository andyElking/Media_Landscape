from eventregistry import *

er = EventRegistry()

q1 = QueryEventsIter(keywords="Wheel of Time")

q2 = QueryEventsIter(conceptUri="https://en.wikipedia.org/wiki/The_Wheel_of_Time_(TV_series)")

eventListByKeyword = list(q1.execQuery(er, sortBy="date", maxItems= 100))
print(len(eventListByKeyword))
print("\n")

commonEvents = list()

for event in q2.execQuery(er, sortBy="date", maxItems= 100):
    if (eventListByKeyword.__contains__(event)):
        commonEvents.append(event)


print("\n".join(commonEvents))
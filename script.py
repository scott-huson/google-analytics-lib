import analyticsLib as anaLib

client = "696969" #randomly generated string
tracking = "UA-129142756-1"

analytics = anaLib.analyticsObjects(client, tracking)

pageviewInfo = analytics.pageView("Home") #Gets the information for the first page.

print(pageviewInfo)
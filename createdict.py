from sea import get_attractions,loop

source_data = dict(get_attractions(loop))
def createdict(source_data):
    ds = []
    for i in source_data():
         #ds[source_data[i]['title']] == null:
        #if:
        ds[source_data[i]['title']] = ds[source_data[i]['title']]+","+source_data[i]
        #else:
        ds[source_data[i]['title']]['link'] = ds[source_data[i]['title']]['link']+","+source_data[i]['link']
    return(ds)
    #arr = dict(ds)

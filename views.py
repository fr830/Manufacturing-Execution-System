from django.shortcuts import render
# Create your views here.

def ViewBase(request):
    status_by_station=['-','A','-','-','-']
    status_by_object=['A']

    station_name=['Station 1','Station 2','Station 3','Station 4','Station 5']


    sbs_out = []
    sbo_out = []
    for i in range(len(station_name)):
        sbs_out.append(station_name[i]+'：'+status_by_station[i])

    sbo_out.append(status_by_object[0]+'：'+station_name[1])


    return render(request, 'base.html',{'status_by_station': sbs_out,
                                        'status_by_object': sbo_out,
                                        })

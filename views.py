from django.shortcuts import render
# Create your views here.

def ViewBase(request):
    status_by_station=['-','A','-','-','-'] #工作站矩陣
    status_by_object=['A'] #物件矩陣

    station_name=['Station 1','Station 2','Station 3','Station 4','Station 5'] #工作站名稱矩陣


    sbs_out = [] #工作站視角最後輸出字串
    sbo_out = [] #物件視角最後輸出字串
    for i in range(len(station_name)):
        sbs_out.append(station_name[i]+'：'+status_by_station[i]) #字串處理（結合名稱和狀態）

    sbo_out.append(status_by_object[0]+'：'+station_name[1]) #字串處理（結合名稱和狀態）


    #輸出參數至base.html
    return render(request, 'base.html',{'status_by_station': sbs_out,
                                        'status_by_object': sbo_out,
                                        })

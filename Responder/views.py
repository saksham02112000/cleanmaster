from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from sys import maxsize
from itertools import permutations
from .models import DevicePings
import pickle

@csrf_exempt

def func(dist, gas1, gas2, gas3):
    scaler = pickle.load(open('ML/scaler', 'rb'))
    reg1 = pickle.load(open('ML/rf', 'rb'))
    log = pickle.load(open('ML/LogisticModel', 'rb'))
    t = scaler.transform([[dist, gas1, gas2, gas3]])
    a = reg1.predict(t)[0]
    b = log.predict(t)[0]
    if dist >= 85:
        return ["90% capacity reached", b, 0]
    if b == True:
        return ["Gas Exceeds limits", b, 0]
    else:
        return ["Dustbin Safe to use till ", b, a]


def handler(request):
    if request.method == "POST":
        print(request.body)
        try:
            parse = json.load(request)
            print(parse)
        except:
            raise Exception("Not able to parse")

    return HttpResponse("Welcome to IOT")


def xyz(request):
    if request.method == "POST":
        print(request.body)
        try:
            client_id = request.body["client_id"]
            print(client_id)
        except:
            raise Exception("Not able to parse")


# //source, dest
def trav(request):
    if request.method=="GET":
        try:
            route_v=["Hostel-M","Hostel-K","Hostel-L","COS","H-hostel","H-block","Old Library","Library","Jaggi"]
            return JsonResponse({"route": route_v})
        except:
            raise Exception("Route not found")


def picked(request, client_id=1):
    if request.method == "POST":
        try:
            dbdata = DevicePings.objects.all()
            dustbin = dbdata.objects.get(client_id=client_id)
            dustbin.mq2reading = 0
            dustbin.mq3reading = 0
            dustbin.mq4reading = 0
            dustbin.save()
        except:
            raise Exception("Dustbin not found")


def masterreset(request):
    if request.method == "GET":
        try:
            # dustbin = DevicePings.objects.all()
            dustbin={}
            matrix_demo=return_dummy_set()
            demo={}
            # clear dustbin function
            for i in range(10):
                demo["client_id"] = matrix_demo[i][0]
                demo["dist_reading"] = matrix_demo[i][1]
                demo["mq2reading"] = matrix_demo[i][2]
                demo["mq3reading"] = matrix_demo[i][3]
                demo["mq4reading"] = matrix_demo[i][4]
                dustbin[matrix_demo[i][0]]= demo

            print(dustbin)
            return JsonResponse(dustbin)
        except:
            raise Exception("masterrreset failed")



def return_dummy_set():
    dummy_set = [[1, 8.96767778131896, 87.2082125938314, 16.8379036490526, 28.9336012739938],
                 [2, 80.1731393629776, 79.9021917953746, 55.7972793990095, 27.8783945396686],
                 [3, 91.7859853064276, 85.6312342447822, 11.6264354258183, 90.6243300823676],
                 [4, 59.9047105793823, 13.4340731486214, 94.3540378041737, 56.0223073260305],
                 [5, 73.3642917784595, 7.71140813495834, 14.5931937517691, 57.0737404042271],
                 [6, 75.3073848672983, 80.8028543234019, 75.3044913533533, 34.6208512715647],
                 [7, 8.58945970059132, 85.9084758621924, 92.1673184105358, 88.715621973651],
                 [8, 53.0723312578271, 36.1803311105915, 46.6428797004184, 65.7062893233451],
                 [9, 0.40813186569465, 14.8602870555449, 38.0140059436064, 73.7807156605876],
                 [10, 78.3158153769719, 66.4648755030589, 45.5825079923297, 39.1995784354457]]
    return dummy_set



# def delete_everything(self):
#     Reporter.objects.all().delete()
#
# def drop_table(self):
#     cursor = connection.cursor()
#     table_name = self.model._meta.db_table
#     sql = "DROP TABLE %s;" % (table_name, )
#     cursor.execute(sql)


# def algorithm(self, source, destination):


# func sab(self, ):
#     return shortest adge;

# void
# postRefreshML():
#
# void
# postRefresh():
# postRefreshMl()
# func(, newSrc)
#
# void
# picked(x):
# x.dustbins.stats = 0
#
# model
# dustbins:
# dist, gas1, gas2, Dust_number(!id), name
#
# void
# masterReset(x):
# // refill
# dummy
# garbage
# clearExistingData()
# stats = readJson()
from django.shortcuts import render
from .models import Candidate
# Create your views here.
from rest_framework import viewsets
from .serializers import CandidateSerializer
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
import json
import requests





class CandidateViewset(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer


    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def candidate_found(self, request):
        print('insider....')
        url = 'https://testapi.karza.in/v2/epf-auth/'
        uan = request.data.get("uan")
        consent = request.data.get("consent")
        name = request.data.get("name")
        # print(name.lower())
        payload = { "uan": uan, "consent": consent }
        payload = json.dumps(payload)
        headers = { "Content-Type": "application/json", "x-karza-key": "Cfjyb5T6U8BZqVko" } 
        print(type(payload))
        print(type(headers))
        # res = requests.post(url, data=payload, headers=headers)
        # print(response.text)
        res = '''{"result": {"summary": {"totalWorkExperienceInMonths": 21, "lastEmployer": {"dateOfJoining": "2019-10-30", "vintageInMonths": 4, "dateOfExit": null, "employerName": "VIRTUSA CONSULTING SERVICES (P) LTD"}}, "personalDetails": {"bankAccountStatus": "AVAILABLE", "aadhaarVerificationStatus": "AVAILABLE", "panVerificationStatus": "AVAILABLE", "name": "PRIYANKA JADHAV", "contactNo": null, "fatherOrHusbandName": "SHANKAR JADHAV"}, "employers": [{"dateOfJoining": "2019-10-30", "establishmentId": "APHYD0061537000", "memberId": "APHYD00615370000030551", "exitReason": null, "address": {"city": "RR DIST HYDERABAD", "state": "TELANGANA", "pincode": "500032", "district": "HYDERABAD", "address": "SYNO115 PART PLOT NO10 NANAKRAMGUDA VILLAGE SERLINGAMPALLI MANDAL"}, "establishmentName": "VIRTUSA CONSULTING SERVICES (P) LTD", "dateOfExit": null}, {"dateOfJoining": "2018-06-04", "establishmentId": "PYKRP0045053000", "memberId": "PYKRP00450530000056875", "exitReason": null, "address": {"city": "BELLANDUR VARTHUR HOBLI", "state": "KARNATAKA", "pincode": "560103", "district": null, "address": "SALARPURIA SOFT ZONE GRND FLR BLK B SALARPURIA SOFT ZONE GRND FLR BLK B"}, "establishmentName": "GENPACT INDIA PRIVATE LIMITED", "dateOfExit": null}]}, "request_id": "c8ff7ac7-4148-43ab-9d49-b6418a55aebc", "status-code": "101"}'''
        res = json.loads(res)
        print(type(res))
        print(res['result']['personalDetails']['name'])
        name_res = res['result']['personalDetails']['name']
        # name_res.lower()
        print('----', name, '----', name_res)
        if name == name_res:
            print('matched')
        else:
            print('not matched')
        # response_content = res.text
        # parsed_response = json.loads(response_content)
        return Response(res)

import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from attendees.models import Attendee


def get_attendees(request):
    attendees = [attendee.to_dict() for attendee in Attendee.objects.all()]
    return JsonResponse({'attendees': attendees}, status=200) 


def add_attendee(request):
    if request.method != 'POST':
        return HttpResponse('Method Not Allowed', status=405)

    params = json.loads(request.body)

    new_attendee = Attendee.objects.create(
        first_name=params['first_name'],
        last_name=params['last_name']
    )

    return JsonResponse(new_attendee.to_dict(), status=201)


def update_or_delete_attendee(request, attendee_id):
    if request.method not in ('PUT', 'DELETE'):
        return HttpResponse('Method Not Allowed', status=405)

    attendee = Attendee.objects.get(pk=attendee_id)

    if request.method == 'PUT':
        params = json.loads(request.body)

        attendee.first_name = params['first_name']
        attendee.last_name = params['last_name']
        attendee.save()

        return JsonResponse(attendee.to_dict(), status=200)

    if request.method == 'DELETE':
        attendee.delete()

        return HttpResponse('', status=204)


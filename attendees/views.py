import json

from django.shortcuts import redirect
from django.http import HttpResponse, JsonResponse

from attendees.models import Attendee


def index(request):
    return redirect('attendees-get-or-add', permanent=True)

def get_or_add_attendees(request):
    if request.method == 'POST':
        params = json.loads(request.body)

        new_attendee = Attendee.objects.create(
            first_name=params['first_name'],
            last_name=params['last_name']
        )

        return JsonResponse(new_attendee.to_dict(), status=201)

    if request.method == 'GET':
        attendees = [attendee.to_dict() for attendee in Attendee.objects.all()]
        return JsonResponse({'attendees': attendees}, status=200) 

    return HttpResponse('Method Not Allowed', status=405)


def get_attendee(request, attendee_id):
    attendee = Attendee.objects.get_or_404(id=attendee_id)
    return JsonResponse(attendee.to_dict(), status=200)


def update_or_delete_attendee(request, attendee_id):
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

    return HttpResponse('Method Not Allowed', status=405)


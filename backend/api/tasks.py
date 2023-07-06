import time

from celery.result import AsyncResult
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from celery import shared_task
from wallet.factories.utils import load_data


@shared_task
def load_data_task(count_users=10, count_operations=100):
    result = load_data(count_users=count_users, count_operations=count_operations)

    if result:
        return {
            "status": "success",
            "message": "Data loaded successfully",
            "count_users": count_users,
            "count_operations": count_operations,
        }

    return False


@shared_task
def test_data():
    result = []
    for i in range(10):
        result.append(i)
        time.sleep(1)

    return result


@shared_task
def create_task(task_type):
    time.sleep(int(task_type) * 10)
    return True


@csrf_exempt
def task_task(request):
    if request.POST:
        task_type = request.POST.get("type")
        task = create_task.delay(int(task_type))
        return JsonResponse({"task_id": task.id}, status=202)

    return JsonResponse({"error": "Method not allowed"}, status=405)


from celery.result import AsyncResult
from django.http import JsonResponse
from rest_framework import permissions, viewsets

from api.serializers import WalletSerializer, AccountSerializer, TransactionSerializer, OperationSerializer, AttachmentSerializer
from wallet.models import WalletModel, AccountModel, TransactionModel, OperationModel, AttachmentModel
from api.tasks import test_data, load_data_task


def load_data(request):
    result = load_data_task.delay(count_users=10, count_operations=100)
    if result:
        return JsonResponse({"task_id": result.id}, status=202)


def generate_test_data(request):
    result = test_data.delay()
    print(type(result))
    if result:
        return JsonResponse({"task_id": result.id}, status=202)

    return JsonResponse({"result": 'Всё пропало, шеф!'}, status=202)


def get_status(request, task_id):
    task_result = AsyncResult(task_id)
    print(task_result.__dict__)
    result = {
        "task_id": task_id,
        "task_status": task_result.status,
        "task_result": task_result.result
    }
    return JsonResponse(result, status=200)
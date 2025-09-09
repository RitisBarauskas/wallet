from api.tasks import create_task


def added_new_items_trigger(item_id):
    create_task.delay(item_id)

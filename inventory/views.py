from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Item
from .serializers import ItemSerializer
from django.core.cache import cache
import logging
import traceback

logger = logging.getLogger(__name__)

class ItemList(APIView):
    def get(self, request):
        try:
            items = Item.objects.all()
            serializer = ItemSerializer(items, many=True)
            return Response(serializer.data)
        except Exception as e:
            logger.error(f"Error retrieving item list: {e}\n{traceback.format_exc()}")
            return Response({"detail": "Error retrieving item list"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = ItemSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                logger.debug("Item created successfully")
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            logger.warning(f"Item creation failed: {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Error creating item: {e}\n{traceback.format_exc()}")
            return Response({"detail": "Error creating item"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ItemDetail(APIView):
    def get(self, request, item_id):
        try:
            item = get_object_or_404(Item, pk=item_id)
            serializer = ItemSerializer(item)
            return Response(serializer.data)
        except Exception as e:
            logger.error(f"Error retrieving item {item_id}: {e}\n{traceback.format_exc()}")
            return Response({"detail": "Error retrieving item"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, item_id):
        try:
            item = get_object_or_404(Item, pk=item_id)
            serializer = ItemSerializer(item, data=request.data)
            if serializer.is_valid():
                serializer.save()
                logger.info(f'Item {item_id} updated.')
                return Response(serializer.data)
            logger.warning(f"Item update failed: {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Error updating item {item_id}: {e}\n{traceback.format_exc()}")
            return Response({"detail": "Error updating item"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, item_id):
        try:
            item = get_object_or_404(Item, pk=item_id)
            item.delete()
            logger.info(f'Item {item_id} deleted.')
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            logger.error(f"Error deleting item {item_id}: {e}\n{traceback.format_exc()}")
            return Response({"detail": "Error deleting item"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
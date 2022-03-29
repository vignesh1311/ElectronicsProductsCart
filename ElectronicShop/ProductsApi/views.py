# from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from .models import ElectronicProducts


# Create your views here.


@method_decorator(csrf_exempt, name='dispatch')
class ElectProducts(View):

    def post(self, request):
        data = json.loads(request.body.decode("utf-8"))
        p_name = data.get('Name')
        p_description = data.get('Description')
        p_type = data.get('Type')
        if p_type == 'MO':
            p_processor = data.get('Processor')
            p_ram = data.get('RAM')
            p_screensize = data.get('Screensize')
            p_color = data.get('Color')
            product_data = {
                'Name': p_name,
                'Description': p_description,
                'Type': p_type,
                'Processor': p_processor,
                'RAM': p_ram,
                'Screensize': p_screensize,
                'Color': p_color,
            }

            cart_item = ElectronicProducts.objects.create(**product_data)

        elif p_type == 'LAP':
            p_processor = data.get('Processor')
            p_ram = data.get('RAM')
            p_hd = data.get('HDCapacity')
            product_data = {
                'Name': p_name,
                'Description': p_description,
                'Type': p_type,
                'Processor': p_processor,
                'RAM': p_ram,
                'HDCapacity': p_hd,
            }

            cart_item = ElectronicProducts.objects.create(**product_data)

        data = {
            "message": f"New item added to Cart with id: {ElectronicProducts.id}"}
        return JsonResponse(data, status=200)

    def get(self, request):
        items_count = ElectronicProducts.objects.count()
        items = ElectronicProducts.objects.all()

        items_data = []
        for item in items:
            if item.Type == 'MO':
                items_data.append({
                    'Name': item.Name,
                    'Description': item.Description,
                    'Type': item.Type,
                    'Processor': item.Processor,
                    'RAM': item.RAM,
                    'Screensize': item.Screensize,
                    'Color': item.Color,
                })
            elif item.Type == 'LAP':
                items_data.append({
                    'Name': item.Name,
                    'Description': item.Description,
                    'Type': item.Type,
                    'Processor': item.Processor,
                    'RAM': item.RAM,
                    'HDCapacity': item.HDCapacity,
                })

        data = {
            'items': items_data,
            'count': items_count,
        }
        return JsonResponse(data)


@method_decorator(csrf_exempt, name='dispatch')
class ElectProductsUpdate(View):

    def patch(self, request, item_id):
        data = json.loads(request.body.decode("utf-8"))
        item = ElectronicProducts.objects.get(id=item_id)
        item.Description = data['Description']
        item.save()

        data = {
            'message': f'Item {item_id} has been updated'
        }

        return JsonResponse(data)

    def delete(self, request, item_id):
        item = ElectronicProducts.objects.get(id=item_id)
        item.delete()

        data = {
            'message': f'Item {item_id} has been deleted'
        }

        return JsonResponse(data)

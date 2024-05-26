from django.shortcuts import render
from django.http import JsonResponse
from .models import data_prediction
import json

def welcome(request):
    return render(request, 'map/index.html') 
# Create your views here.

def select_crop(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        crop = data.get('crop')  # POST 요청으로부터 작물 정보 받기
        year = data.get('year')  # POST 요청으로부터 년도 정보 받기
        print(crop, year)

        try:
            region_production_data = data_prediction.objects.filter(crop=crop, year=year)
            # 데이터베이스에서 조회한 결과를 JSON 형식으로 응답
            data = [{'region': data.region, 'prediction': data.prediction} for data in region_production_data]
            print(data)
            return JsonResponse(data, safe=False)
        except data_prediction.DoesNotExist:
            # 해당 작물 및 연도에 대한 데이터가 없는 경우
            return JsonResponse({'error': 'Data not found for the given crop and year'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
    
def map_price(request):
    # URL에서 위도와 경도 파라미터 가져오기
    latitude = request.GET.get('lat')
    longitude = request.GET.get('lng')

    # 이미지 URL 생성
    image_url = f"http://api.vworld.kr/ned/wms/getIndvdLandPriceWMS?apiKey=E739356B-02E6-3D72-BF19-C82D8E68E834&domain=localhost&layers=dt_d150&crs=EPSG:4326&bbox={latitude},{longitude},{float(latitude) + 0.002},{float(longitude) + 0.004}&width=500&height=300&format=image/png&transparent=false&bgcolor=0xFFFFFF&exceptions=blank"
    
    # HTML 템플릿 렌더링
    return render(request, 'map/mapPrice.html', {'image_url': image_url})
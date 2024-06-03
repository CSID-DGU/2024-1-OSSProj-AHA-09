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
    # URL에서 지역, 작물, 연도 파라미터 가져오기
    region = request.GET.get('region')
    crop = request.GET.get('crop')
    year = request.GET.get('year')

    # URL 매개변수 로그로 출력
    print(f"Region: {region}, Crop: {crop}, Year: {year}")

    # 데이터베이스에서 생산량 값 조회
    try:
        production_data = data_prediction.objects.get(region=region, crop=crop, year=year)
        print("Production Data:", production_data)  # 데이터 확인을 위한 출력
        prediction = production_data.prediction
        region_name = production_data.region
    except data_prediction.DoesNotExist:
        prediction = "No data available"
        region_name = "Unknown"

    # 이미지 URL 생성
    latitude = request.GET.get('lat')
    longitude = request.GET.get('lng')
    image_url = f"http://api.vworld.kr/ned/wms/getIndvdLandPriceWMS?apiKey=E739356B-02E6-3D72-BF19-C82D8E68E834&domain=localhost&layers=dt_d150&crs=EPSG:4326&bbox={latitude},{longitude},{float(latitude) + 0.002},{float(longitude) + 0.004}&width=500&height=300&format=image/png&transparent=false&bgcolor=0xFFFFFF&exceptions=blank"

    # HTML 템플릿 렌더링
    return render(request, 'map/mapPrice.html', {
        'image_url': image_url,
        'region': region_name,
        'crop': crop,
        'year': year,
        'prediction': prediction
    })
def identify_location(request):
    if request.method == 'GET':
        # 클라이언트로부터 위도와 경도 값을 받음
        latitude = request.GET.get('latitude')
        longitude = request.GET.get('longitude')
        
        # 여기서 실제로 위도와 경도를 기반으로 어느 지역인지 식별하는 로직을 구현하고
        # 해당 지역을 JSON 형식으로 응답합니다.
        # 이 예시에서는 임시로 "Unknown" 지역을 응답합니다.
        region = "Unknown"
        
        # 식별된 지역 정보를 JSON 형식으로 응답
        return JsonResponse({'region': region})
    else:
        # 잘못된 요청 방식에 대한 오류 응답
        return JsonResponse({'error': 'Invalid request method'}, status=400)

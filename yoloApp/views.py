from django.shortcuts import render
from .functions import detectLicensePlateNumber
from .models import MultipleImage


def upload(request):
    if request.method == "POST":
        images = request.FILES.getlist('images')
        for image in images:
            MultipleImage.objects.create(car=image)
    images = MultipleImage.objects.all()
    plateNumbers = []
    for image in images:
        if image.plate_number == "":
            result = detectLicensePlateNumber(image.car.read())
            plateNumbers.append(result)
            image.plate_number = result
            image.save()
    return render(request, 'index.html', {'result':reversed(images)})

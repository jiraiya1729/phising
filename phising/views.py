from django.shortcuts import render
from .utils.extract import extract_features
from .utils.predict import predict
def hello_world(request):
    message = ''  # Initialize the message as an empty string
    feature_list =[]
    if request.method == 'POST':
        url = request.POST.get('url')
        if url:
            message = "URL received: " + url
            feature_list = extract_features(url)
            output = predict(feature_list)
            result = ''
            if output == 0:
                result = 'safe site'
            else:
                result = 'danger its not safe'
                
    return render(request, 'hello.html', {'message': message, 'result':result})

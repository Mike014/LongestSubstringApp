from django.shortcuts import render
from .algorithm import length_of_longest_substring
from .models import SubstringResult

def longest_substring_view(request):
    print("Received Request: ", request.method)
    result = None
    longest_length = None  
    
    if request.method == "POST":
        input_string = request.POST.get("input_string")
        print("Input String: ", input_string)  
        
        if input_string:
            longest_length = length_of_longest_substring(input_string)
            print("Longest Length: ", longest_length)  
            
            result = SubstringResult.objects.create(
                input_string=input_string,
                length_of_longest_substring=longest_length
            )
            print("Result Saved: ", result)  
            print("Context Passed:", {"result": result})
    
    return render(request, "substring/index.html", {"result": result, "longest_length": longest_length})



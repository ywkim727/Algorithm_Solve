def solution(brown, yellow):
    carpet = brown + yellow
    car_list = []
    for i in range(1, carpet+1) :
        if carpet % i == 0 :
            car_list.append(i)
    
    for i in range(len(car_list)) :
        width = car_list[i]
        height = carpet / width
        if (width-2) * (height-2) == yellow :
            if width > height :
                return [width, height]
            else :
                return [height, width]
        
    
    
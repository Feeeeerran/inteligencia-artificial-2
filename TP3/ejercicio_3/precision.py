def precision(arr,clases):
    suma = 0
    for i in range(len(arr)):
        if arr[i] == clases[i]:
            suma += 1
    precision = suma/len(arr) * 100
    print("La precision es del ",precision,"%")
    return precision
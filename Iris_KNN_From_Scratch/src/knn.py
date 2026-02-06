def euclidean_distance(point1 , point2):
    if len(point1) != len(point2):
        return None

    return np.sqrt(np.sum((point1 - point2)**2))

def KNN1(input_col , species ,point , k):
    lst = []

    for i in range(0,len(input_col)):
        distance = euclidean_distance(np.array(input_col[i]) , np.array(point) )
        lst.append((distance , species[i]))

    lst.sort(key=lambda x: x[0])
    k_nearest = [j for _ , j in lst[:k]]

    return Counter(k_nearest).most_common(1)[0][0]
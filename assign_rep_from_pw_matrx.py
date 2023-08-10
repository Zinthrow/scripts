
def cluster_representatives_from_pairwise_matrix(matrix: dict, diff = 6):

    cluster_reps = {}
    outgroup = {}

    for i in matrix:
        for j in matrix[i]:
            if i == j:
                continue
            v = matrix[i][j]
            if v <= diff:
                if i in cluster_reps:
                    cluster_reps[i][j] = None
                    if j in cluster_reps:
                        del cluster_reps[j]
                    outgroup[j] = None
                if j in cluster_reps:
                    cluster_reps[j][i] = None
                    outgroup[i] = None
                    if i in cluster_reps:
                        del cluster_reps[i] 
                if i not in cluster_reps and i not in outgroup:
                    cluster_reps[i] = {j:None}
                    outgroup[j] = None

        if i not in matrix and i not in outgroup:
            matrix[i] = {i: None}
            outgroup[i] = {i: None}


    cluster_reps[i] = {i: None}

    assigned = {}
    for i in cluster_reps:
        assigned[i] = i
        for j in cluster_reps[i]:
            assigned[j] = i


    print(len(cluster_reps), len(assigned), len(outgroup))
    
    return assigned


assigned = cluster_representatives_from_pairwise_matrix(matrix)

def motxilla_fb(nombre:int, capacitat:int, pes_cost:list[any]) -> tuple[int,list[int]]:
    """
    Tria la millor combinació d'objectes amb l'algoritme de la motxilla 

    Parametres:
    :param nombre: nombre d'items possibles
    :param capacitat: capacitat de la motxilla
    :param pes_cost:
        llista de tuples del tipus [(pes, cost), (pes, cost), ...]

    Retorn:
        Tupla on el primer element és el cost i el segon element és la
        combinació òptima d'objectes.
    
    Idea:
        definition of status: 
            f(i, j) = **Maximum value** for a backpack with capacity j, in i items
        update status: whether to add the pes_cost[i] to the backpack
            f(i, j) = 0                                                                  if i == 0 or j == 0
                    = f(i-1, j)                                                          if j < i.weight
                    = max(f(i-1, j), f(i, j - pes_cost[i].weight) + pes_cost[i].value)   if j >= i-th item.weight
    """
    if not pes_cost: raise ValueError("There are 0 elements in pes_cost!!")
    comb_past: list[set[int]] = [set() for i in range(capacitat + 1)]
    comb_curr: list[set[int]] = [set() for i in range(capacitat + 1)]
    past: list[int] = [0] * (capacitat + 1)
    curr: list[int] = [0] * (capacitat + 1)

    # the case of backpacks for the 0-th item is the same as list prev, so
    # the dp starts from backpacks for the 1st item: pes_cost[0]
    for i in range(nombre):
        weight: int = pes_cost[i][0]
        value: float = pes_cost[i][1]

        for j in range(capacitat + 1):  # 有必要在这里将 range 改成 1，capacity + 1 吗？
            if j < weight:
                curr[j] = past[j]
                comb_curr[j] = comb_past[j].copy()
            else:
                take_item: int = past[j - weight] + value
                leave_item: int = past[j]
                if take_item > leave_item:
                    curr[j] = take_item
                    comb_curr[j] = comb_past[j - weight].copy()
                    comb_curr[j].add(i)
                else:
                    curr[j] = leave_item
                    comb_curr[j] = comb_past[j].copy()
        curr, past = past, curr
        comb_curr, comb_past = comb_past, comb_curr

    return (past[-1], comb_past[-1])
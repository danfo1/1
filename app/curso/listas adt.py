def insertion_sort(L):
    if len(L)>1:
        market=L.first()
        while market !=L.last():
            pivot=L.after(market)
            value=pivot.element()
            if value >market.element():
                market=pivot
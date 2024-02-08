import scores


def tradePotatoForOrc():
    scores.orcs.score = scores.orcs.score - 1
    if scores.potatoForOrc.score > scores.potatoes.score:
        scores.potatoes.score = 0
        return
    scores.potatoes.score = scores.potatoes.score - scores.potatoForOrc.score
    

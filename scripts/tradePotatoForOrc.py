import scores


def tradePotatoForOrc():
    if scores.potatoForOrc.score > scores.potatoes.score:
        print("Sorry chap, not enough potatoes to bribe the orcs")
        return
    if scores.orcs.score <= 0:
        print("Orcs score is already at zero. Are you mad, why are you trying to give away potatos?")
        return
    scores.orcs.score = scores.orcs.score - 1
    scores.potatoes.score = scores.potatoes.score - scores.potatoForOrc.score

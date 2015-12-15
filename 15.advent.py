from inputs import FIFTEENTH
import operator
import functools

ing_attribs = FIFTEENTH.ingredients

class cookie_mix:
    ingredients = {}

    metrics = [
        'capacity',
        'durability',
        'flavor',
        'texture',
        'calories',
        ]

    def __init__(self,combo):
        self.ingredients['Sugar'] = combo[0]
        self.ingredients['Sprinkles'] = combo[1]
        self.ingredients['Candy'] = combo[2]
        self.ingredients['Chocolate'] = combo[3]

    def inc_dec(self, increase, decrease):
        self.ingredients[increase] += 1
        self.ingredients[decrease] -= 1
        return self

    def id(self):
        return ":".join([str(i) for i in self.ingredients.values()])

    def get_score(self):
        scores = {
            'capacity': 0,
            'durability': 0,
            'flavor': 0,
            'texture': 0,
            'calories': 0
        }
        for metric in self.metrics:
            for (ing,amount) in self.ingredients.items():
                scores[metric] += ing_attribs[ing][metric] * amount

        if True in [s <= 0 for s in scores.values()]:
            return 0
        if scores['calories'] != 500:
            return 0

        total_score = functools.reduce(operator.mul,[v for (k,v) in scores.items() if k != 'calories'],1)
        print scores, total_score

        return total_score


best_score = 0
for i in range(0,100):
    for j in range(0,100-i):
        for k in range(0,100-i-j):
            h = 100-i-j-k
            mix = cookie_mix([i,j,k,h])
            score = mix.get_score()
            if score > best_score:
                best_score = score
                print 'new best {}'.format(best_score)

print best_score


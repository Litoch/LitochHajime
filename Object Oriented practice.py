class Medal:
    def __init__(self, country, gold, silver, bronze):
        self.country = country
        self.gold = gold
        self.silver = silver
        self.bronze = bronze

    def new_ranking(self, ranking):
        if ranking == 1:
            self.gold += 1
        if ranking == 2:
            self.silver += 1
        if ranking == 3:
            self.bronze += 1

    def total_medal(self):
        return self.gold + self.silver + self.bronze

    def __str__(self):
        return  '%s: Gold %d    Silver %d   ' \
                'Bronze %d   Total %d' % (self.country, self.gold,
                                          self.silver, self.bronze, self.total_medal())


china = Medal("China", 47, 18, 26)
us = Medal("the USA", 36, 37, 38)
uk = Medal("the UK", 27, 23, 17)

print(china)
print(us)
print(uk)
print()

china.new_ranking(1)
us.new_ranking(2)
uk.new_ranking(3)

print(china)
print(us)
print(uk)
print()

medal_list = [china, us, uk]

print('Ranking by Gold Medal:')
ranking_by_gold = sorted(medal_list, key=lambda x: x.gold, reverse=True)
for i in ranking_by_gold:
    print(i)

print()
print('Ranking by Total Medal:')
ranking_by_total_medal = sorted(medal_list, key=lambda x: x.total_medal(), reverse=True)
for i in ranking_by_total_medal:
    print(i)

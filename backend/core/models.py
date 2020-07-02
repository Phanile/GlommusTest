from django.db import models


class Player(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=50, default='username')
    money = models.IntegerField(default=0)
    gems = models.IntegerField(default=0)
    level = models.IntegerField(default=1)
    damage = models.IntegerField(default=50)
    fiends = models.ManyToManyField('Player', blank=True)

    def take_all_gifts(self):
        my_gifts = Gift.objects.get(player = self)
        all_money = (sum([gift.money for gift in my_gifts]))
        self.money += all_money
        self.save()

    def __str__(self):
        return self.name


class Gift(models.Model):
    objects = models.Manager()
    money = models.IntegerField(default=0)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)

    def __str__(self):
        return 'Подарок'

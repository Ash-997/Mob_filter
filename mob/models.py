from django.db import models


class Brand(models.Model):
    brand = models.CharField(max_length=20)

    def __str__(self):
        return self.brand


class Ram(models.Model):
    ram = models.CharField(max_length=5)

    def __str__(self):
        return self.ram


class Memory(models.Model):
    memory = models.CharField(max_length=20)

    def __str__(self):
        return self.memory

class Pricecat(models.Model):
    pricecat = models.CharField(max_length=30)

    def __str__(self):
        return self.pricecat


class Mobiles(models.Model):
    phonemod = models.CharField(max_length=20)
    brnd = models.ForeignKey(Brand, on_delete=models.DO_NOTHING, related_name='brands')
    ram = models.ForeignKey(Ram, on_delete=models.DO_NOTHING, related_name='Ram', null=True)
    memory = models.ForeignKey(Memory, on_delete=models.DO_NOTHING, related_name='Memory', null=True)
    price = models.IntegerField(null=True)
    pricecat = models.ForeignKey(Pricecat, on_delete=models.DO_NOTHING, related_name='pcat', null=True)
    image = models.ImageField(upload_to='images',null=True)


    def __str__(self):
        return self.phonemod

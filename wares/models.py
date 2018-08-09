from django.db import models


class Cat(models.Model):
    cat_name = models.CharField(max_length=50, verbose_name="Категория")
    def __str__(self):
        return self.cat_name


class Vendor(models.Model):
    vendor_name = models.CharField(max_length=50, verbose_name="Категория")
    def __str__(self):
        return self.vendor_name



class Ware(models.Model):
    ware_name = models.CharField(max_length=200, verbose_name="Наименование")
    ware_code = models.CharField(max_length=20, verbose_name="Код")
    ware_vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, blank=True, null=True)
    ware_description = models.TextField(verbose_name="Описание")
    ware_cat = models.ForeignKey(Cat, on_delete=models.SET_NULL, blank=True, null=True)
    def __str__(self):
        return self.ware_name


class Seller(models.Model):
    seller_name = models.CharField(max_length=200, verbose_name="Наименование")
    seller_ogrn = models.CharField(max_length=15, verbose_name="ОГРН(ИП)")
    def __str__(self):
        return self.seller_name


class Price(models.Model):
    ware = models.ForeignKey(Ware, on_delete=models.CASCADE)
    price_value = models.DecimalField(verbose_name="Цена(руб.)", default=0, max_digits=19, decimal_places=2)
    price_tax = models.SmallIntegerField(verbose_name="Налог,%")
    pub_date = models.DateTimeField(verbose_name="Дата")
    seller = models.ForeignKey(Seller, on_delete=models.SET_NULL, blank=True, null=True)


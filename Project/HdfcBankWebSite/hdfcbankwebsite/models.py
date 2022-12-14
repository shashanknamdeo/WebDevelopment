from django.db import models


class transactions(models.Model):
    transaction_id  =models.IntegerField(primary_key=True)
    date            =models.CharField(max_length=20)
    narration       =models.CharField(max_length=255)
    cheque_no       =models.CharField(max_length=20)
    value_date      =models.CharField(max_length=20)
    withdrawal      =models.CharField(max_length=20)
    deposit         =models.CharField(max_length=20)
    closing_balance =models.CharField(max_length=20)
    class Meta:
        db_table='transactions'

from django.db import models

# Create your models here.
class Data_Pasien(models.Model):
    nama=models.CharField(max_length=255,blank=False)
    tanggal_masuk=models.DateField()
    tanggal_lahir=models.DateField(     )
    jenis_kelamin=models.CharField()
    alamat=models.TextField()
    no_telp=models.CharField()
class Meta:
    db_table:'pasien'

from django.db import models


class AnnouncedPollingUnitResult(models.Model):
    result_id = models.IntegerField()
    polling_unit_unique_id = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField(auto_now_add=True)
    user_ip_address = models.CharField(max_length=50)


class AnnouncedLgaResult(models.Model):
    result_id = models.IntegerField()
    lga_name = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=50, blank=True, null=True)
    date_entered = models.DateTimeField(auto_now_add=True)
    user_ip_address = models.CharField(max_length=50)


class LGA(models.Model):
    unique_id = models.IntegerField()
    lga_id = models.IntegerField()
    lga_name = models.CharField(max_length=50)
    state_id = models.IntegerField()
    lga_description = models.TextField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField(max_length=50)


class PollingUnit(models.Model):
    unique_id = models.IntegerField()
    polling_unit_id = models.IntegerField()
    ward_id = models.IntegerField()
    lga_id = models.IntegerField()
    unique_ward_id = models.IntegerField(blank=True, null=True)
    polling_unit_number = models.CharField(max_length=50, blank=True, null=True)
    polling_unit_name = models.CharField(max_length=50, blank=True, null=True)
    polling_unit_description = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=255, blank=True, null=True)
    long = models.CharField(max_length=255, blank=True, null=True)
    entered_by_user = models.CharField(max_length=50, blank=True, null=True)
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField(max_length=50, blank=True, null=True)


class Party(models.Model):
    party_id = models.CharField(max_length=11)
    party_name = models.CharField(max_length=11)

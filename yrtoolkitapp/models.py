# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import cgi

# Create your models here.
class Project(models.Model):
    ai_gallery_id = models.CharField(max_length=255, null=True, blank=True)
    tutorial_id = models.IntegerField(default=0, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    add_date = models.DateTimeField(null=True, blank=True, db_index=True)
    def getJSONObject(self):
        jsonObject = {'id':cgi.escape(self.ai_gallery_id),'name':cgi.escape(self.name),'username':cgi.escape(self.username)}
        return jsonObject

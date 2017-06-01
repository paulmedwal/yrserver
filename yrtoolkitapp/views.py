# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone

from yrtoolkitapp.models import Project

import json

# Create your views here.
def submitProject(request,tutorialId, projectId):
  appName = request.POST["appName"]
  username = request.POST["username"]
  #we know projectId is a number from url selection
  returnObject = {}
  try:
    project = Project.objects.get(ai_gallery_id = projectId,tutorial_id = tutorialId)
    #project already exists
    returnObject['type'] = "Error"
    returnObject['msg'] = "Project already exists"
  except Project.DoesNotExist:
    project = Project(ai_gallery_id = projectId, tutorial_id = tutorialId, name = appName, username = username,add_date = timezone.now())
    project.save()
    returnObject['type'] = "Success"
    returnObject['msg'] = "Project was submitted"

  return HttpResponse(json.dumps(returnObject))

def getTutorialProjects(request,tutorialId):
  projects = Project.objects.filter(tutorial_id = tutorialId).order_by('-add_date')
  aiProjectIdList = list(map(lambda project: project.getJSONObject(), projects))
  
  return HttpResponse(json.dumps(aiProjectIdList))

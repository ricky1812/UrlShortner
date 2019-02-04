#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 14:00:49 2019

@author: rounak
"""

from django import forms
class Submit(forms.Form):
    website=forms.CharField(label='Submit URL')
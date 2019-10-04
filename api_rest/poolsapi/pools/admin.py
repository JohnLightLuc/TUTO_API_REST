from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class PollAdmin(admin.ModelAdmin):

    list_display = ('id', 'question', 'create_by', 'pub_date')
    list_filter = (
        'crea
class ChoiceAdmin(admin.ModelAdmin):

    list_display = ('id', 'pool', 'Choice_text')
    list_filter = ('pool', 'id', 'pool', 'Choice_text')


class VoteAdmin(admin.ModelAdmin):

    list_display = ('id', 'choice', 'poll', 'voted_by')
    list_filter = (
        'choice',
        'poll',
        'voted_by',
        'id',
        'choice',
        'poll',
        'voted_by',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Poll, PollAdmin)
_register(models.Choice, ChoiceAdmin)
_register(models.Vote, VoteAdmin)

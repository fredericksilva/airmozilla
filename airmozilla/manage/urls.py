from django.conf.urls.defaults import patterns, url

from . import views


urlpatterns = patterns(
    '',
    url(r'^/?$', views.dashboard, name='home'),
    url(r'^users/(?P<id>\d+)/$', views.user_edit, name='user_edit'),
    url(r'^users/', views.users, name='users'),
    url(r'^groups/(?P<id>\d+)/$', views.group_edit, name='group_edit'),
    url(r'^groups/remove/(?P<id>\d+)/$', views.group_remove,
        name='group_remove'),
    url(r'^groups/new/$', views.group_new, name='group_new'),
    url(r'^groups/$', views.groups, name='groups'),
    url(r'^events/request/$', views.event_request, name='event_request'),
    url(r'^events/(?P<id>\d+)/$', views.event_edit, name='event_edit'),
    url(r'^events/(?P<id>\d+)/vidly-submissions/$',
        views.event_vidly_submissions,
        name='event_vidly_submissions'),
    url(r'^events/(?P<id>\d+)/vidly-submissions/submission'
        r'/(?P<submission_id>\d+)/$',
        views.event_vidly_submission,
        name='event_vidly_submission'),
    url(r'^events/(?P<id>\d+)/tweets/$', views.event_tweets,
        name='event_tweets'),
    url(r'^events/(?P<id>\d+)/tweets/new/$', views.new_event_tweet,
        name='new_event_tweet'),
    url(r'^events/all/tweets/$', views.all_event_tweets,
        name='all_event_tweets'),
    url(r'^events/archive/(?P<id>\d+)/$', views.event_archive,
        name='event_archive'),
    url(r'^events/duplicate/(?P<duplicate_id>\d+)/$', views.event_request,
        name='event_duplicate'),
    url(r'^events/vidlyurltoshortcode/(?P<id>\d+)/',
        views.vidly_url_to_shortcode,
        name='vidly_url_to_shortcode'),
    url(r'^events/$', views.events, name='events'),
    url(r'^tag-autocomplete/$', views.tag_autocomplete,
        name='tag_autocomplete'),
    url(r'^events-autocomplete/$', views.event_autocomplete,
        name='event_autocomplete'),
    url(r'^participant-autocomplete/$', views.participant_autocomplete,
        name='participant_autocomplete'),
    url(r'^participants/new/$', views.participant_new, name='participant_new'),
    url(r'^participants/(?P<id>\d+)/$', views.participant_edit,
        name='participant_edit'),
    url(r'^participants/remove/(?P<id>\d+)/$', views.participant_remove,
        name='participant_remove'),
    url(r'^participants/email/(?P<id>\d+)/$', views.participant_email,
        name='participant_email'),
    url(r'^participants/$', views.participants, name='participants'),
    url(r'^categories/new/$', views.category_new, name='category_new'),
    url(r'^categories/(?P<id>\d+)/$', views.category_edit,
        name='category_edit'),
    url(r'^categories/remove/(?P<id>\d+)/$', views.category_remove,
        name='category_remove'),
    url(r'^categories/$', views.categories, name='categories'),
    url(r'^channels/new/$', views.channel_new, name='channel_new'),
    url(r'^channels/(?P<id>\d+)/$', views.channel_edit,
        name='channel_edit'),
    url(r'^channels/remove/(?P<id>\d+)/$', views.channel_remove,
        name='channel_remove'),
    url(r'^channels/$', views.channels, name='channels'),
    url(r'^templates/env-autofill/$', views.template_env_autofill,
        name='template_env_autofill'),
    url(r'^templates/new/$', views.template_new, name='template_new'),
    url(r'^templates/(?P<id>\d+)/$', views.template_edit,
        name='template_edit'),
    url(r'^templates/remove/(?P<id>\d+)/$', views.template_remove,
        name='template_remove'),
    url(r'^templates/$', views.templates, name='templates'),
    url(r'^tags/$', views.tags, name='tags'),
    url(r'^tags/(?P<id>\d+)/$', views.tag_edit, name='tag_edit'),
    url(r'^tags/remove/(?P<id>\d+)/$', views.tag_remove, name='tag_remove'),
    url(r'^locations/new/$', views.location_new, name='location_new'),
    url(r'^locations/(?P<id>\d+)/$', views.location_edit,
        name='location_edit'),
    url(r'^locations/remove/(?P<id>\d+)/$', views.location_remove,
        name='location_remove'),
    url(r'^locations/tz/$', views.location_timezone, name='location_timezone'),
    url(r'^locations/$', views.locations, name='locations'),
    url(r'^approvals/$', views.approvals, name='approvals'),
    url(r'^approvals/(?P<id>\d+)/$', views.approval_review,
        name='approval_review'),
    url(r'^pages/$', views.flatpages, name='flatpages'),
    url(r'^pages/new/$', views.flatpage_new, name='flatpage_new'),
    url(r'^pages/(?P<id>\d+)/$', views.flatpage_edit, name='flatpage_edit'),
    url(r'^pages/remove/(?P<id>\d+)/$', views.flatpage_remove,
        name='flatpage_remove'),
    url(r'^suggestions/$', views.suggestions, name='suggestions'),
    url(r'^suggestions/(?P<id>\d+)/$', views.suggestion_review,
        name='suggestion_review'),
    url(r'^vidly/$', views.vidly_media,
        name='vidly_media'),
    url(r'^vidly/status/$', views.vidly_media_status,
        name='vidly_media_status'),
    url(r'^vidly/info/$', views.vidly_media_info,
        name='vidly_media_info'),
    url(r'^vidly/resubmit/$', views.vidly_media_resubmit,
        name='vidly_media_resubmit'),
    url(r'^urltransforms/$', views.url_transforms,
        name='url_transforms'),
    url(r'^urltransforms/new/$', views.url_match_new,
        name='url_match_new'),
    url(r'^urltransforms/run/$', views.url_match_run,
        name='url_match_run'),
    url(r'^urltransforms/(?P<id>\d+)/remove/$', views.url_match_remove,
        name='url_match_remove'),
    url(r'^urltransforms/(?P<id>\d+)/add/$', views.url_transform_add,
        name='url_transform_add'),
    url(r'^urltransforms/(?P<id>\d+)/(?P<transform_id>\d+)/remove/$',
        views.url_transform_remove,
        name='url_transform_remove'),
    url(r'^urltransforms/(?P<id>\d+)/(?P<transform_id>\d+)/edit/$',
        views.url_transform_edit,
        name='url_transform_edit'),
)

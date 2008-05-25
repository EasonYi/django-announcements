from django.dispatch import dispatcher
from django.db.models import get_models, signals

try:
    from notification import models as notification
    
    def create_notice_types(app, created_models, verbosity, **kwargs):
        notification.create_notice_type("announcement", "Announcement", "you have received an announcement")
    
    dispatcher.connect(create_notice_types, signal=signals.post_syncdb, sender=notification)
except ImportError:
    print "Skipping creation of NoticeTypes as notification app not found"

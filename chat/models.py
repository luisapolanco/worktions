import uuid
from django.db import models
from Modules.Services.models import User
from django.db.models import Count

class ModelBase(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, db_index=True, editable=False)
    time = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class ChannelMessage(ModelBase):
    channel = models.ForeignKey("Channel", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()

class UserChannel(ModelBase):
    channel = models.ForeignKey("Channel", null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class ChannelQuerySet(models.QuerySet):

    def just_one(self):
        return self.annotate(num_users = Count("users")).filter(num_users=1)
    def just_two(self):
        return self.annotate(num_users = Count("users")).filter(num_users=2)
    
    def filter_by_username(self, username):
        return self.filter(userchannel__user__username=username)

class ChannelManager(models.Manager):   

    def get_queryset(self, *args, **kwargs):
        return ChannelQuerySet(self.model, using=self._db)

    def filter_ms_per_private(self, username_a, username_b):
        return self.get_queryset().just_two().filter_by_username(username_a).filter_by_username(username_b)
    
    def get_or_create_current_user_channel(self, user):
        qs = self.get_queryset().just_one().filter_by_username(user.username)
        if qs.exists():
            return qs.order_by("time").first(), False
        channel_obj = Channel.objects.create()
        UserChannel.objects.create(user= user, channel=channel_obj)
        return channel_obj, True
    
    def get_or_create_channel_ms(self, username_a, username_b):
        qs = self.filter_ms_per_private(username_a, username_b)
        if qs.exists():
            return qs.order_by("time").first(), False
        try:
            user_a =User.objects.get(username=username_a)
        except User.DoesNotExist:
            return None, False
        
        try:
            user_b =User.objects.get(username=username_b)
        except User.DoesNotExist:
            return None, False
        
        if user_a == None or user_b == None:
            return None, False
        
        channel_obj = Channel.objects.create()
        user_channel_a = UserChannel(user=User.objects.get(username=username_a), channel= channel_obj)
        user_channel_b = UserChannel(user= User.objects.get(username= username_b), channel= channel_obj)
        UserChannel.objects.bulk_create([user_channel_a, user_channel_b])
        return channel_obj, True


class Channel(ModelBase):
    users = models.ManyToManyField(User, blank=True, through=UserChannel)
    objects = ChannelManager()


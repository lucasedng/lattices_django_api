from django.db.models import Model, UUIDField, CharField
from django.db.models import IntegerField, FloatField, DateField
from django.contrib.postgres.fields import ArrayField
from uuid import uuid4


class Lattices(Model):

    id_lattice = UUIDField(primary_key = True, default = uuid4, editable = False)
    name = CharField(max_length = 50, unique = True)
    dimension = IntegerField()
    determinant = FloatField()
    minimal_norm = FloatField()
    kissing_number = IntegerField()
    gram_matrix = ArrayField(
        ArrayField(
            FloatField(),
            size = 40
        ),
        size = 40
    )
    create_at = DateField(auto_now_add = True)
    

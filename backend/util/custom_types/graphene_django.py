from graphene.types.inputobjecttype import InputObjectType, InputObjectTypeOptions
from graphene.types.field import Field
from graphene.types.utils import yank_fields_from_attrs

from graphene_django.registry import get_global_registry
from graphene_django.types import construct_fields


class DjangoInputObjectTypeOptions(InputObjectTypeOptions):
    model = None
    registry = None


class DjangoInputObjectType(InputObjectType):
    @classmethod
    def __init_subclass_with_meta__(
        cls, model=None, registry=None, fields=None, exclude=None, _meta=None, **options
    ):
        if not registry:
            registry = get_global_registry()

        convert_choices_to_enum = True
        django_fields = yank_fields_from_attrs(
            construct_fields(model, registry, fields, exclude, convert_choices_to_enum),
            _as=Field,
        )

        if not _meta:
            _meta = DjangoInputObjectTypeOptions(cls)

        _meta.model = model
        _meta.registry = registry
        _meta.fields = django_fields

        super(DjangoInputObjectType, cls).__init_subclass_with_meta__(_meta=_meta, **options)

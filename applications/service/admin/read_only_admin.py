from itertools import chain


class ReadOnlyAdminMixin(object):
    change_form_template = "../templates/admin/view.html"

    def get_readonly_fields(self, request, obj=None):
        return list(field.name for field in self.model._meta.get_fields() if not (field.one_to_many and field.related_model is not None))

    def get_actions(self, request):
        actions = super(ReadOnlyAdminMixin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions["delete_selected"]
        return actions

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def save_model(self, request, obj, form, change):
        pass

    def delete_model(self, request, obj):
        pass

    def save_related(self, request, form, formsets, change):
        pass

from sqladmin import Admin, ModelView
from .sqladmin_models import UsersAuth, Users2FA, UsersClass, UsersPondsAddress, UsersPrimaryAddress, UsersHarvestPlan, OverviewCommunityCache

def create_admin(app, engine):
    admin = Admin(app, engine)

    class UsersAuthAdmin(ModelView, model=UsersAuth):
        name = "Users ID"
        name_plural = "Users ID"
        icon = "fa fa-address-book"
        column_searchable_list = ['user_fullname', 'user_email']
        column_sortable_list = ['user_id', 'user_fullname', 'user_birthdate', 'user_phonenumber', 'user_email']
        column_list = ['user_id', 'user_fullname', 'user_birthdate', 'user_phonenumber', 'user_email']

    class Users2FAAdmin(ModelView, model=Users2FA):
        name = "Users 2FA"
        name_plural = "Users 2FAs"
        icon = "fa fa-key"
        column_sortable_list = ['user_id', 'ota_codes']
        column_list = ['user_id', 'ota_codes']

    class UsersClassAdmin(ModelView, model=UsersClass):
        name = "Users Class"
        name_plural = "Users Classes"
        icon = "fa fa-trophy"
        column_sortable_list = ['user_id', 'user_age', 'user_proficiency_level', 'user_pond_total', 'user_fish_type']
        column_list = ['user_id', 'user_age', 'user_proficiency_level', 'user_pond_total', 'user_fish_type']

    class UsersPondsAddressAdmin(ModelView, model=UsersPondsAddress):
        name = "Ponds Address"
        name_plural = "Ponds Addresses"
        icon = "fa fa-address-card"
        column_sortable_list = ['pond_address_id', 'user_id', 'user_address_full', 'user_address_province', 'user_address_city']
        column_list = ['pond_address_id', 'user_id', 'user_address_full', 'user_address_province', 'user_address_city']

    class UsersPrimaryAddressAdmin(ModelView, model=UsersPrimaryAddress):
        name = "Primary Address"
        name_plural = "Primary Addresses"
        icon = "fa fa-id-card"
        column_sortable_list = ['user_id', 'pond_address_id']
        column_list = ['user_id', 'pond_address_id']

    class UsersHarvestPlanAdmin(ModelView, model=UsersHarvestPlan):
        name = "Harvest Plan"
        name_plural = "Harvest Plans"
        icon = "fa fa-calendar"
        column_sortable_list = ['harvest_plan_id', 'user_id', 'user_province', 'user_city', 'harvest_plan_start']
        column_list = ['harvest_plan_id', 'user_id', 'user_province', 'user_city', 'harvest_plan_start']

    class OverviewCommunityCacheAdmin(ModelView, model=OverviewCommunityCache):
        name = "Community"
        name_plural = "Communities"
        icon = "fa fa-globe"
        column_sortable_list = ['community_id', 'community_province', 'community_city', 'community_month', 'community_fish_type']
        column_list = ['community_id', 'community_province', 'community_city', 'community_month', 'community_fish_type']

    admin.add_view(UsersAuthAdmin)
    admin.add_view(Users2FAAdmin)
    admin.add_view(UsersClassAdmin)
    admin.add_view(UsersPondsAddressAdmin)
    admin.add_view(UsersPrimaryAddressAdmin)
    admin.add_view(UsersHarvestPlanAdmin)
    admin.add_view(OverviewCommunityCacheAdmin)
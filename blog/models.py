from django.conf import settings
from django.db import models
from django.utils import timezone
from users.views import UserCreationForm
from django.contrib.auth.models import User
from datetime import datetime, date


class character(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField("Дата изменения, mm/dd/gg", auto_now_add=False, auto_now=True, blank=True)
    date_create = models.DateTimeField(auto_now_add=True,  auto_now=False, blank=True)
    # description - описание
    character_name = models.CharField(blank=True, null = True, max_length=255)
    worldview = models.CharField(blank=True, null = True,  max_length=255)
    nameperson = models.CharField(blank=True, null = True, max_length=255)
    lvlcharacter = models.IntegerField(blank=True, null = True)
    thedeity = models.CharField(blank=True, null = True,   max_length=255)
    homeland = models.CharField(blank=True, null = True, max_length=255)
    race = models.CharField(blank=True, null = True, max_length=255)
    size = models.IntegerField(blank=True, null = True)
    floor = models.CharField(blank=True, null = True, max_length=255)
    age = models.IntegerField(blank=True, null = True)
    height = models.IntegerField(blank=True, null = True)
    hair = models.CharField(blank=True, null = True, max_length=255)
    weight = models.IntegerField(blank=True, null = True)
    eye = models.CharField(blank=True, null = True, max_length=255)
    # abilities - характеристики
    srtength_ability_score = models.IntegerField(blank=True, null = True)
    srtength_ability_modifier = models.IntegerField(blank=True, null = True)
    srtength_temp_adjustment = models.IntegerField(blank=True, null = True)
    srtength_temp_modifier = models.IntegerField(blank=True, null = True)
    dexterity_ability_score = models.IntegerField(blank=True, null = True)
    dexterity_ability_modifier = models.IntegerField(blank=True, null = True)
    dexterity_temp_adjustment = models.IntegerField(blank=True, null = True)
    dexterity_temp_modifier = models.IntegerField(blank=True, null = True)
    constitution_ability_score = models.IntegerField(blank=True, null = True)
    constitution_ability_modifier = models.IntegerField(blank=True, null = True)
    constitution_temp_adjustment = models.IntegerField(blank=True, null = True)
    constitution_temp_modifier = models.IntegerField(blank=True, null = True)
    intelligence_ability_score = models.IntegerField(blank=True, null = True)
    intelligence_ability_modifier = models.IntegerField(blank=True, null = True)
    intelligence_temp_adjustment = models.IntegerField(blank=True, null = True)
    intelligence_temp_modifier = models.IntegerField(blank=True, null = True)
    wisdom_ability_score = models.IntegerField(blank=True, null = True)
    wisdom_ability_modifier = models.IntegerField(blank=True, null = True)
    wisdom_temp_adjustment = models.IntegerField(blank=True, null = True)
    wisdom_temp_modifier = models.IntegerField(blank=True, null = True)
    charisma_ability_score = models.IntegerField(blank=True, null = True)
    charisma_ability_modifier = models.IntegerField(blank=True, null = True)
    charisma_temp_adjustment = models.IntegerField(blank=True, null = True)
    charisma_temp_modifier = models.IntegerField(blank=True, null = True)
    # armor-класс брони
    armor_class_total = models.IntegerField(blank=True, null = True, max_length=255)
    armor_class_bonus_armor = models.IntegerField(blank=True, null = True, max_length=255)
    armor_class_shield_bonus = models.IntegerField(blank=True, null = True, max_length=255)
    armor_class_dex_modifier = models.IntegerField(blank=True, null = True, max_length=255)
    armor_class_size_modifier = models.IntegerField(blank=True, null = True, max_length=255)
    armor_class_natural_armor = models.IntegerField(blank=True, null = True, max_length=255)
    armor_class_deflection_modifier = models.IntegerField(blank=True, null = True, max_length=255)
    armor_class_misc_modifier = models.IntegerField(blank=True, null = True, max_length=255)
    touch_armor_class = models.CharField(blank=True, null = True, max_length=255)
    flat_footed_armor_class = models.CharField(blank=True, null = True, max_length=255)
    armor_class_modifier = models.CharField(blank=True, null = True, max_length=255)
    # HP - здоровье
    hit_points_total = models.IntegerField(blank=True, null = True)
    hit_points_damage_reduction = models.IntegerField(blank=True, null = True)
    hit_points_wounds_current_HP = models.CharField(blank=True, null = True, max_length=255)
    hit_points_nonlethal_damage = models.IntegerField(blank=True, null = True)
    # инициативы
    initiative_modifier_total = models.CharField(blank=True, null = True, max_length=255)
    initiative_modifier_dex_modifier = models.CharField(blank=True, null = True, max_length=255)
    initiative_modifier_misc_modifier = models.CharField(blank=True, null = True, max_length=255)
    # наземная скорость
    speed_land_base_speed_FT_SQ = models.CharField(blank=True, null = True, max_length=255)
    speed_land_with_armor_FT_SQ = models.CharField(blank=True, null = True, max_length=255)
    speed_land_fly_FT = models.CharField(blank=True, null = True, max_length=255)
    speed_land_maneuverability_FT = models.CharField(blank=True, null = True, max_length=255)
    speed_land_swim_FT = models.CharField(blank=True, null = True, max_length=255)
    speed_land_climb_FT = models.CharField(blank=True, null = True, max_length=255)
    speed_land_burrow_FT = models.CharField(blank=True, null = True, max_length=255)
    speed_land_temp_modifiers = models.CharField(blank=True, null = True, max_length=255)
    # испытания
    fortitude_total = models.CharField(blank=True, null = True, max_length=255)  # стойкость
    fortitude_base_save = models.CharField(blank=True, null = True, max_length=255)  # стойкость
    fortitude_ability_modifier = models.CharField(blank=True, null = True, max_length=255)  # стойкость
    fortitude_magic_modifier = models.CharField(blank=True, null = True, max_length=255)  # стойкость
    fortitude_misc_modifier = models.CharField(blank=True, null = True, max_length=255)  # стойкость
    fortitude_temporary_modifier = models.CharField(blank=True, null = True, max_length=255)  # стойкость
    reflex_total = models.CharField(blank=True, null = True, max_length=255)  # реакция
    reflex_base_save = models.CharField(blank=True, null = True, max_length=255)  # реакция
    reflex_ability_modifier = models.CharField(blank=True, null = True, max_length=255)  # реакция
    reflex_magic_modifier = models.CharField(blank=True, null = True, max_length=255)  # реакция
    reflex_misc_modifier = models.CharField(blank=True, null = True, max_length=255)  # реакция
    reflex_temporary_modifier = models.CharField(blank=True, null = True, max_length=255)  # реакция
    will_total = models.CharField(blank=True, null = True, max_length=255)  # воля
    will_base_save = models.CharField(blank=True, null = True, max_length=255)  # воля
    will_ability_modifier = models.CharField(blank=True, null = True, max_length=255)  # воля
    will_magic_modifier = models.CharField(blank=True, null = True, max_length=255)  # воля
    will_misc_modifier = models.CharField(blank=True, null = True, max_length=255)  # воля
    will_temporary_modifier = models.CharField(blank=True, null = True, max_length=255)  # воля
    saving_throws_modifier = models.CharField(blank=True, null = True, max_length=255)  # общая модель для всех испытаний
    # other
    base_attack_bonus = models.CharField(blank=True, null = True, max_length=255)
    spell_resistance = models.CharField(blank=True, null = True, max_length=255)
    # cmb
    cmb_total = models.CharField(blank=True, null = True, max_length=255)
    cmb_base_attack_bonus = models.CharField(blank=True, null = True, max_length=255)
    cmb_strength_modifier = models.CharField(blank=True, null = True, max_length=255)
    cmb_size_modifier = models.CharField(blank=True, null = True, max_length=255)
    cmb_modifier = models.CharField(blank=True, null = True, max_length=255)
    # cmd
    cmd_total = models.CharField(blank=True, null = True, max_length=255)
    cmd_base_attack_bonus = models.CharField(blank=True, null = True, max_length=255)
    cmd_dexterity_modifier = models.CharField(blank=True, null = True, max_length=255)
    cmd_size_modifier = models.CharField(blank=True, null = True, max_length=255)
    cmd_strength_modifier = models.CharField(blank=True, null = True, max_length=255)
    # weapon_one
    weapon_one_name = models.CharField(blank=True, null = True, max_length=255)
    weapon_one_attack_bonus = models.CharField(blank=True, null = True, max_length=255)
    weapon_one_critical = models.CharField(blank=True, null = True, max_length=255)
    weapon_one_type = models.CharField(blank=True, null = True, max_length=255)
    weapon_one_range = models.CharField(blank=True, null = True, max_length=255)
    weapon_one_ammunition = models.CharField(blank=True, null = True, max_length=255)
    weapon_one_damage = models.CharField(blank=True, null = True, max_length=255)
    # weapon_two
    weapon_two_name = models.CharField(blank=True, null = True, max_length=255)
    weapon_two_attack_bonus = models.CharField(blank=True, null = True, max_length=255)
    weapon_two_critical = models.CharField(blank=True, null = True, max_length=255)
    weapon_two_type = models.CharField(blank=True, null = True, max_length=255)
    weapon_two_range = models.CharField(blank=True, null = True, max_length=255)
    weapon_two_ammunition = models.CharField(blank=True, null = True, max_length=255)
    weapon_two_damage = models.CharField(blank=True, null = True, max_length=255)
    # weapon_three
    weapon_three_name = models.CharField(blank=True, null = True, max_length=255)
    weapon_three_attack_bonus = models.CharField(blank=True, null = True, max_length=255)
    weapon_three_critical = models.CharField(blank=True, null = True, max_length=255)
    weapon_three_type = models.CharField(blank=True, null = True, max_length=255)
    weapon_three_range = models.CharField(blank=True, null = True, max_length=255)
    weapon_three_ammunition = models.CharField(blank=True, null = True, max_length=255)
    weapon_three_damage = models.CharField(blank=True, null = True, max_length=255)
    # weapon_four
    weapon_four_name = models.CharField(blank=True, null = True, max_length=255)
    weapon_four_attack_bonus = models.CharField(blank=True, null = True, max_length=255)
    weapon_four_critical = models.CharField(blank=True, null = True, max_length=255)
    weapon_four_type = models.CharField(blank=True, null = True, max_length=255)
    weapon_four_range = models.CharField(blank=True, null = True, max_length=255)
    weapon_four_ammunition = models.CharField(blank=True, null = True, max_length=255)
    weapon_four_damage = models.CharField(blank=True, null = True, max_length=255)
    # weapon_five
    weapon_five_name = models.CharField(blank=True, null = True, max_length=255)
    weapon_five_attack_bonus = models.CharField(blank=True, null = True, max_length=255)
    weapon_five_critical = models.CharField(blank=True, null = True, max_length=255)
    weapon_five_type = models.CharField(blank=True, null = True, max_length=255)
    weapon_five_range = models.CharField(blank=True, null = True, max_length=255)
    weapon_five_ammunition = models.CharField(blank=True, null = True, max_length=255)
    weapon_five_damage = models.CharField(blank=True, null = True, max_length=255)
    # skills
    skill_acrobatics_bool = models.BooleanField(default=False)  # 1
    skill_acrobatics_total_bonus = models.CharField(blank=True, null = True, max_length=255)
    skill_acrobatics_attribute_modifiers = models.CharField(blank=True, null = True, max_length=255)
    skill_acrobatics_points_skill = models.CharField(blank=True, null = True, max_length=255)
    skill_acrobatics_misc_mod = models.CharField(blank=True, null = True, max_length=255)
    
    skill_bluff_bool = models.BooleanField(default=False)  # 3
    skill_bluff_total_bonus = models.CharField(blank=True, null = True, max_length=255)
    skill_bluff_attribute_modifiers = models.CharField(blank=True, null = True, max_length=255)
    skill_bluff_points_skill = models.CharField(blank=True, null = True, max_length=255)
    skill_bluff_misc_mod = models.CharField(blank=True, null = True, max_length=255)

    skill_horseback_riding_bool = models.BooleanField(default=False)  # 2
    skill_horseback_riding_total_bonus = models.CharField(blank=True, null = True, max_length=255)
    skill_horseback_riding_attribute_modifiers = models.CharField(blank=True, null = True, max_length=255)
    skill_horseback_riding_points_skill = models.CharField(blank=True, null = True, max_length=255)
    skill_horseback_riding_misc_mod = models.CharField(blank=True, null = True, max_length=255)
    
    
    
    skill_attention_bool = models.BooleanField(default=False)  # 4
    skill_attention_total_bonus = models.CharField(blank=True, null = True, max_length=255)
    skill_attention_misc_attribute_modifiers = models.CharField(blank=True, null = True, max_length=255)
    skill_attention_points_skill = models.CharField(blank=True, null = True, max_length=255)
    skill_attention_misc_mod = models.CharField(blank=True, null = True, max_length=255)
    
    
    
    skill_survival_bool = models.BooleanField(default=False)  # 8
    skill_survival_total_bonus = models.CharField(blank=True, null = True, max_length=255)
    skill_survival_attribute_modifiers = models.CharField(blank=True, null = True, max_length=255)
    skill_survival_points_skill = models.CharField(blank=True, null = True, max_length=255)
    skill_survival_misc_mod = models.CharField(blank=True, null = True, max_length=255)
    
    skill_diplomacy_device_bool = models.BooleanField(default=False)  # 9
    skill_diplomacy_device_total_bonus = models.CharField(blank=True, null = True, max_length=255)
    skill_diplomacy_device_attribute_modifiers = models.CharField(blank=True, null = True, max_length=255)
    skill_diplomacy_device_points_skill = models.CharField(blank=True, null = True, max_length=255)
    skill_diplomacy_device_misc_mod = models.CharField(blank=True, null = True, max_length=255)
    
    skill_training_bool = models.BooleanField(default=False)  # 10
    skill_training_total_bonus = models.CharField(blank=True, null = True, max_length=255)
    skill_training_attribute_modifiers = models.CharField(blank=True, null = True, max_length=255)
    skill_training_points_skill = models.CharField(blank=True, null = True, max_length=255)
    skill_training_misc_mod = models.CharField(blank=True, null = True, max_length=255)
    
    skill_intimidation_artist_bool = models.BooleanField(default=False)  # 11
    skill_intimidation_artist_total_bonus = models.CharField(blank=True, null = True, max_length=255)
    skill_intimidation_artist_attribute_modifiers = models.CharField(blank=True, null = True, max_length=255)
    skill_intimidation_artist_points_skill = models.CharField(blank=True, null = True, max_length=255)
    skill_intimidation_artist_misc_mod = models.CharField(blank=True, null = True, max_length=255)
    
    
    # knowledge
    skill_elite_bool = models.BooleanField(default=False)  # 16
    skill_elite_total_bonus = models.CharField(blank=True, null = True, max_length=255)
    skill_elite_attribute_modifiers = models.CharField(blank=True, null = True, max_length=255)
    skill_elite_points_skill = models.CharField(blank=True, null = True, max_length=255)
    skill_elite_misc_mod = models.CharField(blank=True, null = True, max_length=255)
    
    skill_geography_bool = models.BooleanField(default=False)  # 17
    skill_geography_total_bonus = models.CharField(blank=True, null = True, max_length=255)
    skill_geography_attribute_modifiers = models.CharField(blank=True, null = True, max_length=255)
    skill_geography_points_skill = models.CharField(blank=True, null = True, max_length=255)
    skill_geography_misc_mod = models.CharField(blank=True, null = True, max_length=255)
    
    skill_engineering_bool = models.BooleanField(default=False)  # 18
    skill_engineering_total_bonus = models.CharField(blank=True, null = True, max_length=255)
    skill_engineering_attribute_modifiers = models.CharField(blank=True, null = True, max_length=255)
    skill_engineering_points_skill = models.CharField(blank=True, null = True, max_length=255)
    skill_engineering_misc_mod = models.CharField(blank=True, null = True, max_length=255)
    
    skill_history_bool = models.BooleanField(default=False)  # 19
    skill_history_total_bonus = models.CharField(blank=True, null = True, max_length=255)
    skill_history_attribute_modifiers = models.CharField(blank=True, null = True, max_length=255)
    skill_history_points_skill = models.CharField(blank=True, null = True, max_length=255)
    skill_history_misc_mod = models.CharField(blank=True, null = True, max_length=255)
    
    skill_local_history_bool = models.BooleanField(default=False)  # 20
    skill_local_history_total_bonus = models.CharField(blank=True, null = True, max_length=255)
    skill_local_history_attribute_modifiers = models.CharField(blank=True, null = True, max_length=255)
    skill_local_history_points_skill = models.CharField(blank=True, null = True, max_length=255)
    skill_local_history_misc_mod = models.CharField(blank=True, null = True, max_length=255)
    
    skill_magic_bool = models.BooleanField(default=False)  # 21
    skill_magic_total_bonus = models.CharField(blank=True, null = True, max_length=255)
    skill_magic_attribute_modifiers = models.CharField(blank=True, null = True, max_length=255)
    skill_magic_points_skill = models.CharField(blank=True, null = True, max_length=255)
    skill_magic_misc_mod = models.CharField(blank=True, null = True, max_length=255)
    
    skill_plan_bool = models.BooleanField(default=False)  # 22
    skill_plan_total_bonus = models.CharField(blank=True, null = True, max_length=255)
    skill_plan_attribute_modifiers = models.CharField(blank=True, null = True, max_length=255)
    skill_plan_points_skill = models.CharField(blank=True, null = True, max_length=255)
    skill_plan_misc_mod = models.CharField(blank=True, null = True, max_length=255)
    
    skill_dungeons_bool = models.BooleanField(default=False)  # 23
    skill_dungeons_total_bonus = models.CharField(blank=True, null = True, max_length=255)
    skill_dungeons_attribute_modifiers = models.CharField(blank=True, null = True, max_length=255)
    skill_dungeons_points_skill = models.CharField(blank=True, null = True, max_length=255)
    skill_dungeons_misc_mod = models.CharField(blank=True, null = True, max_length=255)
    
    skill_nature_bool = models.BooleanField(default=False)  # 24
    skill_nature_total_bonus = models.CharField(blank=True, null = True, max_length=255)
    skill_nature_attribute_modifiers = models.CharField(blank=True, null = True, max_length=255)
    skill_nature_points_skill = models.CharField(blank=True, null = True, max_length=255)
    skill_nature_misc_mod = models.CharField(blank=True, null = True, max_length=255)

    skill_religion_bool = models.BooleanField(default=False)  # 24
    skill_religion_total_bonus = models.CharField(blank=True, null = True, max_length=255)
    skill_religion_attribute_modifiers = models.CharField(blank=True, null = True, max_length=255)
    skill_religion_points_skill = models.CharField(blank=True, null = True, max_length=255)
    skill_religion_misc_mod = models.CharField(blank=True, null = True, max_length=255)
    
    
    # скилы после knowledge
    skill_resourcefulness_bool = models.BooleanField(default=False)  # 25
    skill_resourcefulness_total_bonus = models.CharField(blank=True, null = True, max_length=255)
    skill_resourcefulness_attribute_modifiers = models.CharField(blank=True, null = True, max_length=255)
    skill_resourcefulness_points_skill = models.CharField(blank=True, null = True, max_length=255)
    skill_resourcefulness_misc_mod = models.CharField(blank=True, null = True, max_length=255)

    skill_performance_bool = models.BooleanField(default=False)  # 26
    skill_performance_dop = models.CharField(blank=True, null = True, max_length=255)
    skill_performance_total_bonus = models.CharField(blank=True, null = True, max_length=255)
    skill_performance_attribute_modifiers = models.CharField(blank=True, null = True, max_length=255)
    skill_performance_points_skill = models.CharField(blank=True, null = True, max_length=255)
    skill_performance_misc_mod = models.CharField(blank=True, null = True, max_length=255)

    skill_performance_one_bool = models.BooleanField(default=False)  # 26
    skill_performance_one_dop = models.CharField(blank=True, null = True, max_length=255)
    skill_performance_one_total_bonus = models.CharField(blank=True, null = True, max_length=255)
    skill_performance_one_attribute_modifiers = models.CharField(blank=True, null = True, max_length=255)
    skill_performance_one_points_skill = models.CharField(blank=True, null = True, max_length=255)
    skill_performance_one_misc_mod = models.CharField(blank=True, null = True, max_length=255)
    
    skill_use_magic_devices_bool = models.BooleanField(default=False)  # 27
    skill_use_magic_devices_total_bonus = models.CharField(blank=True, null = True, max_length=255)
    skill_use_magic_devices_attribute_modifiers = models.CharField(blank=True, null = True, max_length=255)
    skill_use_magic_devices_points_skill = models.CharField(blank=True, null = True, max_length=255)
    skill_use_magic_devices_misc_mod = models.CharField(blank=True, null = True, max_length=255)

    skill_witchcraft_bool = models.BooleanField(default=False)  # 28
    skill_witchcraft_total_bonus = models.CharField(blank=True, null = True, max_length=255)
    skill_witchcraft_attribute_modifiers = models.CharField(blank=True, null = True, max_length=255)
    skill_witchcraft_points_skill = models.CharField(blank=True, null = True, max_length=255)
    skill_witchcraft_misc_mod = models.CharField(blank=True, null = True, max_length=255)
    
    skill_climbing_bool = models.BooleanField(default=False)  # 32
    skill_climbing_total_bonus = models.CharField(blank=True, null = True, max_length=255)
    skill_climbing_attribute_modifiers = models.CharField(blank=True, null = True, max_length=255)
    skill_climbing_points_skill = models.CharField(blank=True, null = True, max_length=255)
    skill_climbing_misc_mod = models.CharField(blank=True, null = True, max_length=255)
    
    skill_hilling_bool = models.BooleanField(default=False)  # 33
    skill_hilling_total_bonus = models.CharField(blank=True, null = True, max_length=255)
    skill_hilling_attribute_modifiers = models.CharField(blank=True, null = True, max_length=255)
    skill_hilling_points_skill = models.CharField(blank=True, null = True, max_length=255)
    skill_hilling_misc_mod = models.CharField(blank=True, null = True, max_length=255)
    
    skill_sleight_of_hand_bool = models.BooleanField(default=False)  # 34
    skill_sleight_of_hand_total_bonus = models.CharField(blank=True, null = True, max_length=255)
    skill_sleight_of_hand_attribute_modifiers = models.CharField(blank=True, null = True, max_length=255)
    skill_sleight_of_hand_points_skill = models.CharField(blank=True, null = True, max_length=255)
    skill_sleight_of_hand_misc_mod = models.CharField(blank=True, null = True, max_length=255)



    skill_disguise_bool = models.BooleanField(default=False)  # 35
    skill_disguise_total_bonus = models.CharField(blank=True, null = True, max_length=255)
    skill_disguise_attribute_modifiers = models.CharField(blank=True, null = True, max_length=255)
    skill_disguise_points_skill = models.CharField(blank=True, null = True, max_length=255)
    skill_disguise_misc_mod = models.CharField(blank=True, null = True, max_length=255)

    skill_mechanic_bool = models.BooleanField(default=False)  # 36
    skill_mechanic_total_bonus = models.CharField(blank=True, null = True, max_length=255)
    skill_mechanic_attribute_modifiers = models.CharField(blank=True, null = True, max_length=255)
    skill_mechanic_points_skill = models.CharField(blank=True, null = True, max_length=255)
    skill_mechanic_misc_mod = models.CharField(blank=True, null = True, max_length=255)

    skill_grade_bool = models.BooleanField(default=False)  # 37
    skill_grade_total_bonus = models.CharField(blank=True, null = True, max_length=255)
    skill_grade_attribute_modifiers = models.CharField(blank=True, null = True, max_length=255)
    skill_grade_points_skill = models.CharField(blank=True, null = True, max_length=255)
    skill_grade_misc_mod = models.CharField(blank=True, null = True, max_length=255)

    skill_swimming_bool = models.BooleanField(default=False)  # 38
    skill_swimming_total_bonus = models.CharField(blank=True, null = True, max_length=255)
    skill_swimming_attribute_modifiers = models.CharField(blank=True, null = True, max_length=255)
    skill_swimming_points_skill = models.CharField(blank=True, null = True, max_length=255)
    skill_swimming_misc_mod = models.CharField(blank=True, null = True, max_length=255)

    skill_fly_bool = models.BooleanField(default=False)  # 39
    skill_fly_total_bonus = models.CharField(blank=True, null = True, max_length=255)
    skill_fly_attribute_modifiers = models.CharField(blank=True, null = True, max_length=255)
    skill_fly_points_skill = models.CharField(blank=True, null = True, max_length=255)
    skill_fly_misc_mod = models.CharField(blank=True, null = True, max_length=255)

    skill_permeability_bool = models.BooleanField(default=False)  # 40
    skill_permeability_total_bonus = models.CharField(blank=True, null = True, max_length=255)
    skill_permeability_attribute_modifiers = models.CharField(blank=True, null = True, max_length=255)
    skill_permeability_points_skill = models.CharField(blank=True, null = True, max_length=255)
    skill_permeability_misc_mod = models.CharField(blank=True, null = True, max_length=255)

    skill_profession_one_bool = models.BooleanField(default=False)  # 30 тут еще есть строка которую нужно заполнить, я не сделал доп модель для неё
    skill_profession_one_dop = models.CharField(blank=True, null = True, max_length=255)
    skill_profession_one_total_bonus = models.CharField(blank=True, null = True, max_length=255)
    skill_profession_one_attribute_modifiers = models.CharField(blank=True, null = True, max_length=255)
    skill_profession_one_points_skill = models.CharField(blank=True, null = True, max_length=255)
    skill_profession_one_misc_mod = models.CharField(blank=True, null = True, max_length=255)
    
    skill_profession_two_bool = models.BooleanField(default=False)  # 31 тут еще есть строка которую нужно заполнить, я не сделал доп модель для неё
    skill_profession_two_dop = models.CharField(blank=True, null = True, max_length=255)
    skill_profession_two_total_bonus = models.CharField(blank=True, null = True, max_length=255)
    skill_profession_two_attribute_modifiers = models.CharField(blank=True, null = True, max_length=255)
    skill_profession_two_points_skill = models.CharField(blank=True, null = True, max_length=255)
    skill_profession_two_misc_mod = models.CharField(blank=True, null = True, max_length=255)
    
    skill_craft_one_bool = models.BooleanField(default=False)  # 5
    skill_craft_one_dop = models.CharField(blank=True, null = True, max_length=255)
    skill_craft_one_total_bonus = models.CharField(blank=True, null = True, max_length=255)
    skill_craft_one_attribute_modifiers = models.CharField(blank=True, null = True, max_length=255)
    skill_craft_one_points_skill = models.CharField(blank=True, null = True, max_length=255)
    skill_craft_one_misc_mod = models.CharField(blank=True, null = True, max_length=255)
    
    skill_craft_two_bool = models.BooleanField(default=False)  # 6
    skill_craft_two_dop = models.CharField(blank=True, null = True, max_length=255)
    skill_craft_two_total_bonus = models.CharField(blank=True, null = True, max_length=255)
    skill_craft_two_attribute_modifiers = models.CharField(blank=True, null = True, max_length=255)
    skill_craft_two_points_skill = models.CharField(blank=True, null = True, max_length=255)
    skill_craft_two_misc_mod = models.CharField(blank=True, null = True, max_length=255)
    
    skill_craft_three_bool = models.BooleanField(default=False)  # 7
    skill_craft_three_dop = models.CharField(blank=True, null = True, max_length=255)
    skill_craft_three_total_bonus = models.CharField(blank=True, null = True, max_length=255)
    skill_craft_three_attribute_modifiers = models.CharField(blank=True, null = True, max_length=255)
    skill_craft_three_points_skill = models.CharField(blank=True, null = True, max_length=255)
    skill_craft_three_misc_mod = models.CharField(blank=True, null = True, max_length=255)
    
    skill_secrecy_bool = models.BooleanField(default=False)  # 37
    skill_secrecy_total_bonus = models.CharField(blank=True, null = True, max_length=255)
    skill_secrecy_attribute_modifiers = models.CharField(blank=True, null = True, max_length=255)
    skill_secrecy_points_skill = models.CharField(blank=True, null = True, max_length=255)
    skill_secrecy_misc_mod = models.CharField(blank=True, null = True, max_length=255)
    
    skill_languachies_bool = models.BooleanField(default=False)  # 37
    skill_languachies_total_bonus = models.CharField(blank=True, null = True, max_length=255)
    skill_languachies_attribute_modifiers = models.CharField(blank=True, null = True, max_length=255)
    skill_languachies_points_skill = models.CharField(blank=True, null = True, max_length=255)
    skill_languachies_misc_mod = models.CharField(blank=True, null = True, max_length=255)

    #модификаторы обстоятельств
    
    circumstance_modifier_one = models.CharField(blank=True, null = True, max_length=255)
    circumstance_modifier_two = models.CharField(blank=True, null = True, max_length=255)
    
    #языки
    languachies_one = models.CharField(blank=True, null = True, max_length=255)
    languachies_two = models.CharField(blank=True, null = True, max_length=255)
    languachies_three = models.CharField(blank=True, null = True, max_length=255)

    # предметы
    ac_items_one = models.CharField(blank=True, null = True, max_length=255)
    ac_items_two = models.CharField(blank=True, null = True, max_length=255)
    ac_items_three = models.CharField(blank=True, null = True, max_length=255)
    ac_items_four = models.CharField(blank=True, null = True, max_length=255)
    ac_items_five = models.CharField(blank=True, null = True, max_length=255)
    # bonus
    bonus_one = models.CharField(blank=True, null = True, max_length=255)
    bonus_two = models.CharField(blank=True, null = True, max_length=255)
    bonus_three = models.CharField(blank=True, null = True, max_length=255)
    bonus_four = models.CharField(blank=True, null = True, max_length=255)
    bonus_five = models.CharField(blank=True, null = True, max_length=255)
    bonus_totals = models.CharField(blank=True, null = True, max_length=255)
    # type
    type_one = models.CharField(blank=True, null = True, max_length=255)
    type_two = models.CharField(blank=True, null = True, max_length=255)
    type_three = models.CharField(blank=True, null = True, max_length=255)
    type_four = models.CharField(blank=True, null = True, max_length=255)
    type_five = models.CharField(blank=True, null = True, max_length=255)
    type_totals = models.CharField(blank=True, null = True, max_length=255)
    # check_penalty
    check_penalty_one = models.CharField(blank=True, null = True, max_length=255)
    check_penalty_two = models.CharField(blank=True, null = True, max_length=255)
    check_penalty_three = models.CharField(blank=True, null = True, max_length=255)
    check_penalty_four = models.CharField(blank=True, null = True, max_length=255)
    check_penalty_five = models.CharField(blank=True, null = True, max_length=255)
    check_penalty_totals = models.CharField(blank=True, null = True, max_length=255)
    # spell_failure
    spell_failure_one = models.CharField(blank=True, null = True, max_length=255)
    spell_failure_two = models.CharField(blank=True, null = True, max_length=255)
    spell_failure_three = models.CharField(blank=True, null = True, max_length=255)
    spell_failure_four = models.CharField(blank=True, null = True, max_length=255)
    spell_failure_five = models.CharField(blank=True, null = True, max_length=255)
    spell_failure_totals = models.CharField(blank=True, null = True, max_length=255)
    # weight
    weight_one = models.CharField(blank=True, null = True, max_length=255)
    weight_two = models.CharField(blank=True, null = True, max_length=255)
    weight_three = models.CharField(blank=True, null = True, max_length=255)
    weight_four = models.CharField(blank=True, null = True, max_length=255)
    weight_five = models.CharField(blank=True, null = True, max_length=255)
    weight_totals = models.CharField(blank=True, null = True, max_length=255)
    
    light_load =  models.CharField(blank=True, null = True, max_length=255)
    middle_load =  models.CharField(blank=True, null = True, max_length=255)
    big_load =  models.CharField(blank=True, null = True, max_length=255)
    raise_overhead =  models.CharField(blank=True, null = True, max_length=255)
    tear_off_the_ground = models.CharField(blank=True, null = True, max_length=255)
    push_or_drag = models.CharField(blank=True, null = True, max_length=255)
    # properties
    properties_one = models.CharField(blank=True, null = True, max_length=255)
    properties_two = models.CharField(blank=True, null = True, max_length=255)
    properties_three = models.CharField(blank=True, null = True, max_length=255)
    properties_four = models.CharField(blank=True, null = True, max_length=255)
    properties_five = models.CharField(blank=True, null = True, max_length=255)
    properties_totals = models.CharField(blank=True, null = True, max_length=255)

    #equipment
    equipment_1 = models.CharField(blank=True, null = True, max_length=255)
    equipment_1_ves = models.CharField(blank=True, null = True, max_length=255)
    equipment_2 = models.CharField(blank=True, null = True, max_length=255)
    equipment_2_ves = models.CharField(blank=True, null = True, max_length=255)
    equipment_3 = models.CharField(blank=True, null = True, max_length=255)
    equipment_3_ves = models.CharField(blank=True, null = True, max_length=255)
    equipment_4 = models.CharField(blank=True, null = True, max_length=255)
    equipment_4_ves = models.CharField(blank=True, null = True, max_length=255)
    equipment_5 = models.CharField(blank=True, null = True, max_length=255)
    equipment_5_ves = models.CharField(blank=True, null = True, max_length=255)
    equipment_6 = models.CharField(blank=True, null = True, max_length=255)
    equipment_6_ves = models.CharField(blank=True, null = True, max_length=255)
    equipment_7 = models.CharField(blank=True, null = True, max_length=255)
    equipment_7_ves = models.CharField(blank=True, null = True, max_length=255)
    equipment_8 = models.CharField(blank=True, null = True, max_length=255)
    equipment_8_ves = models.CharField(blank=True, null = True, max_length=255)
    equipment_9 = models.CharField(blank=True, null = True, max_length=255)
    equipment_9_ves = models.CharField(blank=True, null = True, max_length=255)
    equipment_10 = models.CharField(blank=True, null = True, max_length=255)
    equipment_10_ves = models.CharField(blank=True, null = True, max_length=255)
    equipment_11 = models.CharField(blank=True, null = True, max_length=255)
    equipment_11_ves = models.CharField(blank=True, null = True, max_length=255)
    equipment_12 = models.CharField(blank=True, null = True, max_length=255)
    equipment_12_ves = models.CharField(blank=True, null = True, max_length=255)
    equipment_13 = models.CharField(blank=True, null = True, max_length=255)
    equipment_13_ves = models.CharField(blank=True, null = True, max_length=255)
    equipment_14 = models.CharField(blank=True, null = True, max_length=255)
    equipment_14_ves = models.CharField(blank=True, null = True, max_length=255)
    equipment_15 = models.CharField(blank=True, null = True, max_length=255)
    equipment_15_ves = models.CharField(blank=True, null = True, max_length=255)
    equipment_16 = models.CharField(blank=True, null = True, max_length=255)
    equipment_16_ves = models.CharField(blank=True, null = True, max_length=255)
    equipment_17 = models.CharField(blank=True, null = True, max_length=255)
    equipment_17_ves = models.CharField(blank=True, null = True, max_length=255)
    equipment_18 = models.CharField(blank=True, null = True, max_length=255)
    equipment_18_ves = models.CharField(blank=True, null = True, max_length=255)
    equipment_19 = models.CharField(blank=True, null = True, max_length=255)
    equipment_19_ves = models.CharField(blank=True, null = True, max_length=255)
    equipment_20 = models.CharField(blank=True, null = True, max_length=255)
    equipment_20_ves = models.CharField(blank=True, null = True, max_length=255)
    equipment_21 = models.CharField(blank=True, null = True, max_length=255)
    equipment_21_ves = models.CharField(blank=True, null = True, max_length=255)
    equipment_22 = models.CharField(blank=True, null = True, max_length=255)
    equipment_22_ves = models.CharField(blank=True, null = True, max_length=255)
    equipment_23 = models.CharField(blank=True, null = True, max_length=255)
    equipment_23_ves = models.CharField(blank=True, null = True, max_length=255)
    equipment_24 = models.CharField(blank=True, null = True, max_length=255)
    equipment_24_ves = models.CharField(blank=True, null = True, max_length=255)
    equipment_25 = models.CharField(blank=True, null = True, max_length=255)
    equipment_25_ves = models.CharField(blank=True, null = True, max_length=255)
    equipment_26 = models.CharField(blank=True, null = True, max_length=255)
    equipment_26_ves = models.CharField(blank=True, null = True, max_length=255)
    equipment_27 = models.CharField(blank=True, null = True, max_length=255)
    equipment_27_ves = models.CharField(blank=True, null = True, max_length=255)
    equipment_28 = models.CharField(blank=True, null = True, max_length=255)
    equipment_28_ves = models.CharField(blank=True, null = True, max_length=255)
    equipment_29 = models.CharField(blank=True, null = True, max_length=255)
    equipment_29_ves = models.CharField(blank=True, null = True, max_length=255)
    equipment_30 = models.CharField(blank=True, null = True, max_length=255)
    equipment_30_ves = models.CharField(blank=True, null = True, max_length=255)
    equipment_total = models.CharField(blank=True, null = True, max_length=255)


    # feats
    feats_1 = models.CharField(blank=True, null = True, max_length=255)
    feats_2 = models.CharField(blank=True, null = True, max_length=255)
    feats_3 = models.CharField(blank=True, null = True, max_length=255)
    feats_4 = models.CharField(blank=True, null = True, max_length=255)
    feats_5 = models.CharField(blank=True, null = True, max_length=255)
    feats_6 = models.CharField(blank=True, null = True, max_length=255)
    feats_7 = models.CharField(blank=True, null = True, max_length=255)
    feats_8 = models.CharField(blank=True, null = True, max_length=255)
    feats_9 = models.CharField(blank=True, null = True, max_length=255)
    feats_10 = models.CharField(blank=True, null = True, max_length=255)
    feats_11 = models.CharField(blank=True, null = True, max_length=255)
    feats_12 = models.CharField(blank=True, null = True, max_length=255)
    feats_13 = models.CharField(blank=True, null = True, max_length=255)
    feats_14 = models.CharField(blank=True, null = True, max_length=255)
    # special_abilities
    special_abilities = models.CharField(blank=True, null = True, max_length=255)
    special_abilities_1 = models.CharField(blank=True, null = True, max_length=255)
    special_abilities_2 = models.CharField(blank=True, null = True, max_length=255)
    special_abilities_3 = models.CharField(blank=True, null = True, max_length=255)
    special_abilities_4 = models.CharField(blank=True, null = True, max_length=255)
    special_abilities_5 = models.CharField(blank=True, null = True, max_length=255)
    special_abilities_6 = models.CharField(blank=True, null = True, max_length=255)
    special_abilities_7 = models.CharField(blank=True, null = True, max_length=255)
    special_abilities_8 = models.CharField(blank=True, null = True, max_length=255)
    special_abilities_9 = models.CharField(blank=True, null = True, max_length=255)
    special_abilities_10 = models.CharField(blank=True, null = True, max_length=255)
    special_abilities_11 = models.CharField(blank=True, null = True, max_length=255)
    special_abilities_12 = models.CharField(blank=True, null = True, max_length=255)
    special_abilities_13 = models.CharField(blank=True, null = True, max_length=255)
    special_abilities_14 = models.CharField(blank=True, null = True, max_length=255)
    special_abilities_15 = models.CharField(blank=True, null = True, max_length=255)
    special_abilities_16 = models.CharField(blank=True, null = True, max_length=255)
    special_abilities_17 = models.CharField(blank=True, null = True, max_length=255)
    special_abilities_18 = models.CharField(blank=True, null = True, max_length=255)
    special_abilities_19 = models.CharField(blank=True, null = True, max_length=255)
    special_abilities_20 = models.CharField(blank=True, null = True, max_length=255)
    special_abilities_21 = models.CharField(blank=True, null = True, max_length=255)
    special_abilities_22 = models.CharField(blank=True, null = True, max_length=255)
    special_abilities_23 = models.CharField(blank=True, null = True, max_length=255)
    special_abilities_24 = models.CharField(blank=True, null = True, max_length=255)
    special_abilities_25 = models.CharField(blank=True, null = True, max_length=255)
    special_abilities_26 = models.CharField(blank=True, null = True, max_length=255)
    # spells
    # lvl0
    spells_known_lvl0 = models.CharField(blank=True, null = True, max_length=255)
    spell_save_dc_lvl0 = models.CharField(blank=True, null = True, max_length=255)
    spells_per_day_lvl0 = models.CharField(blank=True, null = True, max_length=255)
    spells_bonus_lvl0 = models.CharField(blank=True, null = True, max_length=255)
    # lvl1
    spells_known_lvl1 = models.CharField(blank=True, null = True, max_length=255)
    spell_save_dc_lvl1 = models.CharField(blank=True, null = True, max_length=255)
    spells_per_day_lvl1 = models.CharField(blank=True, null = True, max_length=255)
    spells_bonus_lvl1 = models.CharField(blank=True, null = True, max_length=255)
    # lvl2
    spells_known_lvl2 = models.CharField(blank=True, null = True, max_length=255)
    spell_save_dc_lvl2 = models.CharField(blank=True, null = True, max_length=255)
    spells_per_day_lvl2 = models.CharField(blank=True, null = True, max_length=255)
    spells_bonus_lvl2 = models.CharField(blank=True, null = True, max_length=255)
    # lvl3
    spells_known_lvl3 = models.CharField(blank=True, null = True, max_length=255)
    spell_save_dc_lvl3 = models.CharField(blank=True, null = True, max_length=255)
    spells_per_day_lvl3 = models.CharField(blank=True, null = True, max_length=255)
    spells_bonus_lvl3 = models.CharField(blank=True, null = True, max_length=255)
    # lvl4
    spells_known_lvl4 = models.CharField(blank=True, null = True, max_length=255)
    spell_save_dc_lvl4 = models.CharField(blank=True, null = True, max_length=255)
    spells_per_day_lvl4 = models.CharField(blank=True, null = True, max_length=255)
    spells_bonus_lvl4 = models.CharField(blank=True, null = True, max_length=255)
    # lvl5
    spells_known_lvl5 = models.CharField(blank=True, null = True, max_length=255)
    spell_save_dc_lvl5 = models.CharField(blank=True, null = True, max_length=255)
    spells_per_day_lvl5 = models.CharField(blank=True, null = True, max_length=255)
    spells_bonus_lvl5 = models.CharField(blank=True, null = True, max_length=255)
    # lvl6
    spells_known_lvl6 = models.CharField(blank=True, null = True, max_length=255)
    spell_save_dc_lvl6 = models.CharField(blank=True, null = True, max_length=255)
    spells_per_day_lvl6 = models.CharField(blank=True, null = True, max_length=255)
    spells_bonus_lvl6 = models.CharField(blank=True, null = True, max_length=255)
    # lvl7
    spells_known_lvl7 = models.CharField(blank=True, null = True, max_length=255)
    spell_save_dc_lvl7 = models.CharField(blank=True, null = True, max_length=255)
    spells_per_day_lvl7 = models.CharField(blank=True, null = True, max_length=255)
    spells_bonus_lvl7 = models.CharField(blank=True, null = True, max_length=255)
    # lvl8
    spells_known_lvl8 = models.CharField(blank=True, null = True, max_length=255)
    spell_save_dc_lvl8 = models.CharField(blank=True, null = True, max_length=255)
    spells_per_day_lvl8 = models.CharField(blank=True, null = True, max_length=255)
    spells_bonus_lvl8 = models.CharField(blank=True, null = True, max_length=255)
    # lvl9
    spells_known_lvl9 = models.CharField(blank=True, null = True, max_length=255)
    spell_save_dc_lvl9 = models.CharField(blank=True, null = True, max_length=255)
    spells_per_day_lvl9 = models.CharField(blank=True, null = True, max_length=255)
    spells_bonus_lvl9 = models.CharField(blank=True, null = True, max_length=255)
    conditional_modifiers = models.CharField(blank=True, null = True, max_length=255)
    #spheres/specializations_sсhool
    Circumstance_modifiers = models.CharField(blank=True, null = True, max_length=255)
    #School_of_Incarnation-0
    School_of_Incarnation_1 = models.CharField(blank=True, null = True, max_length=255)
    School_of_Incarnation_2 = models.CharField(blank=True, null = True, max_length=255)
    School_of_Incarnation_3 = models.CharField(blank=True, null = True, max_length=255)
    School_of_Incarnation_4 = models.CharField(blank=True, null = True, max_length=255)
    School_of_Incarnation_5 = models.CharField(blank=True, null = True, max_length=255)
    School_of_Incarnation_6 = models.CharField(blank=True, null = True, max_length=255)
    School_of_Incarnation_7 = models.CharField(blank=True, null = True, max_length=255)
    School_of_Incarnation_8 = models.CharField(blank=True, null = True, max_length=255)
    #School_of_illusion-1
    School_of_illusion_1 = models.CharField(blank=True, null = True, max_length=255)
    School_of_illusion_2 = models.CharField(blank=True, null = True, max_length=255)
    School_of_illusion_3 = models.CharField(blank=True, null = True, max_length=255)
    School_of_illusion_4 = models.CharField(blank=True, null = True, max_length=255)
    School_of_illusion_5 = models.CharField(blank=True, null = True, max_length=255)
    School_of_illusion_6 = models.CharField(blank=True, null = True, max_length=255)
    School_of_illusion_7 = models.CharField(blank=True, null = True, max_length=255)
    School_of_illusion_8 = models.CharField(blank=True, null = True, max_length=255)
    #School_of_Necromancy-2
    School_of_Necromancy_1 = models.CharField(blank=True, null = True, max_length=255)
    School_of_Necromancy_2 = models.CharField(blank=True, null = True, max_length=255)
    School_of_Necromancy_3 = models.CharField(blank=True, null = True, max_length=255)
    School_of_Necromancy_4 = models.CharField(blank=True, null = True, max_length=255)
    School_of_Necromancy_5 = models.CharField(blank=True, null = True, max_length=255)
    School_of_Necromancy_6 = models.CharField(blank=True, null = True, max_length=255)
    School_of_Necromancy_7 = models.CharField(blank=True, null = True, max_length=255)
    School_of_Necromancy_8 = models.CharField(blank=True, null = True, max_length=255)
    #School_of_charm-3
    School_of_charm_1 = models.CharField(blank=True, null = True, max_length=255)
    School_of_charm_2 = models.CharField(blank=True, null = True, max_length=255)
    School_of_charm_3 = models.CharField(blank=True, null = True, max_length=255)
    School_of_charm_4 = models.CharField(blank=True, null = True, max_length=255)
    School_of_charm_5 = models.CharField(blank=True, null = True, max_length=255)
    School_of_charm_6 = models.CharField(blank=True, null = True, max_length=255)
    School_of_charm_7 = models.CharField(blank=True, null = True, max_length=255)
    School_of_charm_8 = models.CharField(blank=True, null = True, max_length=255)
    #School_of_transformation
    School_of_transformation_1 = models.CharField(blank=True, null = True, max_length=255)
    School_of_transformation_2 = models.CharField(blank=True, null = True, max_length=255)
    School_of_transformation_3 = models.CharField(blank=True, null = True, max_length=255)
    School_of_transformation_4 = models.CharField(blank=True, null = True, max_length=255)
    School_of_transformation_5 = models.CharField(blank=True, null = True, max_length=255)
    School_of_transformation_6 = models.CharField(blank=True, null = True, max_length=255)
    School_of_transformation_7 = models.CharField(blank=True, null = True, max_length=255)
    School_of_transformation_8 = models.CharField(blank=True, null = True, max_length=255)
    #Obstruction_school
    Obstruction_school_1 = models.CharField(blank=True, null = True, max_length=255)
    Obstruction_school_2 = models.CharField(blank=True, null = True, max_length=255)
    Obstruction_school_3 = models.CharField(blank=True, null = True, max_length=255)
    Obstruction_school_4 = models.CharField(blank=True, null = True, max_length=255)
    Obstruction_school_5 = models.CharField(blank=True, null = True, max_length=255)
    Obstruction_school_6 = models.CharField(blank=True, null = True, max_length=255)
    Obstruction_school_7 = models.CharField(blank=True, null = True, max_length=255)
    Obstruction_school_8 = models.CharField(blank=True, null = True, max_length=255)
    #School_of_Divination
    School_of_Divination_1 = models.CharField(blank=True, null = True, max_length=255)
    School_of_Divination_2 = models.CharField(blank=True, null = True, max_length=255)
    School_of_Divination_3 = models.CharField(blank=True, null = True, max_length=255)
    School_of_Divination_4 = models.CharField(blank=True, null = True, max_length=255)
    School_of_Divination_5 = models.CharField(blank=True, null = True, max_length=255)
    School_of_Divination_6 = models.CharField(blank=True, null = True, max_length=255)
    School_of_Divination_7 = models.CharField(blank=True, null = True, max_length=255)
    School_of_Divination_8 = models.CharField(blank=True, null = True, max_length=255)
    #School_of_destruction
    School_of_destruction_1 = models.CharField(blank=True, null = True, max_length=255)
    School_of_destruction_2 = models.CharField(blank=True, null = True, max_length=255)
    School_of_destruction_3 = models.CharField(blank=True, null = True, max_length=255)
    School_of_destruction_4 = models.CharField(blank=True, null = True, max_length=255)
    School_of_destruction_5 = models.CharField(blank=True, null = True, max_length=255)
    School_of_destruction_6 = models.CharField(blank=True, null = True, max_length=255)
    School_of_destruction_7 = models.CharField(blank=True, null = True, max_length=255)
    School_of_destruction_8 = models.CharField(blank=True, null = True, max_length=255)
    #School_of_Universalism
    School_of_Universalism_1 = models.CharField(blank=True, null = True, max_length=255)
    School_of_Universalism_2 = models.CharField(blank=True, null = True, max_length=255)
    School_of_Universalism_3 = models.CharField(blank=True, null = True, max_length=255)
    School_of_Universalism_4 = models.CharField(blank=True, null = True, max_length=255)
    School_of_Universalism_5 = models.CharField(blank=True, null = True, max_length=255)
    School_of_Universalism_6 = models.CharField(blank=True, null = True, max_length=255)
    School_of_Universalism_7 = models.CharField(blank=True, null = True, max_length=255)
    School_of_Universalism_8 = models.CharField(blank=True, null = True, max_length=255)
    #money
    money_MM = models.CharField(blank=True, null = True, max_length=255)
    money_CM = models.CharField(blank=True, null = True, max_length=255)
    money_3M =  models.CharField(blank=True, null = True, max_length=255)
    money_PM =  models.CharField(blank=True, null = True, max_length=255)
    experience =  models.CharField(blank=True, null = True, max_length=255)
    following_experience =  models.CharField(blank=True, null = True, max_length=255)


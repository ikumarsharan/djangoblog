from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from django.templatetags.static import static
from django.urls import reverse

class Profile(models.Model):
    GENDER_MALE = 1
    GENDER_FEMALE = 2
    GENDER_OTHER = 3
    GENDER_NOT = 4
    GENDER_CHOICES = [
        (GENDER_MALE, ("Male")),
        (GENDER_FEMALE, ("Female")),
        (GENDER_OTHER, ("Other")),
        (GENDER_NOT, ("Preferred not to say")),
    ]

    EDU_UG = 1
    EDU_PG = 2
    EDU_VOC = 3
    EDU_HSE = 4
    EDU_SE = 5
    EDU_EE = 6
    EDU_CHOICES = [
        (EDU_UG, ("Under Graduate")),
        (EDU_PG, ("Post Graduates")),
        (EDU_VOC, ("Vocational")),
        (EDU_HSE, ("Higher Secondary Education")),
        (EDU_SE, ("Secondary Education")),
        (EDU_EE, ("Elementary Education")),
    ]

    COUNTRY_1 = 1
    COUNTRY_2 = 2
    COUNTRY_3 = 3
    COUNTRY_4 = 4
    COUNTRY_5 = 5
    COUNTRY_6 = 6
    COUNTRY_7 = 7
    COUNTRY_8 = 8
    COUNTRY_9=9
    COUNTRY_10=10
    COUNTRY_11=11
    COUNTRY_12=12
    COUNTRY_13=13
    COUNTRY_14=14
    COUNTRY_15=15
    COUNTRY_16=16
    COUNTRY_17=17
    COUNTRY_18=18
    COUNTRY_19=19 
    COUNTRY_20=20
    COUNTRY_21=21
    COUNTRY_22=22
    COUNTRY_23=23
    COUNTRY_24=24
    COUNTRY_25=25
    COUNTRY_26=26
    COUNTRY_27=27
    COUNTRY_28=28
    COUNTRY_29=29
    COUNTRY_30=30
    COUNTRY_31=31
    COUNTRY_32=32
    COUNTRY_33=33
    COUNTRY_34=34
    COUNTRY_35=35
    COUNTRY_36=36
    COUNTRY_37=37
    COUNTRY_38=38
    COUNTRY_39=39
    COUNTRY_40=40
    COUNTRY_41=41
    COUNTRY_42=42
    COUNTRY_43=43
    COUNTRY_44=44
    COUNTRY_45=45
    COUNTRY_46=46
    COUNTRY_47=47
    COUNTRY_48=48
    COUNTRY_49=49
    COUNTRY_50=50
    COUNTRY_51=51
    COUNTRY_52=52
    COUNTRY_53=53
    COUNTRY_54=54
    COUNTRY_55=55
    COUNTRY_56=56
    COUNTRY_57=57
    COUNTRY_58=58
    COUNTRY_59=59
    COUNTRY_60=60
    COUNTRY_61=61
    COUNTRY_62=62
    COUNTRY_63=63
    COUNTRY_64=64
    COUNTRY_65=65
    COUNTRY_66=66
    COUNTRY_67=67
    COUNTRY_68=68
    COUNTRY_69=69
    COUNTRY_70=70
    COUNTRY_71=71
    COUNTRY_72=72
    COUNTRY_73=73
    COUNTRY_74=74
    COUNTRY_75=75
    COUNTRY_76=76
    COUNTRY_77=77
    COUNTRY_78=78
    COUNTRY_79=79
    COUNTRY_80=80
    COUNTRY_81=81
    COUNTRY_82=82
    COUNTRY_83=83
    COUNTRY_84=84
    COUNTRY_85=85
    COUNTRY_86=86
    COUNTRY_87=87
    COUNTRY_88=88
    COUNTRY_89=89
    COUNTRY_90=90
    COUNTRY_91=91
    COUNTRY_92=92
    COUNTRY_93=93
    COUNTRY_94=94
    COUNTRY_95=95
    COUNTRY_96=96
    COUNTRY_97=97
    COUNTRY_98=98
    COUNTRY_99=99
    COUNTRY_100=100
    COUNTRY_101=101
    COUNTRY_102=102
    COUNTRY_103=103
    COUNTRY_104=104
    COUNTRY_105=105
    COUNTRY_106=106
    COUNTRY_107=107
    COUNTRY_108=108
    COUNTRY_109=109
    COUNTRY_110=110
    COUNTRY_111=111
    COUNTRY_112=112
    COUNTRY_113=113
    COUNTRY_114=114
    COUNTRY_115=115
    COUNTRY_116=116
    COUNTRY_117=117
    COUNTRY_118=118
    COUNTRY_119=119
    COUNTRY_120=120
    COUNTRY_121=121
    COUNTRY_122=122
    COUNTRY_123=123
    COUNTRY_124=124
    COUNTRY_125=125
    COUNTRY_126=126
    COUNTRY_127=127
    COUNTRY_128=128
    COUNTRY_129=129
    COUNTRY_130=130
    COUNTRY_131=131
    COUNTRY_132=132
    COUNTRY_133=133
    COUNTRY_134=134
    COUNTRY_135=135
    COUNTRY_136=136
    COUNTRY_137=137
    COUNTRY_138=138
    COUNTRY_139=139
    COUNTRY_140=140
    COUNTRY_141=141
    COUNTRY_142=142
    COUNTRY_143 = 143
    COUNTRY_144=144
    COUNTRY_145=145
    COUNTRY_146=146
    COUNTRY_147=147
    COUNTRY_148=148
    COUNTRY_149=149
    COUNTRY_150=150
    COUNTRY_151=151
    COUNTRY_152=152
    COUNTRY_153=153
    COUNTRY_154=154
    COUNTRY_155=155
    COUNTRY_156=156
    COUNTRY_157=157
    COUNTRY_158=158
    COUNTRY_159=159
    COUNTRY_160=160
    COUNTRY_161=161
    COUNTRY_162=162
    COUNTRY_163=163
    COUNTRY_164=164
    COUNTRY_165=165
    COUNTRY_166=166
    COUNTRY_167=167
    COUNTRY_168=168
    COUNTRY_169=169
    COUNTRY_170=170
    COUNTRY_171=171
    COUNTRY_172=172
    COUNTRY_173=173
    COUNTRY_174=174
    COUNTRY_175=175
    COUNTRY_176=176
    COUNTRY_177=177
    COUNTRY_178=178
    COUNTRY_179=179
    COUNTRY_180=180
    COUNTRY_181=181
    COUNTRY_182=182
    COUNTRY_183=183
    COUNTRY_184=184
    COUNTRY_185=185
    COUNTRY_186=186
    COUNTRY_187=187
    COUNTRY_188=188
    COUNTRY_189=189
    COUNTRY_190=190
    COUNTRY_191=191
    COUNTRY_192=192
    COUNTRY_193=193
    COUNTRY_194=194
    COUNTRY_195=195
    
    COUNTRY_CHOICES = [
        (COUNTRY_78, ('India')),
        (COUNTRY_1, ('Afghanistan')),
        (COUNTRY_2, ('Albania')),
        (COUNTRY_3, ('Algeria')), 
        (COUNTRY_4,('Andorra')),
        (COUNTRY_5, ('Angola')),
        (COUNTRY_6, ('Antigua and Barbuda')),
        (COUNTRY_7, ('Argentina')),
        (COUNTRY_8, ('Armenia')),
        (COUNTRY_9, ('Australia')),
        (COUNTRY_10, ('Austria')),
        (COUNTRY_11, ('Azerbaijan')),
        (COUNTRY_12, ('Bahamas')),
        (COUNTRY_13, ('Bahrain')),
        (COUNTRY_14, ('Bangladesh')),
        (COUNTRY_15, ('Barbados')),
        (COUNTRY_16, ('Belarus')),
        (COUNTRY_17, ('Belgium')),
        (COUNTRY_18, ('Belize')),
        (COUNTRY_19, ('Benin')),
        (COUNTRY_20, ('Bhutan')),
        (COUNTRY_21, ('Bolivia')),
        (COUNTRY_22, ('Bosnia and Herzegovina')),
        (COUNTRY_23, ('Botswana')),
        (COUNTRY_24, ('Brazil')),
        (COUNTRY_25, ('Brunei')),
        (COUNTRY_26, ('Bulgaria')),
        (COUNTRY_27, ('Burkina Faso')),
        (COUNTRY_28, ('Burundi')),
        (COUNTRY_29, ("Cote d'Ivoire'")),
        (COUNTRY_30, ('Cabo Verde')),
        (COUNTRY_31, ('Cambodia')),
        (COUNTRY_32, ('Cameroon')),
        (COUNTRY_33, ('Canada')),
        (COUNTRY_34, ('Central African Republic')),
        (COUNTRY_35, ('Chad')),
        (COUNTRY_36, ('Chile')),
        (COUNTRY_37, ('China')),
        (COUNTRY_38, ('Colombia')),
        (COUNTRY_39, ('Comoros')),
        (COUNTRY_40, ('Congo (Congo-Brazzaville)')),
        (COUNTRY_41, ('Costa Rica')),
        (COUNTRY_42, ('Croatia')),
        (COUNTRY_43, ('Cuba')),
        (COUNTRY_44, ('Cyprus')),
        (COUNTRY_45, ('Czechia (Czech Republic)')),
        (COUNTRY_46, ('Democratic Republic of the Congo')),
        (COUNTRY_47, ('Denmark')),
        (COUNTRY_48, ('Djibouti')),
        (COUNTRY_49, ('Dominica')),
        (COUNTRY_50, ('Dominican Republic')),
        (COUNTRY_51, ('Ecuador')),
        (COUNTRY_52, ('Egypt')),
        (COUNTRY_53, ('El Salvador')),
        (COUNTRY_54, ('Equatorial Guinea')),
        (COUNTRY_55, ('Eritrea')),
        (COUNTRY_56, ('Estonia')),
        (COUNTRY_57, ('Eswatini (fmr. "Swaziland")')),
        (COUNTRY_58, ('Ethiopia')),
        (COUNTRY_59, ('Fiji')),
        (COUNTRY_60, ('Finland')),
        (COUNTRY_61, ('France')),
        (COUNTRY_62, ('Gabon')),
        (COUNTRY_63, ('Gambia')),
        (COUNTRY_64, ('Georgia')),
        (COUNTRY_65, ('Germany')),
        (COUNTRY_66, ('Ghana')),
        (COUNTRY_67, ('Greece')),
        (COUNTRY_68, ('Grenada')),
        (COUNTRY_69, ('Guatemala')),
        (COUNTRY_70, ('Guinea')),
        (COUNTRY_71, ('Guinea-Bissau')),
        (COUNTRY_72, ('Guyana')),
        (COUNTRY_73, ('Haiti')),
        (COUNTRY_74, ('Holy See')),
        (COUNTRY_75, ('Honduras')),
        (COUNTRY_76, ('Hungary')),
        (COUNTRY_77, ('Iceland')),
        (COUNTRY_79, ('Indonesia')),
        (COUNTRY_80, ('Iran')),
        (COUNTRY_81, ('Iraq')),
        (COUNTRY_82, ('Ireland')),
        (COUNTRY_83, ('Israel')),
        (COUNTRY_84, ('Italy')),
        (COUNTRY_85, ('Jamaica')),
        (COUNTRY_86, ('Japan')),
        (COUNTRY_87, ('Jordan')),
        (COUNTRY_88, ('Kazakhstan')),
        (COUNTRY_89, ('Kenya')),
        (COUNTRY_90, ('Kiribati')),
        (COUNTRY_91, ('Kuwait')),
        (COUNTRY_92, ('Kyrgyzstan')),
        (COUNTRY_93, ('Laos')),
        (COUNTRY_94, ('Latvia')),
        (COUNTRY_95, ('Lebanon')),
        (COUNTRY_96, ('Lesotho')),
        (COUNTRY_97, ('Liberia')),
        (COUNTRY_98, ('Libya')),
        (COUNTRY_99, ('Liechtenstein')),
        (COUNTRY_100, ('Lithuania')),
        (COUNTRY_101, ('Luxembourg')),
        (COUNTRY_102, ('Madagascar')),
        (COUNTRY_103, ('Malawi')),
        (COUNTRY_104, ('Malaysia')),
        (COUNTRY_105, ('Maldives')),
        (COUNTRY_106, ('Mali')),
        (COUNTRY_107, ('Malta')),
        (COUNTRY_108, ('Marshall Islands')),
        (COUNTRY_109, ('Mauritania')),
        (COUNTRY_110, ('Mauritius')),
        (COUNTRY_111, ('Mexico')),
        (COUNTRY_112, ('Micronesia')),
        (COUNTRY_113, ('Moldova')),
        (COUNTRY_114, ('Monaco')),
        (COUNTRY_115, ('Mongolia')),
        (COUNTRY_116, ('Montenegro')),
        (COUNTRY_117, ('Morocco')),
        (COUNTRY_118, ('Mozambique')),
        (COUNTRY_119, ('Myanmar (formerly Burma)')),
        (COUNTRY_120, ('Namibia')),
        (COUNTRY_121, ('Nauru')),
        (COUNTRY_122, ('Nepal')),
        (COUNTRY_123, ('Netherlands')),
        (COUNTRY_124, ('New Zealand')),
        (COUNTRY_125, ('Nicaragua')),
        (COUNTRY_126, ('Niger')),
        (COUNTRY_127, ('Nigeria')),
        (COUNTRY_128, ('North Korea')),
        (COUNTRY_129, ('North Macedonia')),
        (COUNTRY_130, ('Norway')),
        (COUNTRY_131, ('Oman')),
        (COUNTRY_132, ('Pakistan')),
        (COUNTRY_133, ('Palau')),
        (COUNTRY_134, ('Palestine State')),
        (COUNTRY_135, ('Panama')),
        (COUNTRY_136, ('Papua New Guinea')),
        (COUNTRY_137, ('Paraguay')),
        (COUNTRY_138, ('Peru')),
        (COUNTRY_139, ('Philippines')),
        (COUNTRY_140, ('Poland')),
        (COUNTRY_141, ('Portugal')),
        (COUNTRY_142, ('Qatar')),
        (COUNTRY_143, ('Romania')),
        (COUNTRY_144, ('Russia')),
        (COUNTRY_145, ('Rwanda')),
        (COUNTRY_146, ('Saint Kitts and Nevis')),
        (COUNTRY_147, ('Saint Lucia')),
        (COUNTRY_148, ('Saint Vincent and the Grenadines')),
        (COUNTRY_149, ('Samoa')),
        (COUNTRY_150, ('San Marino')),
        (COUNTRY_151, ('Sao Tome and Principe')),
        (COUNTRY_152, ('Saudi Arabia')),
        (COUNTRY_153, ('Senegal')),
        (COUNTRY_154, ('Serbia')),
        (COUNTRY_155, ('Seychelles')),
        (COUNTRY_156, ('Sierra Leone')),
        (COUNTRY_157, ('Singapore')),
        (COUNTRY_158, ('Slovakia')),
        (COUNTRY_159, ('Slovenia')),
        (COUNTRY_160, ('Solomon Islands')),
        (COUNTRY_161, ('Somalia')),
        (COUNTRY_162, ('South Africa')),
        (COUNTRY_163, ('South Korea')),
        (COUNTRY_164, ('South Sudan')),
        (COUNTRY_165, ('Spain')),
        (COUNTRY_166, ('Sri Lanka')),
        (COUNTRY_167, ('Sudan')),
        (COUNTRY_168, ('Suriname')),
        (COUNTRY_169, ('Sweden')),
        (COUNTRY_170, ('Switzerland')),
        (COUNTRY_171, ('Syria')),
        (COUNTRY_172, ('Tajikistan')),
        (COUNTRY_173, ('Tanzania')),
        (COUNTRY_174, ('Thailand')),
        (COUNTRY_175, ('Timor-Leste')),
        (COUNTRY_176, ('Togo')),
        (COUNTRY_177, ('Tonga')),
        (COUNTRY_178, ('Trinidad and Tobago')),
        (COUNTRY_179, ('Tunisia')),
        (COUNTRY_180, ('Turkey')),
        (COUNTRY_181, ('Turkmenistan')),
        (COUNTRY_182, ('Tuvalu')),
        (COUNTRY_183, ('Uganda')),
        (COUNTRY_184, ('Ukraine')),
        (COUNTRY_185, ('United Arab Emirates')),
        (COUNTRY_186, ('United Kingdom')),
        (COUNTRY_187, ('United States of America')),
        (COUNTRY_188, ('Uruguay')),
        (COUNTRY_189, ('Uzbekistan')),
        (COUNTRY_190, ('Vanuatu')),
        (COUNTRY_191, ('Venezuela')),
        (COUNTRY_192, ('Vietnam')),
        (COUNTRY_193, ('Yemen')),
        (COUNTRY_194, ('Zambia')),
        (COUNTRY_195, ('Zimbabwe')),

    ]

    STATE_AN = 1
    STATE_AP = 2
    STATE_ARP = 3
    STATE_ASM = 4
    STATE_BH = 5
    STATE_CH = 6
    STATE_CHH = 7
    STATE_DD = 8
    STATE_GH = 9
    STATE_GJ = 10
    STATE_HR = 11
    STATE_HP = 12
    STATE_JK = 13
    STATE_JN = 14
    STATE_KA = 15
    STATE_KL = 16
    STATE_LK = 17
    STATE_LD = 18
    STATE_MP = 19
    STATE_MH = 20
    STATE_MN = 21
    STATE_MG = 22
    STATE_MZ = 23
    STATE_NG = 24
    STATE_ND = 25
    STATE_OD = 26
    STATE_PD = 27
    STATE_PJ = 28
    STATE_RJ = 29
    STATE_SK = 30
    STATE_TN = 31
    STATE_TS = 32
    STATE_TR = 33
    STATE_UP = 34
    STATE_UK = 35
    STATE_WB = 36
    STATE_CHOICES = [
        (STATE_AN, ('(UT6) Andaman and Nicobar Islands')),
        (STATE_AP, ('(S10) Andhra Pradesh')),
        (STATE_ARP, ('(S26) Arunachal Pradesh')),
        (STATE_ASM, ('(S15) Assam')),
        (STATE_BH, ('(S3) Bihar')),
        (STATE_CH, ('(UT4) Chandigarh')),
        (STATE_CHH, ('(S17) Chhattisgarh')),
        (STATE_DD, ('(UT5) Dadra and Nagar Haveli and Daman and Diu')),
        (STATE_GH, ('(S25) Goa')),
        (STATE_GJ, ('(S9) Gujarat')),
        (STATE_HR, ('(S18) Haryana')),
        (STATE_HP, ('(S20) Himachal Pradesh')),
        (STATE_JK, ('(UT2) Jammu and Kashmir')),
        (STATE_JN, ('(S14) Jharkhand')),
        (STATE_KA, ('(S8) Karnataka')),
        (STATE_KL, ('(S13) Kerala')),
        (STATE_LK, ('(UT7) Ladakh')),
        (STATE_LD, ('(UT8) Lakshadweep')),
        (STATE_MP, ('(UT8) Madhya Pradesh')),
        (STATE_MH, ('(S2) Maharashtra')),
        (STATE_MN, ('(S23) Manipur')),
        (STATE_MG, ('(S22) Meghalaya')),
        (STATE_MZ, ('(S22) Mizoram')),
        (STATE_NG, ('(S24) Nagaland')),
        (STATE_ND, ('(UT1) New Delhi')),
        (STATE_OD, ('(S11) Odisha')),
        (STATE_PD, ('(UT3) Puducherry')),
        (STATE_PJ, ('(S16) Punjab')),
        (STATE_RJ, ('(S7) Rajasthan')),
        (STATE_SK, ('(S28) Sikkim')),
        (STATE_TN, ('(S6) Tamil Nadu')),
        (STATE_TS, ('(S12) Telangana')),
        (STATE_TR, ('(S21) Tripura')),
        (STATE_UP, ('(S1) Uttar Pradesh')),
        (STATE_UK, ('(S) Uttarakhand')),
        (STATE_WB, ('(S4) West Bengal')),                  
    ]
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="customers/profiles/avatars/", default="customers/profiles/avatars/default-profile-picture.png")
    birthday = models.DateField(null=True, blank=True)
    gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICES, null=True, blank=True)
    education = models.PositiveSmallIntegerField(choices=EDU_CHOICES, null=True, blank=True)
    phone = models.CharField(max_length=32, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    number = models.CharField(max_length=32, null=True, blank=True)
    city = models.CharField(max_length=60, null=True, blank=True)
    state = models.PositiveBigIntegerField(choices=STATE_CHOICES, null=True, blank=True)
    country = models.PositiveBigIntegerField(choices=COUNTRY_CHOICES, null=True, blank=True)
    zip = models.CharField(max_length=30, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ('Profile')
        verbose_name_plural = ('Profiles')

    @property
    def get_avatar(self):
        return self.avatar.url if self.avatar else static('assets/img/team/default-profile-picture.png')
    
    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name
from enum import Enum


class Naics(Enum):
    AccommodationAndFoodServices = 'Accommodation and Food Services'
    AdministrativeAndSupportAndWasteManagementAndRemediationServices = 'Administrative and Support and Waste Management and Remediation Services'
    AgricultureForestryFishingAndHunting = 'Agriculture, Forestry, Fishing and Hunting'
    ArtsEntertainmentAndRecreation = 'Arts, Entertainment and Recreation'
    Construction = 'Construction'
    EducationalServices = 'Educational Services'
    FinanceAndInsurance = 'Finance and Insurance'
    HealthCareAndSocialAssistance = 'Health Care and Social Assistance'
    Information = 'Information'
    ManagementOfCompaniesAndEnterprises = 'Management of Companies and Enterprises'
    Manufacturing = 'Manufacturing'
    MiningQuarryingAndOilAndGasExtraction = 'Mining, Quarrying, and Oil and Gas Extraction'
    OtherServicesExceptPublicAdministration = 'Other Services (except Public Administration)'
    ProfessionalScientificAndTechnicalServices = 'Professional, Scientific, and Technical Services'
    PublicAdministration = 'Public Administration'
    RealEstateAndRentalAndLeasing = 'Real Estate and Rental and Leasing'
    RetailTrade = 'Retail Trade'
    TransportationAndWarehousing = 'Transportation and Warehousing'
    Utilities = 'Utilities'
    WholesaleTrade = 'Wholesale Trade'
    Missing = "I don't know"

    @classmethod
    def choices(cls):
        # Create a list of tuples in the format Django expects for choices: (value, label)
        return [(member.value, name) for name, member in cls.__members__.items()]


class RevLineCr(Enum):
    Y = 'Yes'
    N = 'No'
    Unknown = "I don't know"

    @classmethod
    def choices(cls):
        # Create a list of tuples in the format Django expects for choices: (value, label)
        return [(member.value, name) for name, member in cls.__members__.items()]


class UrbanRural(Enum):
    R = 'Rural'
    U = 'Urban'
    M = "I don't know"

    @classmethod
    def choices(cls):
        # Create a list of tuples in the format Django expects for choices: (value, label)
        return [(member.value, name) for name, member in cls.__members__.items()]


class USState(Enum):
    AK = 'Alaska'
    AL = 'Alabama'
    AR = 'Arkansas'
    AZ = 'Arizona'
    CA = 'California'
    CO = 'Colorado'
    CT = 'Connecticut'
    DC = 'District of Columbia'
    DE = 'Delaware'
    FL = 'Florida'
    GA = 'Georgia'
    GU = 'Guam'
    HI = 'Hawaii'
    IA = 'Iowa'
    ID = 'Idaho'
    IL = 'Illinois'
    IN = 'Indiana'
    KS = 'Kansas'
    KY = 'Kentucky'
    LA = 'Louisiana'
    MA = 'Massachusetts'
    MD = 'Maryland'
    ME = 'Maine'
    MI = 'Michigan'
    MN = 'Minnesota'
    MO = 'Missouri'
    MS = 'Mississippi'
    MT = 'Montana'
    NC = 'North Carolina'
    ND = 'North Dakota'
    NE = 'Nebraska'
    NH = 'New Hampshire'
    NJ = 'New Jersey'
    NM = 'New Mexico'
    NV = 'Nevada'
    NY = 'New York'
    OH = 'Ohio'
    OK = 'Oklahoma'
    OR = 'Oregon'
    PA = 'Pennsylvania'
    PR = 'Puerto Rico'
    RI = 'Rhode Island'
    SC = 'South Carolina'
    SD = 'South Dakota'
    TN = 'Tennessee'
    TX = 'Texas'
    UT = 'Utah'
    VA = 'Virginia'
    VI = 'Virgin Islands'
    VT = 'Vermont'
    WA = 'Washington'
    WI = 'Wisconsin'
    WV = 'West Virginia'
    WY = 'Wyoming'

    @classmethod
    def choices(cls):
        # Create a list of tuples in the format Django expects for choices: (value, label)
        return [(member.value, name) for name, member in cls.__members__.items()]
    

class YesNo(Enum):
    Y = 'Yes'
    N = 'No'

    @classmethod
    def choices(cls):
        # Create a list of tuples in the format Django expects for choices: (value, label)
        return [(member.value, name) for name, member in cls.__members__.items()]

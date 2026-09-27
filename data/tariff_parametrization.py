from locators.taxi_order_form_locators import TaxiOrderFormLocators
from data.tariffs_descriptions import TariffsDescriptions
import pytest

PARAMETRIZATION_LIST_FOR_INFO_POPUP = [
    [
        TaxiOrderFormLocators.WORKING_TARIFF_LOCATOR,
        TaxiOrderFormLocators.WORKING_TARIFF_INFO_ICON_LOCATOR,
        TaxiOrderFormLocators.WORKING_TARIFF_POPUP_LOCATOR,
        TaxiOrderFormLocators.WORKING_TARIFF_POPUP_TITLE_LOCATOR,
        TaxiOrderFormLocators.WORKING_TARIFF_POPUP_SUBTITLE_LOCATOR,
        TariffsDescriptions.WORKING_TARIFF_TITLE_TEXT,
        TariffsDescriptions.WORKING_TARIFF_SUBTITLE_TEXT
    ],
    [
        TaxiOrderFormLocators.VACATION_TARIFF_LOCATOR,
        TaxiOrderFormLocators.VACATION_TARIFF_INFO_ICON_LOCATOR,
        TaxiOrderFormLocators.VACATION_TARIFF_POPUP_LOCATOR,
        TaxiOrderFormLocators.VACATION_TARIFF_POPUP_TITLE_LOCATOR,
        TaxiOrderFormLocators.VACATION_TARIFF_POPUP_SUBTITLE_LOCATOR,
        TariffsDescriptions.VACATION_TARIFF_TITLE_TEXT,
        TariffsDescriptions.VACATION_TARIFF_SUBTITLE_TEXT
    ],
    [
        TaxiOrderFormLocators.COMFORTING_TARIFF_LOCATOR,
        TaxiOrderFormLocators.COMFORTING_TARIFF_INFO_ICON_LOCATOR,
        TaxiOrderFormLocators.COMFORTING_TARIFF_POPUP_LOCATOR,
        TaxiOrderFormLocators.COMFORTING_TARIFF_POPUP_TITLE_LOCATOR,
        TaxiOrderFormLocators.COMFORTING_TARIFF_POPUP_SUBTITLE_LOCATOR,
        TariffsDescriptions.COMFORTING_TARIFF_TITLE_TEXT,
        TariffsDescriptions.COMFORTING_TARIFF_SUBTITLE_TEXT
    ],
    [
        TaxiOrderFormLocators.CHIC_TARIFF_LOCATOR,
        TaxiOrderFormLocators.CHIC_TARIFF_INFO_ICON_LOCATOR,
        TaxiOrderFormLocators.CHIC_TARIFF_POPUP_LOCATOR,
        TaxiOrderFormLocators.CHIC_TARIFF_POPUP_TITLE_LOCATOR,
        TaxiOrderFormLocators.CHIC_TARIFF_POPUP_SUBTITLE_LOCATOR,
        TariffsDescriptions.CHIC_TARIFF_TITLE_TEXT,
        TariffsDescriptions.CHIC_TARIFF_SUBTITLE_TEXT
    ],
    pytest.param(
TaxiOrderFormLocators.SLEEPY_TARIFF_LOCATOR,
        TaxiOrderFormLocators.SLEEPY_TARIFF_INFO_ICON_LOCATOR,
        TaxiOrderFormLocators.SLEEPY_TARIFF_POPUP_LOCATOR,
        TaxiOrderFormLocators.SLEEPY_TARIFF_POPUP_TITLE_LOCATOR,
        TaxiOrderFormLocators.SLEEPY_TARIFF_POPUP_SUBTITLE_LOCATOR,
        TariffsDescriptions.SLEEPY_TARIFF_TITLE_TEXT,
        TariffsDescriptions.SLEEPY_TARIFF_SUBTITLE_TEXT,
        marks=pytest.mark.xfail(reason="expected from the task description")
    ),
    pytest.param(
TaxiOrderFormLocators.TALKING_TARIFF_LOCATOR,
        TaxiOrderFormLocators.TALKING_TARIFF_INFO_ICON_LOCATOR,
        TaxiOrderFormLocators.TALKING_TARIFF_POPUP_LOCATOR,
        TaxiOrderFormLocators.TALKING_TARIFF_POPUP_TITLE_LOCATOR,
        TaxiOrderFormLocators.TALKING_TARIFF_POPUP_SUBTITLE_LOCATOR,
        TariffsDescriptions.TALKING_TARIFF_TITLE_TEXT,
        TariffsDescriptions.TALKING_TARIFF_SUBTITLE_TEXT,
        marks=pytest.mark.xfail(reason="expected from the task description")
    )
]

PARAMETRIZATION_FOR_USER_INFO = [
    TaxiOrderFormLocators.WORKING_TARIFF_LOCATOR,
    TaxiOrderFormLocators.VACATION_TARIFF_LOCATOR,
    TaxiOrderFormLocators.COMFORTING_TARIFF_LOCATOR,
    TaxiOrderFormLocators.CHIC_TARIFF_LOCATOR,
    TaxiOrderFormLocators.SLEEPY_TARIFF_LOCATOR,
    TaxiOrderFormLocators.TALKING_TARIFF_LOCATOR
]

PARAMETRIZATION_IDS = ['Working Tariff', 'Vacation Tariff', 'Comforting Tariff', 'Chic Tariff', 'Sleepy Tariff', 'Talking Tariff']

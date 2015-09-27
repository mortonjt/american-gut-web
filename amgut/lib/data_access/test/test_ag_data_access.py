from unittest import TestCase, main
from random import choice, randint
from string import ascii_letters
from uuid import UUID
import datetime

from amgut.lib.data_access.ag_data_access import AGDataAccess


class TestAGDataAccess(TestCase):
    def setUp(self):
        self.ag_data = AGDataAccess()

    def tearDown(self):
        del self.ag_data

    def test___init__(self):
        raise NotImplementedError()

    def test___del__(self):
        raise NotImplementedError()

    def test_get_cursor(self):
        raise NotImplementedError()

    def test__open_connection(self):
        raise NotImplementedError()

    def test__get_col_names_from_cursor(self):
        raise NotImplementedError()

    def test_authenticateWebAppUser(self):
        raise NotImplementedError()

    def test_addAGLogin(self):
        # test new user
        exists = 'EXISTS'
        while exists is not None:
            email = ''.join([choice(ascii_letters)
                             for i in range(randint(5, 10))])
            domain = ''.join([choice(ascii_letters)
                             for i in range(randint(5, 10))])
            new_email = '@'.join([email, domain]) + '.com'
            exists = self.ag_data.check_login_exists(new_email)

        # make sure the ag_login_id is a UUID4 string
        ag_login_id = self.ag_data.addAGLogin(
            new_email, 'TESTDUDE', '123 fake test street', 'testcity',
            'teststate', '1L2 2G3', 'United Kingdom')
        as_uuid = UUID(ag_login_id)
        self.assertTrue(as_uuid.version, 4)

        # test existing user
        ag_login_id = self.ag_data.addAGLogin(
            'TEST@EMAIL.com', 'TESTOTHER', '123 fake test street', 'testcity',
            'teststate', '1L2 2G3', 'United Kingdom')

        obs = self.ag_data.addAGLogin(
            'test@EMAIL.com', 'TESTDUDE', '123 fake test street', 'testcity',
            'teststate', '1L2 2G3', 'United Kingdom')
        self.assertEqual(ag_login_id, obs)


    def test_getAGBarcodeDetails(self):
        # test non-existant barcode
        obs = self.ag_data.getAGBarcodeDetails('99')
        self.assertEqual(obs, {})

        # test existing barcode but not in AG
        obs = self.ag_data.getAGBarcodeDetails('000006232')
        self.assertEqual(obs, {})

        # test existing AG barcode
        obs = self.ag_data.getAGBarcodeDetails('000001047')
        exp = {
            'barcode': '000001047',
            'status': 'Received',
            'ag_kit_id': 'd8592c74-7e35-2135-e040-8a80115d6401',
            'name': 'REMOVED',
            'participant_name': 'REMOVED',
            'email': 'REMOVED',
            'site_sampled': 'Stool',
            'environment_sampled': None,
            'sample_date': datetime.date(2013, 3, 28),
            'sample_time': datetime.time(23, 25),
            'notes': 'REMOVED',
            'overloaded': None,
            'withdrawn': None,
            'other': None,
            'moldy': None,
            'refunded': None,
            'ag_kit_barcode_id': 'd8592c74-7e36-2135-e040-8a80115d6401',
            'date_of_last_email': None,
            'other_text': 'REMOVED'
        }
        self.assertEqual(obs, exp)


    def test_getAGKitDetails(self):
        # test non-existant kit
        obs = self.ag_data.getAGKitDetails('IDONTEXI5T')
        self.assertEqual(obs, {})

        # test existing AG kit
        obs = self.ag_data.getAGKitDetails('tst_OQjBX')
        exp = {
            'ag_kit_id': 'd9f2572b-35eb-6b88-e040-8a80115d4a01',
            'supplied_kit_id': 'tst_OQjBX',
            'swabs_per_kit': 1,
            'verification_email_sent': 'n',
            'kit_verification_code': '36714',
            'kit_password': '$2a$12$3yUJTUuTfCMkgVVev8xik.33wruO9SDAwuVDUZBq3c'
                            'VVMuJbK9cai',
            'kit_verified': 'y'}

    def test_registerHandoutKit(self):
        raise NotImplementedError()

    def test_deleteAGParticipantSurvey(self):
        raise NotImplementedError()

    def test_getConsent(self):
        raise NotImplementedError()

    def test_logParticipantSample(self):
        raise NotImplementedError()

    def test_deleteSample(self):
        raise NotImplementedError()

    def test_getHumanParticipants(self):
        raise NotImplementedError()

    def test_is_old_survey(self):
        raise NotImplementedError()

    def test_updateVioscreenStatus(self):
        raise NotImplementedError()

    def test_getAnimalParticipants(self):
        raise NotImplementedError()

    def test_getParticipantSamples(self):
        raise NotImplementedError()

    def test_getEnvironmentalSamples(self):
        raise NotImplementedError()

    def test_getAvailableBarcodes(self):
        raise NotImplementedError()

    def test_verifyKit(self):
        raise NotImplementedError()

    def test_getMapMarkers(self):
        raise NotImplementedError()

    def test_handoutCheck(self):
        raise NotImplementedError()

    def test_check_access(self):
        raise NotImplementedError()

    def test_getAGKitIDsByEmail(self):
        raise NotImplementedError()

    def test_ag_set_pass_change_code(self):
        raise NotImplementedError()

    def test_ag_update_kit_password(self):
        raise NotImplementedError()

    def test_ag_verify_kit_password_change_code(self):
        raise NotImplementedError()

    def test_getBarcodesByKit(self):
        raise NotImplementedError()

    def test_checkPrintResults(self):
        raise NotImplementedError()

    def test_get_user_for_kit(self):
        raise NotImplementedError()

    def test_get_menu_items(self):
        raise NotImplementedError()

    def test_check_if_consent_exists(self):
        raise NotImplementedError()

    def test_get_user_info(self):
        raise NotImplementedError()

    def test_get_person_info(self):
        raise NotImplementedError()

    def test_get_barcode_results(self):
        raise NotImplementedError()

    def test_get_login_info(self):
        raise NotImplementedError()

    def test_get_survey_id(self):
        raise NotImplementedError()

    def test_get_countries(self):
        raise NotImplementedError()


if __name__ == "__main__":
    main()

from django.test import TestCase

from analysis.models import Player, Staff, TechnicalRecord

class PlayerDetailTestCase(TestCase):
    def setUp(self):
        self.player = Player.objects.create(name="test_player", dob="1395-03-03", right_hand=True)
        self.staff = Staff.objects.create(name="test_staff")
        self.technical_record = TechnicalRecord.objects.create(player_id=self.player.id, staff_id=self.staff.id,movement=22,listening=34)

    def test_list_of_plyaer_records_success(self):
        player = Player.objects.get(uuid=self.player.uuid)
        technical_record = TechnicalRecord.objects.get(player__uuid=self.player.uuid)
        assert player.id == self.player.id
        assert technical_record.id == self.technical_record.id

        self.assertEqual(player.name , self.player.name)
        self.assertEqual(technical_record.staff.name, self.staff.name)

        assert technical_record.movement == self.technical_record.movement #22
        assert technical_record.listening == self.technical_record.listening #34
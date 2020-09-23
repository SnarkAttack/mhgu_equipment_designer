from equipment_designer.equipment import EquipmentDatabase

TEST_DB_NAME = "./databases/equipment_test.db"

equipment_db = EquipmentDatabase(TEST_DB_NAME)

def test_armor():
    assert equipment_db.get_armor_count() == 10
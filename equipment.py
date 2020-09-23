import os
import sqlite3


EQUIPMENT_DATABASE_NAME = "./databases/equipment_test.db"

class EquipmentDatabase():

    def __init__(self, db_path):
        self.db_path = db_path

    def populate_skills(self):
        skills = [
            ('Psychic',),
            ('Speed Setup',),
            ('Ranger',),
            ('KO',),
            ('Maestro',),
            ('Status',),
            ('Botany',),
            ('Stam Drain',),
            ('Expert',),
            ('Attack',),
            ('Fire Atk',),
            ('Defense',),
            ('Vault',),
            ('Stun',),
            ('Paralysis',),
            ('Water Atk',),
            ('Ice Atk',),
            ('Bind Res',),
            ('Sleep',),
            ('Poison',),
            ('Thunder Atk',),
            ('Elemental',),
            ('Sheathing',),
            ('Dragon Atk',),
            ('Dragon Res',),
            ('Guard',),
            ('Constitution',),
            ('Artillery',),
            ('Potential',),
            ('Protection',),
            ('Honey',),
            ('Heat Res',),
            ('Cold Res',),
        ]

        conn = sqlite3.connect(EQUIPMENT_DATABASE_NAME)
        c = conn.cursor()

        c.executemany("""INSERT INTO skills (name) VALUES (?)""", skills)

        conn.commit()

    def populate_skill_thresholds(self):
        conn = sqlite3.connect(EQUIPMENT_DATABASE_NAME)
        c = conn.cursor()

        skill_thresholds = [
            ('Autotracker', self.get_skill_id_from_name('Psychic'), 15, ''),
            ('Detect', self.get_skill_id_from_name('Psychic'), 10, ''),
            ('Trap Master', self.get_skill_id_from_name('Speed Setup'), 10, ''),
            ('Outdoorsman', self.get_skill_id_from_name('Ranger'), 10, ''),
        ]

        c.executemany("""INSERT INTO skill_thresholds (name, skill_id, threshold, description)
                    VALUES (?,?,?,?)""", skill_thresholds)

        conn.commit()

    def populate_armor_table(self):
        armors = [
            ('Hunting Helm', 1, 1, 1, 0, 1, 2, 50, 1, 0, 0, 0, 0, 1),
            ('Hunting Mail', 1, 1, 1, 0, 2, 2, 50, 1, 0, 0, 0, 0, 0),
            ('Hunting Braces', 1, 1, 1, 0, 3, 2, 50, 1, 0, 0, 0, 0, 0),
            ('Hunting Faulds', 1, 1, 1, 0, 4, 2, 50, 1, 0, 0, 0, 0, 1),
            ('Hunting Greaves', 1, 1, 1, 0, 5, 2, 50, 1, 0, 0, 0, 0, 2),
            ('Hunter\'s Helm', 1, 1, 1, 0, 1, 6, 54, 0, 0, 0, 0, 0, 0),
            ('Hunter\'s Mail', 1, 1, 1, 0, 2, 6, 54, 0, 0, 0, 0, 0, 1),
            ('Hunter\'s Vambraces', 1, 1, 1, 0, 3, 6, 54, 0, 0, 0, 0, 0, 1),
            ('Hunter\'s Faulds', 1, 1, 1, 0, 4, 6, 54, 0, 0, 0, 0, 0, 1),
            ('Hunter\'s Greaves', 1, 1, 1, 0, 5, 6, 54, 0, 0, 0, 0, 0, 2),
        ]

        conn = sqlite3.connect(EQUIPMENT_DATABASE_NAME)
        c = conn.cursor()

        c.executemany("""INSERT INTO armor (name, male, female, blademaster, gunner, body_part,
                    min_defense, max_defense, fire, water, thunder, ice, dragon, slot_count)
                    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", armors)

        conn.commit()

    def populate_armor_skills_table(self):
        conn = sqlite3.connect(EQUIPMENT_DATABASE_NAME)
        c = conn.cursor()

        armor_skills = [
            (self.get_armor_id_from_name('Hunting Helm'), self.get_skill_id_from_name('Psychic'), 3),
            (self.get_armor_id_from_name('Hunting Mail'), self.get_skill_id_from_name('Psychic'), 2),
            (self.get_armor_id_from_name('Hunting Braces'), self.get_skill_id_from_name('Psychic'), 5),
            (self.get_armor_id_from_name('Hunting Faulds'), self.get_skill_id_from_name('Speed Setup'), 3),
            (self.get_armor_id_from_name('Hunting Greaves'), self.get_skill_id_from_name('Speed Setup'), 3),
            (self.get_armor_id_from_name('Hunter\'s Helm'), self.get_skill_id_from_name('Speed Setup'), 2),
            (self.get_armor_id_from_name('Hunter\'s Helm'), self.get_skill_id_from_name('Ranger'), 3),
            (self.get_armor_id_from_name('Hunter\'s Mail'), self.get_skill_id_from_name('Speed Setup'), 3),
            (self.get_armor_id_from_name('Hunter\'s Vambraces'), self.get_skill_id_from_name('Speed Setup'), 3),
            (self.get_armor_id_from_name('Hunter\'s Faulds'), self.get_skill_id_from_name('Ranger'), 6),
            (self.get_armor_id_from_name('Hunter\'s Greaves'), self.get_skill_id_from_name('Ranger'), 1),
        ]

        c.executemany("""INSERT INTO armor_skills (armor_id, skill_id, skill_value)
                    VALUES (?,?,?)""", armor_skills)

        conn.commit()

    def populate_decorations_table(self):
        conn = sqlite3.connect(EQUIPMENT_DATABASE_NAME)
        c = conn.cursor()

        decorations = [
            ('Psychic Jwl 1', 1),
            ('Trapmaster Jwl 1', 1),
            ('Ranger Jwl 1', 1),
        ]

        c.executemany("""INSERT INTO decorations (name, slots_needed) VALUES (?,?)""", decorations)

        conn.commit()

    def populate_decoration_skills_table(self):
        conn = sqlite3.connect(EQUIPMENT_DATABASE_NAME)
        c = conn.cursor()

        decoration_skills = [
            (self.get_decoration_id_from_name('Psychic Jwl 1'), self.get_skill_id_from_name('Psychic'), 2),
            (self.get_decoration_id_from_name('Trapmaster Jwl 1'), self.get_skill_id_from_name('Speed Setup'), 2),
            (self.get_decoration_id_from_name('Ranger Jwl 1'), self.get_skill_id_from_name('Ranger'), 2),
        ]

        c.executemany("""INSERT INTO decoration_skills (decoration_id, skill_id, skill_value)
                    VALUES (?,?,?)""", decoration_skills)

        conn.commit()

    def get_armor_id_from_name(self, name):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()

        return c.execute("SELECT id from armor WHERE name = (?)", (name,)).fetchone()[0]

    def get_skill_id_from_name(self, name):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()

        return c.execute("SELECT id from skills WHERE name = (?)", (name,)).fetchone()[0]

    def get_decoration_id_from_name(self, name):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        return c.execute("SELECT id from decorations WHERE name = (?)", (name,)).fetchone()[0]

    def table_exists(self, table_name):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        return c.execute(f"SELECT count(*) from {table_name}""").fetchone()[0] > 0

    def get_armor_count(self):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        return c.execute("SELECT count(*) from armor").fetchone()[0]

    def create_database(self):
        try:
            conn = sqlite3.connect(self.db_path)
            c = conn.cursor()

            # Skill stored in separate table, linked by item id
            c.execute("""CREATE TABLE IF NOT EXISTS armor
                    (id integer PRIMARY KEY, name text UNIQUE, male BOOLEAN,
                    female BOOLEAN, blademaster BOOLEAN, gunner BOOLEAN,
                    body_part integer, min_defense integer, max_defense integer,
                    fire integer, water integer, thunder integer, ice integer,
                    dragon integer, slot_count integer)""")

            c.execute("""CREATE TABLE IF NOT EXISTS skills
                    (id integer PRIMARY KEY, name text UNIQUE)""")

            c.execute("""CREATE TABLE IF NOT EXISTS skill_thresholds
                    (id integer PRIMARY KEY, name text UNIQUE, skill_id integer,
                    threshold integer, description text)""")

            c.execute("""CREATE TABLE IF NOT EXISTS armor_skills
                    (id integer PRIMARY KEY, armor_id integer, skill_id integer,
                    skill_value integer)""")

            c.execute("""CREATE TABLE IF NOT EXISTS decorations
                        (id integer PRIMARY KEY, name text, slots_needed integer)""")

            c.execute("""CREATE TABLE IF NOT EXISTS decoration_skills
                        (id integer PRIMARY KEY, decoration_id integer, skill_id integer,
                        skill_value integer)""")

            conn.commit()

            return True
        except sqlite3.Error as e:
            print(e)
            return False

    def maximize_skill(self, skill_id):

        conn = sqlite3.connect(EQUIPMENT_DATABASE_NAME)
        c = conn.cursor()

        head = c.execute("""SELECT armor.id, armor.name, min_defense, max_defense,
                        fire, water, thunder, ice, dragon, slot_count, skill_id, skill_value
                        FROM armor_skills INNER JOIN armor ON armor_skills.armor_id = armor.id WHERE body_part = 1""").fetchall()

if __name__ == "__main__":
    equipment_db = EquipmentDatabase(EQUIPMENT_DATABASE_NAME)
    if equipment_db.create_database():
        if not equipment_db.table_exists('skills'):
            print("Making skills table")
            equipment_db.populate_skills()
        if not equipment_db.table_exists('skill_thresholds'):
            print("Making skill thresholds table")
            equipment_db.populate_skill_thresholds()
        if not equipment_db.table_exists('armor'):
            print("Making armor table")
            equipment_db.populate_armor_table()
        if not equipment_db.table_exists('armor_skills'):
            print("Making armor skills table")
            equipment_db.populate_armor_skills_table()
        if not equipment_db.table_exists('decorations'):
            print("Making decorations table")
            equipment_db.populate_decorations_table()
        if not equipment_db.table_exists('decoration_skills'):
            print("Making decoration skills table")
            equipment_db.populate_decoration_skills_table()


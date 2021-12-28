import itertools

class Goalkeeper(object):

    newid = itertools.count()
    def __init__(self, goalkeeper_info):
        self.new_id = next(Goalkeeper.newid) + 1
        self.goalkeeper_url = goalkeeper_info["player_url"]
        self.short_name = goalkeeper_info["short_name"]
        self.long_name = goalkeeper_info["long_name"]
        self.overall = goalkeeper_info["overall"]
        self.potential = goalkeeper_info["potential"]
        self.value_eur = goalkeeper_info["value_eur"]
        self.wage_eur = goalkeeper_info["wage_eur"]
        self.age = goalkeeper_info["age"]
        self.dob = goalkeeper_info["dob"]
        self.height_cm = goalkeeper_info["height_cm"]
        self.weight_kg = goalkeeper_info["weight_kg"]
        self.club_name = goalkeeper_info["club_name"]
        self.club_position = goalkeeper_info["club_position"]
        self.club_joined = goalkeeper_info["club_joined"]
        self.nationality_name = goalkeeper_info["nationality_name"]
        self.preferred_foot = goalkeeper_info["preferred_foot"]
        self.skill_moves = goalkeeper_info["skill_moves"]
        self.goalkeeping_diving = goalkeeper_info["goalkeeping_diving"]
        self.goalkeeping_handling = goalkeeper_info["goalkeeping_handling"]
        self.goalkeeping_kicking = goalkeeper_info["goalkeeping_kicking"]
        self.goalkeeping_positioning = goalkeeper_info["goalkeeping_positioning"]
        self.goalkeeping_reflexes = goalkeeper_info["goalkeeping_reflexes"]
        self.player_face_url = goalkeeper_info["player_face_url"]
        self.club_logo_url = goalkeeper_info["club_logo_url"]
        self.club_flag_url = goalkeeper_info["club_flag_url"]
        self.nation_flag_url = goalkeeper_info["nation_flag_url"]

    def __repr__(self):
        r = dict(self.__dict__)
        del r["new_id"]
        return "Goalkeeper " + str(self.new_id) + " : " + str(r)
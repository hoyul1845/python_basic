# 마린 : 공격 유닛, 군인. 총을 쏠 수 있음
#name = "마린" # 유닛의 이름
#hp = 40 # 유닛의 체력
#damage = 5  # 유닛의 공격력

#print("{0} 유닛이 생성되었습니다.".format(name))
#print("체력은 {0}, 공격력 {1}\n".format(hp, damage))

# 탱크 : 공격 유닛, 탱크. 포를 쏠 수 있는데, 일반 모드 / 시즈모드.
#tank_name = "탱크"
#tank_hp = 150
#tank_damage = 35

#print("{0} 유닛이 생성되었습니다.".format(tank_name))
#print("체력은 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

#tank2_name = "탱크"
#tank2_hp = 150
#tank2_damage = 35

#print("{0} 유닛이 생성되었습니다.".format(tank2_name))
#print("체력은 {0}, 공격력 {1}\n".format(tank2_hp, tank2_damage))

#def attack(name, location, damage):
  #  print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format( \
 #       name, location, damage))
    
#attack(name, "1시", damage)
#attack(tank_name, "1시", tank_damage)

# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name, location, self.speed))
# 공격 유닛        
class AttackUnit(Unit):
    def __init__(self, name, hp, damage, speed):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.speed = speed
        
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage))
        
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))
# 드랍쉽 : 공중 유닛, 수송기. 마린/파이어뱃/탱크 등을 수송. 공격 x

# 날 수 있는 기능을 가진 클래스
class Flyable:
        def __init__(self, flying_speed):
           self.flying_speed = flying_speed  
        
        def fly(self, name, location):
            print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
                .format(name, location, self.flying_speed))
        
# 공중 공격 유닛 클래스
class FlyableAttackUnit(Flyable, AttackUnit):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed 0
        Flyable.__init__(self, flying_speed)
        
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# 건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass
    
# 서프라이 디폿 : 건물, 1개 건물 = 8 유닛.
supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")
    
def game_over():
    pass

game_start()
game_over()